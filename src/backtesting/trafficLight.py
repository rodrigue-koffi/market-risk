def trafficLight(nExceptions: int) -> str:
    if nExceptions <= 4:
        return "Green"
    elif nExceptions <= 9:
        return "Yellow"
    else:
        return "Red"
