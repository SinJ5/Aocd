from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=4)

input_data = [int(x) for x in puzzle.input_data.split("-")]


def podminka(num):
    tmp = num
    lastval = tmp % 10
    tmp = tmp // 10
    same_count = 0
    while tmp > 0:
        val = tmp % 10
        tmp = tmp // 10
        if (val > lastval):
            return 0
        if (val == lastval):
            same_count += 1
        lastval = val
    if (same_count > 0):
        return 1
    return 0


result = 0
for i in range(input_data[0], input_data[1], 1):
    result += podminka(i)

print("2019-Day4-A result:", result)
puzzle.answer_a=result

