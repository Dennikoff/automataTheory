import sys
from collections import namedtuple as nt
from classes import Tree as tr
import random


def make_Tree(string, flag_make_groups):
    flag = False
    i = 0
    list_groups = []
    brEx = Exception("brackets are not correct")
    string = '(' + string + ')'
    while i < len(string):
        if string[i] == '%':
            i+=2
            continue
        if string[i] == '(':
            flag = True
            if flag_make_groups == 0:
                string = string[:i+1] + '!(' + string[i+1:]
                i+=3
                continue
        if string[i] == ')':
            flag = False
            if flag_make_groups == 0:
                string = string[:i] + ')?' + string[i:]
                i+=3
                continue
        if string[i] == '/' and flag:
            raise brEx
        elif string[i] == '/':
            string = string[:i] + string[i+1:]
        i += 1
    m_symbols = set('|*+{}[]()%$.-')
    flag_first = False
    flag_last = False
    list_string = []
    start = 0
    substr = ""
    el = nt('el', ['char', 'tree'])
    start_p = 0
    start_flag = False
    mul = 0
    i = 0
    while i < len(string):
        if string[i] == '%' and(string[i+1] == '(' or string[i+1] == ')'):
            string = string[:i] + string[i+1:]
        i+=1
    if string == '($)' or string == '()':
        print("string is empty")
        sys.exit(0)
    '''
    for index, char in enumerate(string):
        if char == '[':
            start_p = index
            start_flag = True
        if start_flag and char == ']':
            final_p = index
            break
    '''
    i = 0
    while i != len(string):
        if string[i] == '%':
            i += 2
        if string[i] == '.' and string[i + 1] == '.' and string[i + 2] == '.':
            string = string[:i] + '*' + string[i + 3:]
        if string[i] == '.' and string[i + 1] != '.':
            string = string[:i] + string[i + 1:]
        elif string[i] == '.' and string[i + 1] == '.' and string[i + 2] != '.':
            raise Exception("bad '.' symbols")
        if (string[i] == '*' or string[i] == '+') and (string[i + 1] == '*' or string[i+1] == '+'):
            if string[i] == '+' and string[i+1] == '+':
                string = string[:i+1] + string[i + 2:]
            else:
                string = string[:i] + '*' + string[i + 2:]
            continue
        i += 1
    i = 0
    start_1 = 0
    print(string)
    flagg = False
    flag_after = False
    while i != len(string):
        if string[i] == '%':
            i += 2
            continue
        if string[i] == '[':
            start_1 = i
            start_p = i
            flag_first = True
        if flag_first and string[i] == ']':
            substr = ''
            for index in range(start_1, i):
                if flagg:
                    flagg = False
                    flag_after = True
                    continue
                if (m_symbols.isdisjoint(string[index])) and string[index + 1] != '-' and string[index - 1] != '-':
                    substr += string[index] + '|'
                elif string[index] == '%' and not flagg:
                    if string[index + 2] != '-':
                        substr += string[index] + string[index+1] + '|'
                    flagg = True
                    continue
                elif string[index] == '-':
                    st = string[index - 1]
                    fi = string[index + 1]
                    sub = ''
                    while st != fi:
                        if flag_after:
                            sub+= '%'
                        sub += st + '|'
                        st = chr(ord(st) + 1)
                    sub += st + '|'
                    index += 1
                    substr += sub
            substr = substr[:len(substr) - 1]
            string = string[:start_1] + '(' + substr + ')' + string[i + 1:]
            i = string.find(')', start_1)
        elif string[i] == ']':
            raise brEx
        if string[i] == '(':
            start_p = i
        if string[i] == '{':
            flag_first = True
            start = i
        if string[i] == '}' and flag_first:
            flag_first = False
            a = -1
            b = -1
            if i - start == 6:
                a = int(string[start+1]+string[start+2])
                b = int(string[start+4]+string[start+5])
            elif i - start == 5:
                a = int(string[start+1])
                b = int(string[start+3]+string[start+4])
            elif i - start == 4:
                if string[start+3] != ',':
                    a = int(string[start+1])
                    b = int(string[start+3])
                elif string[start+1].isdigit() and string[start+2].isdigit():
                    a = int(string[start+1]+string[start+2])
            elif i - start == 3:
                a = int(string[start+1])
            elif i - start == 2:
                i += 1
                continue
            if string[start - 1] == ')':
                substr = string[start_p+1:start - 1]
            else:
                substr = string[start - 1]
            if b == -1:
                substr = substr * a + '(' + substr + ')' + '*'
            elif b != -1:
                newsubstr = ''
                for h in range(a, b + 1):
                    newsubstr = newsubstr + '(' + ('('+substr + ')')*h + ')' + '|'
                newsubstr = newsubstr[:len(newsubstr) - 1]
                substr = newsubstr
            if string[start - 1] == ')':
                string = string[:start_p] + '(' + substr + ')' + string[i+1:]
                i = start_p + len(substr) + 1
                print(string[i])
            else:
                string = string[:start-1] + '(' + substr + ')' + string[i+1:]
                i = start + len(substr)
                print(string[i])
        elif string[i] == '}':
            raise brEx
        i += 1
    print(string)
    flag = False
    for char in string:
        cur = char
        if char == '%' and not flag:
            flag = True
            continue
        if char == ' ':
            cur = 'space'
        if m_symbols.isdisjoint(char) or flag:
            cur = f"{cur}-node"
            flag = False
        list_string.append(el(cur, tr.Tree(char)))
    # cr = 'a'
    # fi = 'z'
    # while cr != fi:
    #     print(cr)
    #     cr = chr(ord(cr)+1)
    # print(cr)
    flag_first = False
    while list_string[0].char == '(' or list_string[len(list_string) - 1].char == ')':
        if (list_string[0].char == '(') != (list_string[len(list_string) - 1].char == ')'):
            raise brEx
        for index, char in enumerate(list_string):
            if char.char == '(':
                if list_string[index + 1].char == ')':
                    del list_string[index:index + 2]
                    flag_first = True
                    flag_last = True
                    break
                start = index
                flag_first = True
            if flag_first and char.char == ')':  # находим скобочки
                flag_first = False
                i = start + 1
                while list_string[i].char != ')':
                    if list_string[i].char == '{':
                        start_index_of_the_figure = i  # индекс {
                        i += 1
                        digit = 0
                        while list_string[i].char != '}':
                            digit += int(list_string[i].tree.root) * 10
                            i += 1
                        end_index_of_the_figure = i
                        digit //= 10
                        tree = tr.Tree('.')
                        tree.add_left_t(list_string[start_index_of_the_figure - 1].tree)
                        tree.add_right_t(list_string[start_index_of_the_figure - 1].tree)
                        for k in range(digit - 2):
                            cur_tree = tr.Tree(".")
                            cur_tree.add_right_t(tree)
                            cur_tree.add_left_t(list_string[start_index_of_the_figure - 1].tree)
                            tree = cur_tree
                        node = el("{}-node", tree)
                        list_string[start_index_of_the_figure - 1] = node
                        list_string[start_index_of_the_figure - 1:end_index_of_the_figure + 1] = [
                            list_string[start_index_of_the_figure - 1]]
                        i = start_index_of_the_figure - 1
                    i += 1
                i = start + 1
                while list_string[i].char != ')':
                    if list_string[i].char == '+' and list_string[i - 1].char.endswith("node") and list_string[
                        i + 1].char != '*':
                        node = el("+-node", list_string[i].tree.add_right_t(list_string[i - 1].tree))
                        # a**** меняем на a* a**+ меняем на a* a+* меняем на a+
                        list_string[i - 1] = node
                        list_string[i - 1:i + 1] = [list_string[i - 1]]
                        i -= 1
                    elif list_string[i].tree.root == '+' and (
                            not (list_string[i - 1].char.endswith("node")) or list_string[i + 1].char == '*'):
                        sys.exit(-1)
                    i += 1
                i = start + 1
                while list_string[i].char != ')':
                    if list_string[i].char == '*' and list_string[i - 1].char.endswith("node"):
                        node = el("*-node", list_string[i].tree.add_right_t(list_string[i - 1].tree))
                        list_string[i - 1] = node
                        list_string[i - 1:i + 1] = [list_string[i - 1]]
                        i -= 1
                    elif list_string[i].tree.root == '*' and not (list_string[i - 1].char.endswith("node")):
                        sys.exit(-1)
                    i += 1
                i = start + 1
                while list_string[i].char != ')':
                    if list_string[i].char.endswith("node") and list_string[i - 1].char.endswith("node"):
                        tree = tr.Tree('.')
                        tree.add_left_t(list_string[i].tree)
                        tree.add_right_t(list_string[i - 1].tree)
                        node = el(".-node", tree)
                        list_string[i - 1] = node
                        list_string[i - 1:i + 1] = [list_string[i - 1]]
                        i -= 1
                    i += 1
                i = start + 1
                while list_string[i].char != ')':
                    if list_string[i + 1].char.endswith("node") and list_string[i - 1].char.endswith("node") and \
                            list_string[i].char == "|":
                        tree = tr.Tree('|')
                        tree.add_right_t(list_string[i + 1].tree)
                        tree.add_left_t(list_string[i - 1].tree)
                        node = el("|-node", tree)
                        list_string[i - 1] = node
                        list_string[i - 1:i + 2] = [list_string[i - 1]]
                        i -= 1
                    elif (not (list_string[i + 1].char.endswith("node")) or not (
                            list_string[i - 1].char.endswith("node"))) and list_string[i].char == "|":
                        sys.exit(-1)
                    i += 1
                # list_groups.append(string[start + 1:index])
                # substr = string[start + 1:index]
                # string = string[:start] + '"' + str(num) + '"' + string[index + 1:]
                # num += 1
                # print(string)
                # tr.print_tree(list_string[start + 1].tree, -1)
                list_string[start:start + 3] = [list_string[start + 1]]
                break
    return list_string[0].tree, list_groups
