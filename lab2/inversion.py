from classes.Dka import Dka


def inversion(tree):
    if tree.is_right() and tree.is_left():
        return
    elif tree.is_right() and not tree.is_left():
        inversion(tree.left)
    elif not tree.is_right() and tree.is_left():
        inversion(tree.right)
    else:
        temp = tree.right
        tree.right = tree.left
        tree.left = temp
        inversion(tree.left)
        inversion(tree.right)
