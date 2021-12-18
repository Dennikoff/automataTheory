import sys

from classes.Tree import print_tree
from MakeTree import make_Tree
from makeNka import make_nka
from classes.Nka import print_nka
from classes import Dka
from makeDka import make_dka
from minDka import min_dka
from checkString import check_string
from makeRegularEx import get_regex as gr

def compile_(string, flag=0):
    #try:
    tree, groups = make_Tree(string, flag)
    #except Exception:
    #    print("Something went wrong")
    #    sys.exit(-1)
    #print_tree(tree)
    language = set()
    nka = make_nka(tree, language)
    nka.finish()
    #print_nka(nka)
    dka = make_dka(nka, language)
    #Dka.print_dka(dka)
    minDka = min_dka(dka, language)
    print('\n\n\n')
    Dka.print_dka(minDka)
    if flag != 0:
        print(f"Your Regular expression:{gr(minDka)}")
    return minDka

# строки для проверки алгоритма воссоздания регулярного выражения: 1) (kek){4,} 2)(kek)+  3)((a|1)|(b|2)(d|3)*(c|4))*(b|2)(d|3)*
# 4)(mephi)|(m(s)*u)|lel|pop 5)[1-5]*  группы захвата: %(([a-z]*) %)*

string = input("Введите регулярное выражение\n>>")
dka = compile_(string, 1)
for i in range(10):
    string_check = input("Введите строку для проверки\n")
    groups, flag = check_string(dka, string_check)
    if flag:
        print(f"{groups[0]}\n{flag}\n")
        for index, i in enumerate(groups):
            print(index, ':  ', i)
    else:
        print(string_check, '\n', flag)


