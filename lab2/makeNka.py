import Tree as tr
import Nka as nka
import sys
from collections import namedtuple as nt

head = nka.Nka()

def make_nka(tree):
    if tree.is_right() and tree.is_left():
        new = nka.Nka()
        new.create_new_child(tree.root())
    arg1 = make_nka(tree.left)
    arg2 = make_nka(tree.right)
    if tree.root == '|':
        cur_start = nka.Nka()
        cur_start.add_new_child('~', arg1)
        cur_start.add_new_child('~', arg2)
        cur_end = nka.Nka()
        arg1.






