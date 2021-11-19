class Nka:
    max_name = 'a0'

    def __init__(self, name=None):
        if name:
            self.name = name
            self.transition = []
            self.child = []
            self.tail = None
            self.start = False
            self.end = False
            self.printed = False
        else:
            Nka.max_name = get_next_name(Nka.max_name)
            self.name = Nka.max_name
            self.transition = []
            self.child = []
            self.tail = None
            self.start = False
            self.end = False
            self.printed = False

    def create_new_child(self, transition):
        new_child = Nka()
        self.transition.append(transition)
        self.child.append(new_child)
        self.tail = self.child[0]
        return self

    def add_child(self, transition, child):
        self.transition.append(transition)
        self.child.append(child)
        self.tail = child.tail
        return self

    def add_child_tail(self, transition, child):
        self.tail.transition.append(transition)
        self.tail.child.append(child)
        self.tail = self.tail.child[len(self.tail.child) - 1] #для дебага loop

    def add_childs_tail(self, transition, child):
        self.tail.transition.append(transition[0])
        self.tail.transition.append(transition[1])
        self.tail.child.append(child[0])
        self.tail.child.append(child[1])
        self.tail = self.tail.child[0]

    def add_child_loop(self, transition, child):
        self.tail.child.append(child)
        self.tail.transition.append(transition)

    def finish(self):
        self.start = True
        self.tail.end = True

def print_nka(nka):
    if nka.printed:
        return
    nka.printed = True
    if len(nka.child) == 0:
        print(f"name:{nka.name} End:{nka.end}")
        return
    if len(nka.child) == 1:
        print(f"name:{nka.name}  transition:{nka.transition[0]}  name child:{nka.child[0].name}  Start:{nka.start}")
        print_nka(nka.child[0])
    else:
        print(f"name:{nka.name}  transition:{nka.transition[0]}  name child:{nka.child[0].name}  Start:{nka.start}\nname:{nka.name}  transition:{nka.transition[1]}  name child:{nka.child[1].name}  Start:{nka.start}")
        print_nka(nka.child[0])
        print_nka(nka.child[1])


def get_next_name(name):
    digit = int(name[1:])
    digit += 1
    return name[:1] + str(digit)
