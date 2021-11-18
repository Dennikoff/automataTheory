from classes import Tree as tr
import MakeTree as mt
from makeNka import make_nka
from classes.Nka import print_nka

string = input("Введите строку\n>>")
tree = mt.make_Tree(string)
tr.print_tree(tree)
nka = make_nka(tree)
nka.finish()
print_nka(nka)

