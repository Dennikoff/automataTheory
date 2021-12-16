from classes import Dka


def min_dka(dka, language):
    groups = []
    group1 = []
    group2 = []
    for i in dka:
        if not(i.end):
            group1.append(i)
        else:
            group2.append(i)
    if len(group1) != 0:
        groups.append(group1)
    groups.append(group2)
    flag1 = True
    while flag1:
        flag1 = False
        i = 0
        while i < len(groups):
            group = groups[i]
            for char in language:
                new_group = {}
                for vertex in group:
                    for index in range(len(vertex.transition)):
                        if vertex.transition[index] == char:
                            if not(new_group.get(char)):
                                new_group[char] = ([[vertex, vertex.child[index]]])
                            else:
                                new_group[char].append([vertex, vertex.child[index]])
                letter = new_group[char]
                number_of_group = in_group(groups, letter[0][1])
                flag = False
                new_created_group = []
                new_group_old = []
                for transition in letter:
                    if in_group(groups, transition[1]) != number_of_group:
                        new_created_group.append(transition[0])
                        flag = True
                        flag1 = True
                    else:
                        new_group_old.append(transition[0])
                if not(flag):
                    continue
                groups[i:i+1] = [new_group_old, new_created_group]
                i-=1
                break
            i+=1
    minDka = []
    Dka.Dka.max_name = 'a0'
    for group in groups:    # создаю минимальный автомат без переходов
        new_vertex = Dka.Dka(group)
        minDka.append(new_vertex)
    for index, group in enumerate(groups):    # добавляю переходы в созданный автомат
        for vertex in group:
            if vertex.start:
                minDka[index].start = True
            if vertex.end:
                minDka[index].end = True
            for index2, transition in enumerate(vertex.transition):
                if in_the_list(minDka[index].transition, transition):
                    continue
                minDka[index].transition.append(transition)
                minDka[index].child.append(minDka[in_group(groups, vertex.child[index2])])
    return minDka


def in_the_list(list, element):
    for el in list:
        if el == element:
            return True
    return False

def in_group(groups, my_vertex):
    for index, group in enumerate(groups):
        for vertex in group:
            if my_vertex == vertex:
                return index
    return -1