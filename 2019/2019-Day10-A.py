from aocd.models import Puzzle
import math

puzzle = Puzzle(year=2019, day=10)

data = puzzle.input_data.split("\n")

# data=["......#.#.","#..#.#....","..#######.",".#.#.###..",".#..#.....","..#....#.#","#..#....#.",".##.#..###","##...#..#.",".#....####"]
# data=[".#..#",".....","#####","....#","...##"]
meteorlist = []
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == "#":
            meteorlist.append((x, y))
print("number of meteroit", len(meteorlist))


def isIn(a, b, c):
    """ nachazi ze bod c mezi  bodem a a b"""
    if (a[0] < c[0] and b[0] < c[0]) or (a[0] > c[0] and b[0] > c[0]):
        return False
    if (a[1] < c[1] and b[1] < c[1]) or (a[1] > c[1] and b[1] > c[1]):
        return False
    return True


def isblock(observ, targ, blck):
    """ zjistuje za blck blokuje porimy pohled z observ na targ"""
    direction = (observ[0] - targ[0], observ[1] - targ[1])
    norm = (direction[1], -direction[0])
    c = -((norm[0] * observ[0]) + (norm[1] * observ[1]))
    if (((norm[0] * blck[0]) + (norm[1] * blck[1]) + c) == 0) and isIn(observ, targ, blck):
        return True
    return False


maxcnt = 0
bestresult = ()
for observer in meteorlist:  # couning
    cnt = 0
    for target in meteorlist:
        if (observer == target):  # check
            continue

        is_blocked = False
        for block in meteorlist:  # block
            if block == observer or block == target:
                continue
            if isblock(observer, target, block):
                is_blocked = True
                break
        if not is_blocked:
            cnt += 1

    if cnt > maxcnt:
        maxcnt = cnt
        bestresult = observer
        print(" max:", maxcnt, " =>", bestresult)

print("2019-Day10-A result:", maxcnt, " ", bestresult)
puzzle.answer_a = maxcnt
