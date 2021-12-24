from collections import namedtuple as nt


def error_state(state):
    for child in state.child:
        if child != state:
            return False
    return True


def check_string(mdka, string, flag_groups=0):
    if flag_groups == 0:
        stack_start_indexes = []
        stack_groups = []
        el1 = nt('el1', ['string', 'number'])
        el2 = nt('el2', ['index', 'number'])
        temporary = ''
        number = 0
        string += ')'
        for i in range(len(mdka)):
            if mdka[i].start:
                temporary = mdka[i]
        for string_index, char in enumerate(string):
            while True:
                try:
                    if not error_state(temporary.child[temporary.transition.index(char)]):
                        break
                except ValueError:
                    if char == ')':
                        pass
                    else:
                        return None, False
                flag = True
                ind_exclamation_mark = ind_question_mark = 0
                try:
                    ind_exclamation_mark = temporary.transition.index('!')
                    ind_question_mark = temporary.transition.index('?')
                except ValueError:
                    flag = False
                if flag:
                    next_symbol = True
                    if not error_state(temporary.child[ind_exclamation_mark]) and not error_state(temporary.child[ind_question_mark]):
                        try:
                            next_symbol = not(error_state(temporary.child[ind_exclamation_mark].child[temporary.child[ind_exclamation_mark].transition.index(string[string_index])]))
                        except Exception:
                            if char == ')':
                                next_symbol = False
                            else:
                                return None, False
                    if not error_state(temporary.child[ind_exclamation_mark]) and next_symbol:
                        ind = string_index
                        element = el2(ind, number)
                        number += 1
                        stack_start_indexes.append(element)
                        temporary = temporary.child[ind_exclamation_mark]
                    elif not error_state(temporary.child[ind_question_mark]):
                        start_index = stack_start_indexes.pop()
                        group = string[start_index.index:string_index]
                        stack_groups.append(el1(group, start_index.number))
                        temporary = temporary.child[ind_question_mark]
                    else:
                        break
            if string_index == len(string) - 1:
                break
            try:
                index = temporary.transition.index(char)
            except ValueError:
                return None, False
            temporary = temporary.child[index]
        i = 0
        number = 0
        groups = []
        while len(stack_groups) != 0:
            if stack_groups[i].number == number:
                groups.append(stack_groups.pop(i).string)
                i = 0
                number += 1
                continue
            i+=1
            if i >= len(stack_groups):
                break
        return groups, temporary.end
    else:
        temporary = ''
        for i in range(len(mdka)):
            if mdka[i].start:
                temporary = mdka[i]
        for string_index, char in enumerate(string):
            try:
                index = temporary.transition.index(char)
            except ValueError:
                return None, False
            temporary = temporary.child[index]
        return None, temporary.end
