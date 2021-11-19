from classes.Tree import print_tree
from MakeTree import make_Tree
from makeNka import make_nka
from classes.Nka import print_nka
from classes import Dka
from makeDka import make_dka
from minDka import min_dka


def compile_(string):
    tree = make_Tree(string)
    print_tree(tree)
    language = set()
    nka = make_nka(tree, language)
    nka.finish()
    print_nka(nka)
    dka = make_dka(nka, language)
    Dka.print_dka(dka)
    minDka = min_dka(dka, language)
    print('\n\n\n')
    Dka.print_dka(minDka)


#string = input("Введите строку\n>>")
string = 'kek|lol'
compile_(string)


