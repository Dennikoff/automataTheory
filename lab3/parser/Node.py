class Node:
    def __init__(self, type, data = '', children=None, lineno=-1):
        if not children:
            children = []
        self.type = type
        self.data = data
        self.children = children
        self.lineno = lineno

    def __repr__(self):
        if isinstance(self.data, Node):
            return f"Type: {self.type};  Data: some node: {self.data};"
        return f"Type: {self.type};  Data: {self.data};"

    def __str__(self, kek=0):
        result = kek*'    ' + repr(self) + '\n'
        for child in self.children:
            result += child.__str__(kek+1)
        return result

if __name__ == '__main__':
    node = Node('kek', children=Node('a', 'b'))
    # print(node)
    root = Node('1', 0, lineno=1)
    childL = Node('left', 0, lineno=1)
    childR = Node('right', 0, lineno=1)
    childRchildR = Node('rr', 0, lineno=1)
    childRchildL = Node('rl', 0, lineno=1)
    childLchildL = Node('ll', 0, lineno=1)
    childLchildR = Node('lr', 0, lineno=1)
    root.children.append(childL)
    root.children.append(childR)
    childL.children.append(childLchildR)
    childL.children.append(childLchildL)
    childR.children.append(childRchildR)
    childR.children.append(childRchildL)
    print(root)

