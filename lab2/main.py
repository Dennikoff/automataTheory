from classes import Tree as tr
import MakeTree as mt
from makeNka import make_nka
from classes.Nka import print_nka
from classes import Dka
from makeDka import make_dka

string = input("Введите строку\n>>")
tree = mt.make_Tree(string)
tr.print_tree(tree)
language = set()
nka = make_nka(tree, language)
nka.finish()
print_nka(nka)
dka = make_dka(nka, language)
