def check_string(mdka, string):
    temporary = mdka[0]
    for char in string:
        try:
            index = temporary.transition.index(char)
        except ValueError:
            return False
        temporary = temporary.child[index]
    return temporary.end