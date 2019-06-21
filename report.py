import constants
from prettytable import PrettyTable


def CO2Parser(amountCO2):
        if amountCO2 > 1000000:
            return str(int(amountCO2/1000000))+" tons"
        elif amountCO2 > 1000:
            return str(int(amountCO2/1000))+" kg"
        else:
            return str(int(amountCO2))+" grams"

def reportText(dayArray, companyName):
    estimated = True
    forEach = 'No'
    knownMileages = input("Do you know the MPG of the vehicles? [Yes/No] - if No an average of "+str(constants.averageMPG)+"mpg. ")
    if knownMileages == 'Yes':
        forEach = input("For each vehicle [Yes] (not recommended for many vehicles) or a fleet average [No]? ")
        if forEach == 'No':
            averageMPG = float(input("Enter fleet average MPG: "))
    else:
        averageMPG = constants.averageMPG
    totalMiles = 0
    estimatedFuelBurnt = 0
    
    for i in range(len(dayArray.T.sum())):
        totalMiles += dayArray.T.sum()[i]
        if (forEach != 'Yes'):
            estimatedFuelBurnt += dayArray.T.sum()[i] / averageMPG 
        else:
            estimatedFuelBurnt += dayArray.T.sum()[i]/float(input("Miles per gallon for vehicle: " + dayArray.T.sum().index[i]+"? "))
            estimated = False
        
    returnText = PrettyTable([companyName, ''])
    returnText.add_row(["Total Miles", str(int(totalMiles))])
    returnText.add_row(["Miles per Gallon"+"*"*estimated, str(averageMPG)])
    returnText.add_row(["Total Gallons*", str(int(100*estimatedFuelBurnt)/100)])
    returnText.add_row(["Carbon Footprint*", CO2Parser(constants.CO2perMiles*totalMiles)])

    #for vehicle in constants.garage:
     #   returnText += '\n'
      #  returnText += "For the "+vehicle.name+", £"+str(int(100*constants.energyCost*totalMiles/vehicle.kWperMile)/100)
    return returnText