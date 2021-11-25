from classes.Tree import print_tree
from MakeTree import make_Tree
from makeNka import make_nka
from classes.Nka import print_nka
from classes import Dka
from makeDka import make_dka
from minDka import min_dka
from checkString import check_string


def compile_(string):
    try:
        tree = make_Tree(string)
    except Exception:
        print("Something went wrong")
    #print_tree(tree)
    language = set()
    nka = make_nka(tree, language)
    nka.finish()
    #print_nka(nka)
    dka = make_dka(nka, language)
    #Dka.print_dka(dka)
    minDka = min_dka(dka, language)
    #print('\n\n\n')
    #Dka.print_dka(minDka)
    return minDka


string = input("Введите регулярное выражение\n>>")
dka = compile_(string)
for i in range(10):
    string_check = input("Введите строку для проверки")
    print(check_string(dka, string_check))


