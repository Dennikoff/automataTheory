from classes import Tree as tr
import classes.Nka as Nka

def make_nka(tree):
    if tree == None:
        return None
    if tree.is_right() and tree.is_left():
        new = Nka.Nka()
        new.create_new_child(tree.root)
        return new
    arg1 = make_nka(tree.right)
    arg2 = make_nka(tree.left)
    if tree.root == '|':
        cur_end = Nka.Nka()
        arg1.add_child_tail('~', cur_end)
        arg2.add_child_tail('~', cur_end)
        cur_start = Nka.Nka()
        cur_start.add_child('~', arg1)
        cur_start.add_child('~', arg2)
        return cur_start
    if tree.root == '.':
        arg1.tail.name += arg2.name
        if len(arg2.child) == 1:
            arg1.add_child_tail(arg2.transition[0], arg2.child[0])
        else:
            arg1.add_childs_tail(arg2.transition, arg2.child)
        arg1.tail = arg2.tail
        return arg1
    if tree.root == '*':
        cur_end = Nka.Nka()
        cur_start = Nka.Nka()
        arg1.add_child_loop('~', arg1)
        arg1.add_child_tail('~', cur_end)
        cur_start.add_child('~', cur_end)
        cur_start.add_child('~', arg1)
        return cur_start
    if tree.root == '+':
        cur_end = Nka.Nka()
        cur_start = Nka.Nka()
        arg1.add_child_loop('~', arg1)
        arg1.add_child_tail('~', cur_end)
        cur_start.add_child('~', arg1)
        return cur_start



# tree = tr.Tree('|')
# tree.add_right_r('|')
# tree.right.add_right_r('.')
# tree.right.right.add_right_r('g')
# tree.right.right.add_left_r('k')
# tree.right.add_left_r('b')
# tree.add_left_r('a')
#
# tr.print_tree(tree)
# nk = make_nka(tree)
# nk.finish()
# Nka.print_nka(nk)




