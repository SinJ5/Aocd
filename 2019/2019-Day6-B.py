from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=6)
orbits = [(x.split(")")) for x in puzzle.input_data.split("\n")]


class OrbitDescription:

    def __init__(self, me):
        self.orbiters = []
        self.me = me
        self.parent = None
        self.deep = 0

    def addOrbiters(self, orb):
        self.orbiters.append(orb)

    def setParent(self, parent):
        self.parent = parent

    def cnt(self):
        return len(self.orbiters)


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

you = seznam.get("YOU")

seen = {}
queue = [you]


def search(orb):
    if orb.me in seen:
        return False
    if orb.me == "SAN":
        result = orb.deep
        puzzle.answer_b = result - 2
        print("in search result", result - 2)
        return True
    for o in orb.orbiters:
        if o.me in seen:
            continue
        else:
            o.deep = orb.deep + 1
            queue.append(o)
    if not ((orb.parent is None) or (orb.parent.me in seen)):
        orb.parent.deep = orb.deep + 1
        queue.append(orb.parent)


while True:
    tmp = queue.pop(0)
    if search(tmp):
        break;
    seen[tmp.me] = tmp
