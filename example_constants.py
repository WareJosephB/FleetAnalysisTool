fuelType = 'petrol'
costOfFuel = 549.6 # Supermarket average for Petrol: 549.6 pence/Gallon, Diesel 587.4 pence/Gallon [The AA, April 2019] 
CO2perMiles = 120.1 * 1.6093 # 120.1: Estimate 2016, best year on record for worst case scenario, in g CO2/mile
averageMPG = 51.7 # 51.7 for Petrol, 61.2 for Diesel

energyCost = 14 #cost in pence per kWh: 7p/kW [home, night], 14p/kW [home, day]

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

garage = [example_EV_1, example_EV_2, example_EV_3]
