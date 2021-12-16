from classes import Dka


def make_dka(nka, language):
    list_dka_vertex = []
    start_vertex = Dka.e_transition([nka])
    start = Dka.Dka(start_vertex)
    for vertex in start_vertex:
        if vertex.end:
            start.end = True
    start.start = True
    list_dka_vertex.append(start)
    i = 0
    vertexes = []
    while i < len(list_dka_vertex):
        for char in language:
            for vertex in list_dka_vertex[i].vertexes:
                for index, transition in enumerate(vertex.transition):
                    if transition == char:
                        vertexes.append(vertex.child[index])
            new_vertexes = Dka.e_transition(vertexes)
            vertexes = []
            check = vertex_in_the_list(list_dka_vertex, new_vertexes)
            if check[0]:
                list_dka_vertex[i].transition.append(char)
                list_dka_vertex[i].child.append(list_dka_vertex[check[1]])
                continue
            current = Dka.Dka(new_vertexes)
            for k in current.vertexes:
                if k.end:
                    current.end = True
            list_dka_vertex[i].transition.append(char)
            list_dka_vertex[i].child.append(current)
            list_dka_vertex.append(current)
        i+=1
    return list_dka_vertex

def vertex_in_the_list(list, vertex):
    for index, el in enumerate(list):
        if el.vertexes == vertex:
            return [True, index]
    return [False]