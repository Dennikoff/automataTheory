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
            if vertex2.name[0] != 'e':
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
    return dka_M

def check_string(dka, string):
    temporary = ''
    for i in dka:
        for j in i:
            if j.start:
                temporary = j
    for string_index, char in enumerate(string):
        try:
            index = temporary.transition.index(char)
        except ValueError:
            return None, False
        temporary = temporary.child[index]
    return None, temporary.end


def make_transitions(dka1, dka2, language):
    number1 = dka1[len(dka1)-1].name[1:]
    number2 = dka2[len(dka2)-1].name[1:]
    err1 = DkaM('e' + str(int(number1) + 1))
    err2 = DkaM('e' + str(int(number2) + 1))
    dka1.append(err1)
    dka2.append(err2)
    i = 0
    while i < max(len(dka1), len(dka2)):
        for char in language:
            if i < len(dka1):
                try:
                    index = dka1[i].transition.index(char)
                except ValueError:
                    dka1[i].transition.append(char)
                    dka1[i].child.append(err1)
            if i < len(dka2):
                try:
                    index = dka2[i].transition.index(char)
                except ValueError:
                    dka2[i].transition.append(char)
                    dka2[i].child.append(err2)
        i+=1


def get_language(dka1, dka2):
    language = set()
    for transition in dka1[0].transition:
        language.add(transition)
    for transition in dka2[0].transition:
        language.add(transition)
    return language


if __name__ == '__main__':
    mdka1 = main.compile_('(a*bc*)*', 1)
    mdka2 = main.compile_('b*', 1)
    language = get_language(mdka1, mdka2)
    make_transitions(mdka1, mdka2, language)
    dka = make_multiply(mdka1, mdka2, language)
    print(check_string(dka, 'aabbbbbccc')[1])

