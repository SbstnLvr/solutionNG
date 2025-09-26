from Functions.merit import meritOrder
from Functions.response import responseBuilder
def ngMain(payload):

    load = payload["load"]
    fuels = payload["fuels"]
    plants = payload["powerplants"]

    fuelWind = fuels["wind(%)"]
    fuelGas = fuels["gas(euro/MWh)"]
    fuelKero = fuels["kerosine(euro/MWh)"]

    plantUnits = []
    for plant in plants:
        plantType = plant["type"]
        plantEff = plant["efficiency"]
        plantMin = plant["pmin"]
        plantMax = plant["pmax"]

        if plantType == "windturbine":
            produce = plantMax * (fuelWind/100)
            cost = 0
        elif plantType == "gasfired":
            produce = plantMax 
            cost = fuelGas / plantEff
        elif plantType == "turbojet":
            produce = plantMax
            cost = fuelKero / plantEff
        
        plantUnits.append({
            "name": plant["name"],
            "type": plantType,
            "efficiency": plantEff,
            "pmin": plantMin,
            "pmax": plantMax,
            "avail": produce,
            "cost": cost,
            "p": 0.0
        })

    sortedUnits = meritOrder(plantUnits)
    response = responseBuilder(sortedUnits, load)

    return response