def CO2Parser(amountCO2):
        if amountCO2 > 1000000:
            return str(int(amountCO2/1000000))+" tons"
        elif amountCO2 > 1000:
            return str(int(amountCO2/1000))+" kg"
        else:
            return str(int(amountCO2))+" grams"

def showReport(dayArray, averageMPG, energyCost, garage, fuelType, CO2perMiles, costOfFuel):
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
            estimatedFuelBurnt += dayArray.T.sum()[i]/float(input("Miles per gallon for vehicle: " + dayArray.T.sum().index[i]+"? "))
    
    print ("Total: "+str(int(totalMiles)) + " miles; burning an estimated "+str(int(estimatedFuelBurnt*100)/100)+" gallons of "+fuelType+" and releasing an estimated "+CO2Parser(CO2perMiles*totalMiles)+" of CO2.")
    print ("At current costs: £"+str(int(estimatedFuelBurnt*costOfFuel)/100) + " of "+fuelType+" or claimable from the HMRC: £"+str(int(totalMiles*45)/100))
    
    for vehicle in garage:
        print ("For the "+vehicle.name+", £"+str(int(100*energyCost*totalMiles/vehicle.kWperMile)/100))

def reportText():
    returnText = ''
    returnText += 'Total: '+str(int(totalMiles)) + ' miles; burning an estimated '+str(int(estimatedFuelBurnt*100)/100)+' gallons of '+fuelType+' and releasing an estimated '+CO2Parser(CO2perMiles*totalMiles)+' of CO2.'
    returnText += '\n'
    returnText += 'At current costs: £'+str(int(estimatedFuelBurnt*costOfFuel)/100) + ' of '+fuelType+' or claimable from the HMRC: £'+str(int(totalMiles*45)/100)
    returnText += '\n'
    for vehicle in garage:
        returnText += "For the "+vehicle.name+", £"+str(int(100*energyCost*totalMiles/vehicle.kWperMile)/100)
    return returnText