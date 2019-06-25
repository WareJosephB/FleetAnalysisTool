fuelType = 'petrol'
costOfFuel = 549.6 # Supermarket average for Petrol: 549.6 pence/Gallon, Diesel 587.4 pence/Gallon [The AA, April 2019] 
CO2perMiles = 120.1 * 1.6093 # 120.1: Estimate 2016, best year on record for worst case scenario, in g CO2/mile
averageMPG = 51.7 # 51.7 for Petrol, 61.2 for Diesel

energyCost = 14 #cost in pence per kWh: 7p/kW [home, night], 14p/kW [home, day]

VAT = 20 # %

class generator:
    def __init__(self, name, company, email):
        self.name = name
        self.company = company
        self.email = email

owner = generator('name', 'company', 'name@company')

class EV: #Always using 'worst case' scenario: highway driving at -10c
    def __init__(self, name, mileRange, kWperMile):
        self.name = name;
        self.mileRange = mileRange;
        self.kWperMile = kWperMile;

example_EV_1=EV("Nissan Leaf e+", 155, 385)   
example_EV_2=EV("Tesla Model 3 SR", 135, 340)
example_EV_3=EV("Kia e-niro", 165, 385)

box_garage = [example_EV_1, example_EV_2, example_EV_3]

class vehicle:
    def __init__(self, name, vehicleCost, includesVAT, yearlyCosts, oneOffCosts, fuelCosts, fuelConsumption, otherCostsExplain=''):
        self.name = name
        self.yearlyCosts = yearlyCosts
        self.oneOffCosts = oneOffCosts
        self.fuelCosts = fuelCosts
        self.fuelConsumption = fuelConsumption
        self.otherCostsExplain = otherCostsExplain
        
        if includesVAT:
            self.includesVAT = vehicleCost
            self.sansTax = float("{:.2f}".format(vehicleCost * 100 / (100 + VAT)))
            
        else:
            self.sansTax = vehicleCost
            self.includesVAT = float("{:.2f}".format(vehicleCost * (100 + VAT) / 100))

ICE = vehicle("2019 Renault Clio", 14000, True, 931, 0, 586, 70.6, 'Insurance (£386), Tax (£145), Servicing (£400)')
EV = vehicle("2019 Renault Zoe", 21000, True, 699, 250, 14, 1/0.255, 'Charge Point installation (£250), Insurance (£399), Servicing (£300)')

comp_garage = [ICE, EV]
