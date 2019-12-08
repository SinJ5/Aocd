from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=6)
orbits = [(x.split(")")) for x in puzzle.input_data.split("\n")]


class OrbitDescription:

    def __init__(self, me):
        self.orbiters = []
        self.me = me
        self.parent = None

    def addOrbiters(self, orb):
        self.orbiters.append(orb)

    def setParent(self, parent):
        self.parent = parent

    def cnt(self, deep):
        return len(self.orbiters) * deep + sum([x.cnt(deep + 1) for x in self.orbiters])


seznam = {}

for orb in orbits:
    fr = seznam.get(orb[0])
    to = seznam.get(orb[1])
    if fr is None:
        fr = OrbitDescription(orb[0])
        seznam[orb[0]] = fr
    if to is None:
        to = OrbitDescription(orb[1])
        seznam[orb[1]] = to
    fr.addOrbiters(to)
    to.setParent(fr)

result = seznam.get("COM").cnt(1)
print("result:", result)

puzzle.answer_a = result
