
from sys import argv
import random

rand = random.SystemRandom()

branches = []
garages = []
colors = []

# argv[1] - amount, argv[2] = not active ratio, argv[3] = models path, argv[4] = garages path, argv[5] = branches path, argv[6] = colors path.


def loadModels(path):
    results = []
    modelsCsv = open(path, 'r')
    lines = modelsCsv.readlines()
    for line in lines:
        results.append(line.split(',')[0])
    modelsCsv.close()
    return results


def random_branch():
    return rand.choice(branches)


def random_color():
    rand = random.random()
    for color in colors:
        percent = float(color[2])/100
        if rand < percent:
            return int(color[0])
        else:
            rand -= percent
    return int(colors[0][0])


def random_garage():
    return rand.choice(garages)


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
        garage = 'NULL'
        if not isActive:
            garage = random_garage()
        branch_id = random_branch()
        color_id = random_color()
        data.append(
            f"{x},{int(licenseNumber)},{model},{year},{branch_id},{color_id}\n")
    return data


def load_files(branches_path, garages_path, colors_path):
    bfile = open(branches_path)
    blines = bfile.readlines()
    for b in blines:
        branches.append(int(b.split(',')[0][1:-1]))
    bfile.close()
    gfile = open(garages_path, encoding="utf-8")
    glines = gfile.readlines()
    for g in glines:
        garages.append(int(g.split('\t')[0]))
    gfile.close()
    cfile = open(colors_path)
    clines = cfile.readlines()
    for c in clines:
        colors.append(c.split(','))
    cfile.close()


def __main__():
    models = loadModels(argv[3])
    load_files(argv[5], argv[4],argv[6])
    data = generateData(int(argv[1]), float(argv[2]), models)
    results = open('resultsCars.csv', 'w')
    results.writelines(data)
    results.close()


__main__()
