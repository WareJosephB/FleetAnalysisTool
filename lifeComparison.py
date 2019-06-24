import constants
from prettytable import PrettyTable

VAT = 20 # %
EVcostIncludesTax = True
EVVATexempt = True

numberVehicles = 9
lifeSpanYears = 5
depreciationFactor = numberVehicles / lifeSpanYears
distancePerYear = 10000 #miles/yr, if in km / 1.609

fuelConsumption = constants.averageMPG #constants.averageMPG or enter directly miles per gallon
fuelCosts = constants.costOfFuel / 100 #constants.costOfFuel / 100 or enter directly, in pence/gallon

energyConsumption = 340 # in kW per mile, worst case
energyCosts = constants.energyCost #constants.energyCost or enter directly in pence/kWh

class vehicle:
    def __init__(self, name, vehicleCost, includesVAT, insurance, tyres, roadTax, fuelCosts, fuelConsumption, services, otherCosts=0, otherCostsExplain=''):
        self.name = name
        self.insurance = insurance
        self.tyres = tyres
        self.roadTax = roadTax
        self.fuelCosts = fuelCosts
        self.fuelConsumption = fuelConsumption
        self.otherCosts = otherCosts
        self.otherCostsExplain = otherCostsExplain
        self.services = services
        
        if includesVAT:
            self.includesVAT = vehicleCost
            self.sansTax = float("{:.2f}".format(vehicleCost * 100 / (100 + VAT)))
            
        else:
            self.sansTax = vehicleCost
            self.includesVAT = float("{:.2f}".format(vehicleCost * (100 + VAT) / 100))

ICE = vehicle("Peugeot COMBI Tepee 1.6 Diesel 2012", 11359.34, False, 100, 100, 900, fuelCosts, fuelConsumption, 200)
EV = vehicle("33kw Renault Kangoo Zei (Battery Purchase)", 17260, True, 250, ICE.tyres, 0, energyCosts, energyConsumption, 100, 350, 'Battery Lease (£100), Charge Point installation (£250)')

garage = [ICE, EV]

def yearFuelCosts (fuelCosts, fuelConsumption):
    return float("{:.2f}".format(distancePerYear * fuelCosts / fuelConsumption))

header = ['per Vehicle', 'Yearly Cost', 'Insurance', 'Tax', 'Energy costs', 'Tyres', 'Servicing', 'Other Costs']
foot = ''


def differenceMiles(EV, ICE):
    differenceCost = EV.sansTax - ICE.sansTax
    differentDistanceCost = EV.fuelCosts / EV.fuelConsumption - ICE.fuelCosts / ICE.fuelConsumption
    return 'While the Electric Vehicle is more expensive upfront, the savings in costs per mile (£'+"{:.2f}".format(-differentDistanceCost)+') are recouped after '+ "{:.0f}".format(-differenceCost/differentDistanceCost) +' miles ['+"{:.1f}".format(-differenceCost/(differentDistanceCost*distancePerYear))+' years], in addition to the ecological benefit.'

extraCosts = False #Don't change this
for vehicle in garage:
    if vehicle.otherCosts > 0:
        extraCosts = True
        foot += vehicle.name +' extra costs: ' + vehicle.otherCostsExplain + '\n'

def returnComparison():
    returnText = PrettyTable(header)
    for vehicle in garage:
        returnText.add_row([vehicle.name, "{:.2f}".format(vehicle.sansTax * depreciationFactor), vehicle.insurance, vehicle.roadTax, yearFuelCosts(vehicle.fuelCosts, vehicle.fuelConsumption), vehicle.tyres, vehicle.services, vehicle.otherCosts])
    print (str(returnText) + '\n' + foot + '\n' + differenceMiles(EV, ICE))
    return str(returnText) + '\n' + foot + '\n' + differenceMiles(EV, ICE)
