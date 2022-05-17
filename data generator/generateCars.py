
from sys import argv
import random


# argv[1] - amount, argv[2] = not active ration, argv[3] = models path.

def loadModels(path):
    results = []
    modelsCsv = open(path, 'r')
    lines = modelsCsv.readlines()
    for line in lines:
        results.append(line.split(',')[0])
    modelsCsv.close()
    return results


def generateData(amount, notActiveRatio, models):
    data = []
    licenseNumbers = random.sample(range(10000000, 99999999), amount)
    for x in range(amount):
        licenseNumber = licenseNumbers[x]
        # licenseNumber = x*100-458972 +54784123/((x % 10)+1)*((x % 100/10)+1)
        # while licenseNumber<10000000:
        #     licenseNumber*=10
        model = random.choice(models)
        year = random.randint(2017, 2022)
        isActive = random.random() < notActiveRatio
        data.append(f"{x},{int(licenseNumber)},{model},{year},{isActive}\n")
    return data


def __main__():
    models = loadModels(argv[3])
    data = generateData(int(argv[1]),float(argv[2]), models)
    results = open('results.csv', 'w')
    results.writelines(data)
    results.close()


__main__()
