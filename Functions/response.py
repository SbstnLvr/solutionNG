def powerRounder(power):
    return round(float(power), 1)

def responseBuilder(sortedUnits, load):
    remaining = float(load)

    for unit in sortedUnits:
        if unit["type"] != "windturbine":
            continue

        give = min(unit["avail"], remaining)
        unit["p"] = give
        remaining = remaining - unit["p"]

        if remaining <= 0:
            break

    for unitIndex, unit in enumerate(sortedUnits):
        if unit["type"] == "windturbine":
            continue

        if remaining <= 0:
            unit["p"] = 0.0
            continue

        pmin = float(unit["pmin"])
        pmax = float(unit["pmax"])

        target = min(pmax, remaining)

        if target <= 0.0:
            unit["p"] = 0.0
            continue
            
        if target >= pmin:
            unit["p"] = target
            remaining = remaining - unit["p"]
            continue

        unit["p"] = pmin
        excess = pmin - target

        previousIndex = unitIndex - 1

        while excess > 0 and previousIndex >= 0:
            previous = sortedUnits[previousIndex]
            currentPower = previous.get("p", 0.0)
            lowerCap = 0.0 if previous["type"] == "windturbine" else float(previous["pmin"])
            reducible = currentPower - lowerCap
            if reducible > 0.0:
                take = min(reducible, excess)
                previous["p"] = currentPower - take
                excess = excess - take
            previousIndex -= 1

        if excess > 0:
            unit["p"] = 0.0
        else:
            remaining = remaining - target

    response = [{"name": unit["name"], "p": powerRounder(unit.get("p", 0.0))} for unit in sortedUnits]
    return response