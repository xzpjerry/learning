
MR = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


def solution(M):
    wait_list = []
    counter = 0
    for row in M:
        if 1 not in row:
            wait_list.append(counter)
        counter += 1

    top = wait_list.pop()

    for row in M:
        if row[top] != 1 and row != M[-1]:
            if len(wait_list):
                top = wait_list.pop()
            else:
                return False
    return True

    return wait_list

def solution2(M):
    class Vertex:
        def __init__(self, key, nbrs = []):
            self.id = key
            self.connectedTo = []
            counter = 0
            for v in nbrs:
                if v == 1:
                    self.addNeighbor(counter)
                counter += 1

        def addNeighbor(self, nbr):
            self.connectedTo.append(nbr)

        def __str__(self):
            return str(self.id) + ' is connected to: ' + str([x for x in self.connectedTo])

        def getConnections(self):
            return self.connectedTo

        def getID(self):
            return self.id

    counter = 0
    vertices = []
    for row in M:
        tmp = Vertex(counter, row)
        vertices.append(tmp)
        counter += 1
    for v in vertices:
        print(v)


if __name__ == '__main__':
    print(solution(MR))
    solution2(MR)
