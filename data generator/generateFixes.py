from random import random
from sys import argv
import random
from unittest import result
from datetime import datetime,timedelta

FLAG_DATE = datetime(1, 1, 1, 0, 0)

def loadNonActiveCars(carsPath):
    carsCsv = open(carsPath,'r')
    cars = carsCsv.readlines()
    results = []
    for car in cars:
        if car.split(',')[4][1:] == 'False':
            results.append(int(car.split(',')[0]))
    return results


def loadAllCars(carsPath):
    carsCsv = open(carsPath,'r')
    cars = carsCsv.readlines()
    results = []
    for car in cars:
        results.append(int(car.split(',')[0]))
    return results

def loadGarages(garagesPath):
    carsCsv = open(garagesPath,'r',encoding='utf-8')
    cars = carsCsv.readlines()
    results = []
    for car in cars:
        results.append(int(car.split('\t')[0]))
    return results

def generateInactiveData(cars,percent,garages):
    results = []
    id = 0
    for car in cars:
        if random.random()<percent:
            days_to_subtract = random.randint(1,8)
            start_date = datetime.now()-timedelta(days=days_to_subtract)
            garage = random.choice(garages)
            results.append(f"{id},{car},{start_date},{FLAG_DATE},{garage}\n")
            id +=1
    return id,results
            


def generateOldData(startId,amount,cars,garages):
    results = []
    id = startId
    for x in range(amount):
        car = random.choice(cars)
        days_to_subtract = random.randint(30,700)
        days_to_add = random.randint(1,15)
        start_date = datetime.now()-timedelta(days=days_to_subtract)
        end_date = start_date+timedelta(days=days_to_add)
        garage = random.choice(garages)
        results.append(f"{id},{car},{start_date},{end_date},{garage}\n")
        id +=1
    return results

def __main__():
    ACTIVE_AMOUNT = int(argv[1])
    INACTIVE_IN_FIX_PERCENT = float(argv[2])
    CARS_PATH = argv[3]
    GARAGES_PATH =  argv[4]
    nonActiveCars = loadNonActiveCars(CARS_PATH)
    garages = loadGarages(GARAGES_PATH)
    allCars = loadAllCars(CARS_PATH)
    lastId,data = generateInactiveData(nonActiveCars,INACTIVE_IN_FIX_PERCENT,garages)
    data+=generateOldData(lastId+1,ACTIVE_AMOUNT,allCars,garages)
    resultFile = open("resultsFix.csv",'w')
    resultFile.writelines(data)



__main__()