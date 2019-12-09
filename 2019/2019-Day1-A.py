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


for tmp in data:
    val = fuelCount(tmp)
    summary += val

print("2019-Day1-A result: ", summary)

puzzle.answer_a = summary
