class Tree:
    def __init__(self, root = ''):
        self.root = root
        self.left = None
        self.right = None
        self.cur = None

    def add_left_t(self, root):
        self.left = root
        return self

    def add_right_t(self, root):
        self.right = root
        return self

    def add_left_r(self, root):
        self.left = Tree()
        self.left.root = root
        return self

    def add_right_r(self, root):
        self.right = Tree()
        self.right.root = root
        return self

    def is_right(self):
        return self.right == None

    def is_left(self):
        return self.left == None

def print_tree(tree, kek = -1,tab = -1, end = '\n'):
    if tree == None:
        return
    tab+=1
    kek+=1
    print_tree(tree.right,kek, tab)
    print(kek, '     '*tab, tree.root, sep='', end=end)
    print_tree(tree.left, kek, tab)

