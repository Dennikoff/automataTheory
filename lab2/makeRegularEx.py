from classes.Dka import Dka
from collections import namedtuple as nt


def get_input(Dka, vertex):
    el = nt('el', ['vertex', 'transition'])
    input = []
    for vertexes in Dka:
        if vertexes == vertex:
            continue
        for index, inputs in enumerate(vertexes.child):
            if inputs == vertex:
                element = el(vertexes, vertexes.transition[index])
                input.append(element)
    return input


def error_state(state):
    for child in state.child:
        if child != state:
            return False
    return True


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
    string = ''
    flag = False
    for index, child in enumerate(vertex.child):
        if child == vertex:
            string += vertex.transition[index] + '|'
            flag = True
    string = string[:len(string) - 1]
    return string, flag


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


def has_edge_to_start(child):
    for index, child2 in enumerate(child.child):
        if child2.start:
            return True
    return False


def all_transitions_to_end(start_vertex):
    string = ''
    for index, child in enumerate(start_vertex.child):
        if child.end == True:
            string += start_vertex.transition[index] + '|'
    string = string[:len(string) - 1]
    return string

def find_all_edges(child):
    transition_from_end = ''
    for index, child_end in enumerate(child.child):
        if child_end.start:
            transition_from_end += child.transition[index] + '|'
    transition_from_end = transition_from_end[:len(transition_from_end) - 1]
    return transition_from_end


def get_regex(minDka):
    curDka = copyy(minDka)
    i = 0
    while i < len(curDka):
        if not (curDka[i].start) and not(curDka[i].end):
            inputs = get_input(curDka, curDka[i])
            outputs, flag, loop = get_output(curDka[i])
            for inp in inputs:
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
    loop_start, flag_start = has_loop(curDka[0])
    flag_end = False
    loop_end = ''
    if len(curDka) > 1:
        loop_end, flag_end = has_loop(curDka[1])
    for index, child in enumerate(curDka[0].child):
        if child.end:
            if child.start:
                string += f"({loop_start})*|"
                string = string[:len(string) - 1]
                return string
            else:
                flag_end_trans = has_edge_to_start(child)
                transition_from_end = find_all_edges(child)
                transition_to_end = all_transitions_to_end(curDka[0])
                if flag_end_trans:
                    if flag_start:
                        if flag_end:
                            string = f"(({loop_start})|({transition_to_end})({loop_end})*({transition_from_end}))*({transition_to_end})({loop_end})*|"
                        else:
                            string = f"({loop_start}|({transition_to_end})({transition_from_end}))*({transition_to_end})|"
                    else:
                        if flag_end:
                            string = f"(({transition_to_end})({loop_end})*({transition_from_end}))*({transition_to_end})({loop_end})*|"
                        else:
                            string = f"(({transition_to_end})({transition_from_end}))*({transition_to_end})|"
                else:
                    if flag_start:
                        if flag_end:
                            string = f"({loop_start})*{transition_to_end}({loop_end})*|"
                        else:
                            string = f"({loop_start})*{transition_to_end}|"
                    else:
                        if flag_end:
                            string = f"({transition_to_end})({loop_end})*|"
                        else:
                            string = f"{transition_to_end}|"
                break
    string = string[:len(string)-1]
    return string