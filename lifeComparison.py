from prettytable import PrettyTable, MSWORD_FRIENDLY
from constants import comp_garage as garage

numberVehicles = 9
lifeSpanYears = 5
depreciationFactor = numberVehicles / lifeSpanYears
distancePerYear = 25000 #miles/yr, if in km / 1.609

def yearFuelCosts (fuelCosts, fuelConsumption):
    return float("{:.2f}".format(distancePerYear * fuelCosts / 100 / fuelConsumption))

header = ['', 'Fleet cost/yr', 'Yearly costs', 'One Off costs', 'Fuel costs']
foot = ''


def differenceMiles(EV, ICE):
    differenceCost = EV.sansTax - ICE.sansTax
    differentDistanceCost = (EV.fuelCosts / EV.fuelConsumption - ICE.fuelCosts / ICE.fuelConsumption)/100
    return 'While the Electric Vehicle is more expensive upfront, the savings in costs per mile (£'+"{:.2f}".format(-differentDistanceCost)+') are recouped after '+ "{:.0f}".format(-differenceCost/differentDistanceCost) +' miles ['+"{:.1f}".format(-differenceCost/(differentDistanceCost*distancePerYear))+' years at '+str(distancePerYear)+'/year], in addition to the ecological benefit.'

extraCosts = False #Don't change this
for vehicle in garage:
    if vehicle.otherCostsExplain != '':
        extraCosts = True
        foot += vehicle.name +' extra costs: ' + vehicle.otherCostsExplain + '\n'

def returnComparison():
    returnText = PrettyTable(header)
    returnText.set_style(MSWORD_FRIENDLY)
    for vehicle in garage:
        returnText.add_row([vehicle.name, "{:.2f}".format(vehicle.sansTax * depreciationFactor), vehicle.yearlyCosts, vehicle.oneOffCosts, yearFuelCosts(vehicle.fuelCosts, vehicle.fuelConsumption)])
    return str(returnText) + '\n' + foot + '\n' + differenceMiles(garage[1], garage[0])
