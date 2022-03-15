from ast import arg
from sqlite3 import Cursor
from sys import exit
from sys import argv
from turtle import end_poly
from unittest import result
import cx_Oracle

ARGV_LEN = 7  # py connection csv types name delimiter output


def main():
    if len(argv) == 2 and argv[1] == "-h":
        print_help()
        return
    elif len(argv) != ARGV_LEN:
        bad_argv(len(argv))
    config = read_config(argv[1])
    csv = open(argv[2])
    if not csv.readable():
        bad_csv_path(argv[2])
    
    #generate the results file
    need_results = argv[6]=='-'
    if need_results:
        results_file = open(argv[6],'w')
        if not results_file.writable():
            bad_results_path(argv[6])
        results_file.write('')
        results_file.close()
        results_file = open(argv[6],'a')
        if not results_file.writable():
            bad_results_path(argv[6])
    #create the table

    
    #add all the data to the table
    end_of_csv = False
    while not end_of_csv:
        next_line = csv.readline()
        if not next_line:
            end_of_csv = True
        else:
            sql,data = generate_insert_SQL(next_line,argv[4],argv[5])
            if need_results:
                results_file.write(f"{sql}\t{data}\n")
            execute_sql(config,sql,data)
    


def bad_results_path(path):
    print(f"cant open {path} forn write")
    exit()

def read_config(config_path):
    config_file = open(config_path)
    config = {}
    if not config_file.readable():
        bad_config_path(config_path)
    for line in config_file.readlines():
        config[line.split(' ')[0]] = line.split(' ')[1]
    if ['name', 'password', 'ip', 'port', 'dbname', 'encoding'] not in config.keys():
        bad_config_file(config_path)
    config_results = {
        "username" : config["name"],
        "password" : config["password"],
        "dsn" : cx_Oracle.makedsn("localhost", "1521", "orcl"),
        "port" : 1512,
        "encoding" : 'UTF-8'
    }

def bad_csv_path(path):
    print(f"cant open {path} for read")
    exit()

def connect(config):
    return cx_Oracle.connect(config["username"],config["password"],encoding = config["encoding"])

def generate_insert_SQL(csv_line,table_name,delimiter):
    data = csv_line.split(delimiter)
    params_str = ""
    for i in range(len(data)):
        params_str+=f':p{str(i)},'
    params_str = params_str[0,-1]
    sql = f"insert into {table_name} values({params_str})"
    return sql,data

def execute_sql(config,sql,data):
    try:
        with connect(config) as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(sql,data)
                connection.commit()
                return result
    except cx_Oracle.Error as error:
        print(f"an error was occured while executing '{sql}' with data {data}")
        print(error)
        exit()

    

def bad_config_file(path):
    print(f"the file {path} has missing parameters.")
    print(f"you can run '{argv[0]} -h' for help")
    exit()


def bad_config_path(path):
    print(f"cant open {path} for read")
    exit()


def bad_argv(num):
    print(f"The program must have {ARGV_LEN-1} parameters")
    print(f"you can run '{argv[0]} -h' for help")
    exit()


def print_help():
    print("csv to Oracledb")
    print("The command will look like:")
    print(f"{argv[0]} [config] [csv] [types] [name] [delimiter] [output]")
    print("config - file that contains the connection data in the format below:")
    print("\tname [user name]")
    print("\tpassword [password]")
    print("\tip [database server ip]")
    print("\tport [database port]")
    print("\tdbname [database name (at most is orcl)]")
    print("\tencoding [encoding (at most UTF-8)]")
    print("csv - the csv file name")
    print("types - file that contains all the data types, for example the scheme tab(id:number,name:nvarchar,credit:number) will look like this:")
    print("\tname nvarchar")
    print("\tcredit number")
    print("name - the table name")
    print("delimiter - the delimiter character")
    print("output - an output file for the sql results, for no output give the value -")
    exit()


main()
