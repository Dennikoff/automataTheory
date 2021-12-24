from classes.dkaMultiply import DkaM
import main


def in_the_list(list, element):
    for el in list:
        if el == element:
            return True
    return False


def make_multiply(mdka1, mdka2, language):
    dka_M = []
    start_vertex = ''
    for vertex1 in mdka1:
        cur_row = []
        for vertex2 in mdka2:
            vertex2.name = 'b' + vertex2.name[1:]
            cur1 = DkaM((vertex1.name, vertex2.name), (vertex1, vertex2))
            if vertex1.start and vertex2.start:
                cur1.start = True
                start_vertex = cur1
            if vertex1.end and vertex2.end:
                cur1.end = True
            cur_row.append(cur1)
        dka_M.append(cur_row)
    for vertex in dka_M:
        for vert in vertex:
            print(vert.name, end=';   ')
        print()
    print(dka_M[0][0].name[0])
    stack = []
    i = 0
    stack.append(start_vertex)
    while i < len(stack):
        vertex = stack[i]
        i += 1
        print(vertex.name)
        # print(vertex_a, vertex_b)
        for char in language:
            index1 = vertex.vertexes[0].transition.index(char)
            #находим индекс вершины в которую мы попадаем из вершины (vartexes[0]) по char
            index2 = vertex.vertexes[1].transition.index(char)
            cur_vertex = dka_M[int(vertex.vertexes[0].child[index1].name[1:]) - 1][int(vertex.vertexes[1].child[index2].name[1:]) - 1]
            #рассматриваем вершину, в которую мы можем перейти по букве из vertex[0] и [1] по char
            if not(in_the_list(vertex.child, cur_vertex)) or not(in_the_list(vertex.transition, char)):
                vertex.transition.append(char)
                vertex.child.append(cur_vertex)
                cur_vertex.count += 1
                vertex.count += 1
                if not(in_the_list(stack, cur_vertex)):
                    stack.append(cur_vertex)
    for vertex in dka_M:
        index = 0
        while index < len(vertex):
            vert = vertex[index]
            if vert.count == 0:
                vertex.pop(index)
                index -= 1
            index += 1
    print('kek')

mdka1 = main.compile_('abc*', 1)
mdka2 = main.compile_('ab*c', 1)
make_multiply(mdka1, mdka2, ['a', 'b', 'c'])

