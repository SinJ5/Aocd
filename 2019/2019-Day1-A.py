f = open("Day1a", "r")
data = f.readlines()
f.close()

sumary = 0


def fuelCount(mass):
    """Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module
    , take its mass, divide by three, round down, and subtract 2."""
    tmpVal = int(mass) / 3
    tmpVal = int(tmpVal)
    return tmpVal - 2


for tmp in data:
    val = fuelCount(tmp)
    sumary += val

print(" sum  Part1: ", sumary)
