class DkaM:
    def __init__(self, name, vertex=None):
        self.name = name
        self.count = 0
        self.transition = []
        self.child = []
        self.start = False
        self.end = False
        self.vertexes = vertex


def print_dka(dka):
    for n in dka:
        print(f"name:{n.name}        start:{n.start}        end:{n.end}")
        for i in range(len(n.child)):
            print(f"transition: {n.transition[i]}   child:{n.child[i].name}")