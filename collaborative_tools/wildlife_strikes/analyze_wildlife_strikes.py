import matplotlib.pyplot as plt
import csv

strikesByYear = {}
strikesByMonth = {}

# only track airlines with many strikes (> 1000)
strikesByAirline = {}

numsToMonths = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def addToDictionary(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

# calculate frequencies
with open("aircraft_wildlife_strikes.csv", "r") as file:
    reader = csv.reader(file)
    next(file)

    for line in reader:
        year = int(line[1])
        airline = line[5]
        month = numsToMonths[int(line[2])]

        addToDictionary(strikesByYear, year)
        addToDictionary(strikesByAirline, airline)
        addToDictionary(strikesByMonth, month)

    # remove airlines with less than 1000 strikes
    airlinesList = list(strikesByAirline.keys())
    for airline in airlinesList:
        if strikesByAirline[airline] < 1000:
            del strikesByAirline[airline]

    # generate charts/graphs here...
