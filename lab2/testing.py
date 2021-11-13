import random
import sys
from collections import namedtuple as nt
import Tree as tr

m_symbols = set('|*/+{}[]()%$.-')
string = input("Enter string\n")
string = '(' + string + ')'
list_groups = []
flag_first = False
flag_last = False
list_string = []
start = 0
el = nt('el', ['char', 'tree'])
start_p = 0
start_flag = False
i = 0
mul = 0
while i != len(string):
    if string[i] == '{':
        flag_first = True
        start = i
    if string[i] == '}' and flag_first:
        flag_first = False
        if i - start == 6:
            a = int(string[start+1]+string[start+2])
            b = int(string[start+4]+string[start+5])
            mul = random.randint(a, b % 101)
        elif i - start == 5:
            a = int(string[start+1])
            b = int(string[start+3]+string[start+4])
            mul = random.randint(a, b % 101)
        elif i - start == 4:
            if string[start+3]!= ',':
                a = int(string[start+1])
                b = int(string[start+3])
                mul = random.randint(a, b % 101)
            elif string[start+1].isdigit() and string[start+3].isdigit():
                a = int(string[start+1]+string[start+2])
                mul = random.randint(a, 101)
        elif i - start == 3:
            a = int(string[start+1])
            mul = random.randint(a, 101)
        elif i - start == 2:
            mul = int(string[start+1])
        a = 0
        b = 0
        string = string[:start+1] + str(mul) + string[i:]
        i = start + 2
        while mul // 10 != 0:
            i +=1
            mul //= 10
    i+=1
print(string)
# for char in string:
#     cur = char
#     if char == ' ':
#         cur = 'space'
#     if m_symbols.isdisjoint(char):
#         cur = f"{cur}-node"
#     list_string.append(el(cur, tr.Tree(char)))
# for i in list_string:
#     print(i.char, end=' ')
#     tr.print_tree(i.tree, -1, ' ')
# i = 1
# while list_string[i].char != ')':
#     if list_string[i].char == '*' and list_string[i - 1].char.endswith("node"):
#         node = el("*-node", list_string[i].tree.add_right_t(list_string[i-1].tree))
#         list_string[i - 1] = node
#         list_string[i-1:i+1] = [list_string[i - 1]]
#         i -=1
#     elif list_string[i].tree.root == '*' and not (list_string[i - 1].char.endswith("node")):
#         sys.exit(-1)
#     i+=1
# i = 1
# while list_string[i].char != ')':
#     if list_string[i].char.endswith("node") and list_string[i - 1].char.endswith("node"):
#         tree = tr.Tree('.')
#         tree.add_left_t(list_string[i].tree)
#         tree.add_right_t(list_string[i-1].tree)
#         node = el(".-node", tree)
#         list_string[i - 1] = node
#         list_string[i - 1:i + 1] = [list_string[i - 1]]
#         i-=1
#     i+=1
# i = 1
# while list_string[i].char != ')':
#     if list_string[i + 1].char.endswith("node") and list_string[i - 1].char.endswith("node") and list_string[i].char == "|":
#         tree = tr.Tree('|')
#         tree.add_right_t(list_string[i+1].tree)
#         tree.add_left_t(list_string[i-1].tree)
#         node = el("|-node", tree)
#         list_string[i - 1] = node
#         list_string[i - 1:i + 2] = [list_string[i - 1]]
#         i-=1
#     i+=1
# print('----------------------')
# for i in list_string:
#     print(i.char)
#     tr.print_tree(i.tree, -1)