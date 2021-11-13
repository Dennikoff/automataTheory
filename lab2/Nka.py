# import makeNka


class Nka:
    max_name = 'a0'
    def __init__(self):
        Nka.max_name = get_next_name(Nka.max_name)
        self.name = Nka.max_name
        self.transition = []
        self.child = []
        self.tail = None

    def create_new_child(self, transition):
        new_child = Nka()
        self.transition.append(transition)
        self.child.append(new_child)
        return self

    def add_new_child(self, transition, child):
        self.transition.append(transition)
        self.child.append(child)
        return self

def get_next_name(name):
    digit = int(name[1:])
    digit += 1
    return name[:1] + str(digit)

for _ in range(20):
    cur = Nka()
    print(cur.name)
