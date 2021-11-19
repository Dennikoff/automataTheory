class Dka:
    max_name = 'a0'
    def __init__(self, vertexes=None):
        Dka.max_name = get_next_name(Dka.max_name)
        self.name = Dka.max_name
        self.vertexes = vertexes
        self.transition = []
        self.child = []
        self.start = False
        self.end = False

def print_dka(dka):
    for n in dka:
        print(f"name:{n.name}        start:{n.start}        end:{n.end}")
        for i in range(len(n.child)):
            print(f"transition: {n.transition[i]}   child:{n.child[i].name}")

def get_next_name(name):
    digit = int(name[1:])
    digit += 1
    return name[:1] + str(digit)

def e_transition(edges):
    new_edges = []
    for edge in edges:
        new_edges.append(edge)
    i = 0
    while i < len(new_edges):
        for index, k in enumerate(new_edges[i].transition):
            if k == '~':
                if not(in_the_list(new_edges, new_edges[i].child[index])):
                    new_edges.append(new_edges[i].child[index])
        i+=1
    return new_edges

def in_the_list(list, element):
    for el in list:
        if el == element:
            return True
    return False