fileLocation = 'real_data.csv'
encoding = 'UTF8' #Default is 'UTF8' if throws error try 'cp1252'
companyName = 'CUSTOMER' #For Chart Titles

vehicleIdentifier = 'CARERID' #These should be the column name of the correct column
vehicleIdentifier2 = 'COLOUR'
CombinedUniqueKey = False #Do you need both of the above to make a unique vehicle? [True/False]

mileageColumn = 'STDMILES'
dateColumn = 'THEDATE'

departmentColumn = 'DEPARTMENT' #Needed if showBarChart is True, otherwise ignored

fuelType = 'petrol'
costOfFuel = 549.6 # Supermarket average for Petrol: 549.6 pence/Gallon, Diesel 587.4 pence/Gallon [The AA, April 2019] 
CO2perMiles = 120.1 * 1.6093 # 120.1: Estimate 2016, best year on record for worst case scenario, in g CO2/mile
averageMPG = 51.7 # 51.7 for Petrol, 61.2 for Diesel

energyCost = 7 #cost in pence per kWh: 7p/kW [home, night], 14p/kW [home, day]

showReport = False
generateReport = True
buffer = 15 #Width around title of report

class generator:
    def __init__(self, name, company, email):
        self.name = name
        self.company = company
        self.email = email

owner = generator('name', 'company', 'name@company')

showBarChart = False
saveBarChart = False
rotate_xlabels_bar = [True, 45]
milesOverPercentage = 150 # Range to show percentage of journies under this distance
label_spacing = 5
rotate_bar = True

showBoxPlot = True
saveBoxPlot = True
rotate_xlabels_box = [True, -90] #True or False, note capital, degrees to rotate: 0 = horizontal, 90 = up
labelX = -1 #Where in the x-axis the labels for the example EV ranges should be
rotate_box = True #Should boxplot be vertical (False) or horizontal (True)

class EV: #Always using 'worst case' scenario: highway driving at -10c
    def __init__(self, name, mileRange, kWperMile):
        self.name = name;
        self.mileRange = mileRange;
        self.kWperMile = kWperMile;

example_EV_1=EV("Nissan Leaf e+", 155, 385)   
example_EV_2=EV("Tesla Model 3 SR", 135, 340)
example_EV_3=EV("Kia e-niro", 165, 385)

garage = [example_EV_1, example_EV_2, example_EV_3]

width_px = 595 
height_px = 842
dpi = 100

'''Don't change anything below unless you're sure- remember, it's backed up on Github so you can always pull again'''

import pandas as pd
import report, plot, reportExporter

fleetFile = pd.read_csv(fileLocation,encoding=encoding, delimiter=',')

if (CombinedUniqueKey):
    dayArray = fleetFile.groupby([vehicleIdentifier,vehicleIdentifier2, dateColumn])[mileageColumn].sum().unstack()
else:
    dayArray = fleetFile.groupby([vehicleIdentifier, dateColumn])[mileageColumn].sum().unstack()

#dayArray = dayArray.reindex(index=dayArray.index.to_series().str[-2:].astype(int).sort_values().index)  '''Sorts on last 2 characters as ints'''

if showBarChart:
    plot.showBarChart(fleetFile, departmentColumn, mileageColumn, milesOverPercentage, companyName, width_px, height_px, dpi, rotate_xlabels_bar, saveBarChart, label_spacing)

if showBoxPlot:
    plot.showBoxPlot(dayArray, rotate_box, width_px, height_px, dpi, garage, labelX, companyName, rotate_xlabels_box, saveBoxPlot)

if showReport:
    report.showReport(dayArray, averageMPG, energyCost, garage, fuelType, CO2perMiles, costOfFuel)

if generateReport:
    reportExporter.report(companyName, buffer, owner, milesOverPercentage)
