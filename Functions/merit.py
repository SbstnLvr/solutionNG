def meritOrder(plantUnits):

    def plantOrder(unit):
        windPriority = 0 if unit["type"] == "windturbine" else 1
        return (
            windPriority,
            unit["cost"],
            -unit["efficiency"],
            unit["pmin"],
            -unit["pmax"],
            unit["name"]
        )

    return sorted(plantUnits, key=plantOrder)
