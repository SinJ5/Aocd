from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=1)

data = puzzle.input_data.split("\n")

summary = 0


def fuelCount(mass):
    """Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module
    , take its mass, divide by three, round down, and subtract 2."""
    tmpVal = int(mass) / 3
    tmpVal = int(tmpVal)
    return tmpVal - 2


def fuel_for_fuel(mass):
    tmpsum = 0
    tmp_val = mass
    while tmp_val > 0:
        tmpsum += tmp_val
        tmp_val = fuelCount(tmp_val)

    return tmpsum - mass


for tmp in data:
    val = fuelCount(tmp)
    summary += val
    summary += fuel_for_fuel(val)

print("2019-Day1-B result: ", summary)
puzzle.answer_b = summary
