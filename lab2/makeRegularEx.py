from classes.Dka import Dka
from collections import namedtuple as nt


def get_input(Dka, vertex):
    el = nt('el',['vertex', 'transition'])
    input = []
    for vertexes in Dka:
        if vertexes == vertex:
            continue
        for index, inputs in enumerate(vertexes.child):
            if inputs == vertex:
                element = el(vertexes, vertexes.transition[index])
                input.append(element)
    return input


def get_output(vertex):
    el = nt('el', ['vertex', 'transition'])
    output = []
    flag = False
    loop = None
    for index, child in enumerate(vertex.child):
        if child == vertex:
            flag = True
            loop = el(child, vertex.transition[index])
            continue
        element = el(child, vertex.transition[index])
        output.append(element)
    return output, flag, loop


def transition(vertex1, vertex2):
    for child in vertex1.child:
        if child == vertex2:
            return transition
    return ""


def get_index(Dka, vertex):
    for index, kek in enumerate(Dka):
        if kek.name == vertex.name:
            return index
    return 0

def copyy(Dkaa):
    new_list = []
    new_elem = None
    for element in Dkaa:
        new_elem = Dka()
        new_elem.end = element.end
        new_elem.start = element.start
        new_elem.name = element.name
        new_list.append(new_elem)
    for i in range(len(Dkaa)):
        for child in Dkaa[i].child:
            index = get_index(new_list, child)
            new_list[i].child.append(new_list[index])
        new_list[i].transition = Dkaa[i].transition.copy()
        i+=1
    Dka.max_name = 'a5'
    return new_list


def has_loop(vertex):
    for index, child in enumerate(vertex.child):
        if child == vertex:
            return vertex.transition[index], True
    return None, False


def clear(curDka, index):
    vertex = curDka.pop(index)
    for cur_vertex in curDka:
        i = 0
        while i != len(cur_vertex.child):
            child = cur_vertex.child[i]
            if child == vertex:
                cur_vertex.child.pop(i)
                cur_vertex.transition.pop(i)
                i -= 1
            i += 1
    return


def get_regex(minDka):
    curDka = copyy(minDka)
    i = 0
    while i < len(curDka):
        if not (curDka[i].start) and not(curDka[i].end):
            inputs = get_input(curDka, curDka[i])
            outputs, flag, loop = get_output(curDka[i])
            for inp in inputs:
                new_transitions = []
                new_child = []
                for outp in outputs:
                    trans = transition(inp.vertex, outp)
                    if len(trans) > 1:
                        trans = '(' + trans + ')'
                    if trans != "":
                        if flag:
                            new_transition = f"{trans}|({inp.transition}({loop.transition})*{outp.transition})"
                        else:
                            new_transition = f"{trans}|({inp.transition}{outp.transition})"
                    else:
                        if flag:
                            new_transition = f"{inp.transition}({loop.transition})*{outp.transition}"
                        else:
                            new_transition = f"{inp.transition}{outp.transition}"
                    inp.vertex.child.append(outp.vertex)
                    inp.vertex.transition.append(new_transition)
            clear(curDka, i)
            continue
                # inp.vertex.child = new_child
                # inp.vertex.transition = new_transitions
        i+=1
    string = ''
    for index, vertex in enumerate(curDka[0].child):
        if vertex.end == True:
            trans, flag = has_loop(vertex)
            if flag:
                if vertex.start == True:
                    string += '(' + trans + ')*|'
                else:
                    string += '((' + curDka[0].transition[index] +')(' + trans+ ')*)|'
            else:
                string+= '(' + curDka[0].transition[index] + ')|'
    string = string[:len(string)-1]
    return string