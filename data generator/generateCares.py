from random import randrange, choice
from datetime import datetime, timedelta
from sys import argv

CURRENT_YEAR = '2022'
RESULTS_DATE_FORMAT = '%Y/%m/%d %H:%M:%S'

garages = []
cars = []


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def generate_two_dates(start_year):
    start = datetime.strptime(f'1/1/{start_year} 1:00 AM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime(
        f'11/30/{CURRENT_YEAR} 1:00 AM', '%m/%d/%Y %I:%M %p')
    ret_start = random_date(start, end)
    latest_end = ret_start + timedelta(days=14)
    # print(latest_end)
    ret_end = random_date(ret_start, latest_end)
    return ret_start, ret_end


def ok_dates(start_date, end_date, results, car):
    for care in results:
        if care[1] == car:
            start_care = datetime.strptime(care.split(',')[2], RESULTS_DATE_FORMAT)
            end_care = datetime.strptime(care.split(',')[3], RESULTS_DATE_FORMAT)
            if end_date < end_care and end_date > start_care or start_date > start_care and start_date < end_care:
                return False
    return True


def generate_cares(amount, results_path):
    results = []
    results_text = ''
    for i in range(amount):
        if i%1000 ==0:
            print(i)
        while True:
            car_to_care = choice(cars)
            start_date, end_date = generate_two_dates(car_to_care[3])
            garage = choice(garages)
            if ok_dates(start_date, end_date, results, car_to_care[0]):
                res = f"{i},{car_to_care[0]},{start_date.strftime(RESULTS_DATE_FORMAT)},{end_date.strftime(RESULTS_DATE_FORMAT)},{garage}"
                results.append(res)
                results_text += res+'\r\n'
                break
    results_file = open(results_path,'w')
    results_file.write(results_text)
    results_file.close()


def load_data(cars_stock_path, garages_path):
    # read cars_stock data
    cars_file = open(cars_stock_path)
    cars_lines = cars_file.readlines()
    for line in cars_lines:
        cars.append(line.split(','))
    cars_file.close()
    # read garages data
    garages_file = open(garages_path, encoding='utf-8')
    garage_lines = garages_file.readlines()
    for line in garage_lines:
        garages.append(line.split(',')[0])
    garages_file.close()


def main():
    #cars = argv[1], garages = argv[2], amount = argv[3], rsults = argv[4]
    load_data(argv[1], argv[2])
    generate_cares(int(argv[3]), argv[4])


if __name__ == '__main__':
    main()
