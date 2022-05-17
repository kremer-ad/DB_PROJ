from random import random
from sys import argv
import random
from unittest import result
import datetime
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
    carsCsv = open(garagesPath,'r')
    cars = carsCsv.readlines()
    results = []
    for car in cars:
        results.append(int(car.split(',')[0]))
    return results

def generateInactiveData(cars,percent,garages):
    results = []
    id = 0
    for car in cars:
        if random.random()<percent:
            results.append(f"{id},{car},")
            id +=1
            


def generateOldData(amount,cars,garages):
    return []

def __main__():
    ACTIVE_AMOUNT = int(argv[1])
    INACTIVE_IN_FIX_PERCENT = float(argv[2])
    CARS_PATH = argv[3]
    GARAGES_PATH =  argv[4]
    nonActiveCars = loadNonActiveCars(argv[2])
    garages = loadGarages(GARAGES_PATH)
    allCars = loadAllCars(CARS_PATH)
    data = generateInactiveData(nonActiveCars,INACTIVE_IN_FIX_PERCENT,garages)
    data+=generateOldData(ACTIVE_AMOUNT,allCars,garages)
    resultFile = open("resultsFix.csv",'w')
    resultFile.writelines(data)



__main__()