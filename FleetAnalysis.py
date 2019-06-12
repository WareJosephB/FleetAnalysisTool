fileLocation = 'filename.csv'
encoding = 'cp1252' #Default is 'UTF8' if throws error try 'cp1252'
companyName = 'Customer Name' #For Chart Titles

vehicleIdentifier = 'VEHICLE_IDENT' #These should be the column name of the correct column
mileageColumn = 'TOTAL_MILES'
dateColumn = 'JOURNEY_DATE'
departmentColumn = 'DEPARTMENT' #Needed if showBarChart is True, otherwise ignored


fuelType = 'petrol'
costOfFuel = 549.6 # Supermarket average for Petrol: 549.6 pence/Gallon, Diesel 587.4 pence/Gallon [The AA, April 2019] 
CO2perMiles = 120.1 * 1.6093 # 120.1: Estimate 2016, best year on record for worst case scenario, in g CO2/mile
averageMPG = 51.7 # 51.7 for Petrol, 61.2 for Diesel

energyCost = 7 #cost in pence per kWh: 7p/kW [home, night], 14p/kW [home, day]

class EV: #Always using 'worst case' scenario: highway driving at -10c
    def __init__(self, name, mileRange, kWperMile):
        self.name = name;
        self.mileRange = mileRange;
        self.kWperMile = kWperMile;

example_EV_1=EV("Nissan Leaf e+", 155, 385)   
example_EV_2=EV("Tesla Model 3 SR", 135, 340)
example_EV_3=EV("Kia e-niro", 165, 385)

garage = [example_EV_1, example_EV_2, example_EV_3]

showReport = True
showBoxPlot = True
showBarChart = False
saveBoxPlot = True
saveBarChar = True

labelX = -5 #Where in the x-axis the labels for the example EV ranges should be

width_px = 1920
height_px = 1080
dpi = 100

rotate_xlabels = True #True or False, note capital

'''Don't change anything below unless you've saved a backup'''


import pandas as pd
import matplotlib.pyplot as plt
import datetime


fleetFile = pd.read_csv(fileLocation,encoding=encoding, delimiter=',')


#dayArray = dayArray.reindex(index=dayArray.index.to_series().str[-2:].astype(int).sort_values().index)  '''Sorts on last 2 characters as ints'''


def CO2Parser(amountCO2):
        if amountCO2 > 1000000:
            return str(int(amountCO2/1000000))+" tons"
        elif amountCO2 > 1000:
            return str(int(amountCO2/1000))+" kg"
        else:
            return str(int(amountCO2))+" grams"

if showBoxPlot:
    X=(0, len(fleetFile.groupby(vehicleIdentifier))+0.5)
    dayArray = fleetFile.groupby([vehicleIdentifier, dateColumn])[mileageColumn].sum().unstack()
    fig1, ax1 = plt.subplots()
    fig1.set_size_inches(width_px/dpi, height_px/dpi)
    dayArray.T.boxplot()
    plt.suptitle("")
    ax1.set_title(companyName + " Fleet Analysis: " + str(datetime.date.today()))
    for vehicle in garage:
        Y=(vehicle.mileRange,vehicle.mileRange)    
        ax1.plot(X,Y)
        ax1.text(labelX, vehicle.mileRange, vehicle.name)
    if (rotate_xlabels):
        plt.xticks(rotation=90)
    if saveBoxPlot:
        fig1.savefig(companyName+' Fleet Boxplot '+ str(datetime.date.today())+'.png', dpi=dpi)


if showReport:
    forEach = 'No'
    knownMileages = input("Do you know the MPG of the vehicles? [Yes/No] - if No an average of "+str(averageMPG)+"mpg. ")
    if knownMileages == 'Yes':
        forEach = input("For each vehicle [Yes] (not recommended for many vehicles) or a fleet average [No]? ")
        if forEach == 'No':
            averageMPG = float(input("Enter fleet average MPG: "))
    
    totalMiles = 0
    estimatedFuelBurnt = 0
    
    for i in range(len(dayArray.T.sum())):
        totalMiles += dayArray.T.sum()[i]
        if (forEach != 'Yes'):
            estimatedFuelBurnt += dayArray.T.sum()[i] / averageMPG 
        else:
            estimatedFuelBurnt += float(input("Miles per gallon for vehicle: " + dayArray.T.sum().index[i]+"? "))/dayArray.T.sum()[i]
    
    print ("Total: "+str(int(totalMiles)) + " miles; burning an estimated "+str(int(estimatedFuelBurnt*100)/100)+" gallons of "+fuelType+" and releasing an estimated "+CO2Parser(CO2perMiles*totalMiles)+" of CO2.")
    print ("At current costs: £"+str(int(estimatedFuelBurnt*costOfFuel)/100) + " of "+fuelType)
    
    for vehicle in garage:
        print ("For the "+vehicle.name+", £"+str(int(100*energyCost*totalMiles/vehicle.kWperMile)/100))
    
'''if showBarChart:
    departmentArray = fleetFile.groupby([departmentColumn])[mileageColumn].sum().unstack()
    fig1, ax1 = plt.subplots()
    fig1.set_size_inches(width_px/dpi, height_px/dpi)
    departmentArray. ''' #Unfinished