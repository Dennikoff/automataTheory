import re


Pattern = r"( *(?P<aim_name>[A-Za-z\._][A-Za-z0-9\.\_]*) *:(?P<kk>( *[A-Za-z\._][A-Za-z0-9\.\_]* *)*)$)"
class Regex:
    set = set()
    dict = {}
#  сделать группу над звёздочкой доставать группы через группы
    def __init__(self):
        self.acceptable = False

    def checkStringRG(self, text):
        allresults = re.match(Pattern, text)
        if allresults:
            str = allresults.group('kk')
            str = re.sub(r'\s+', ' ', str)
            lst = str.split()
            lst.append(allresults.group('aim_name'))
            for word in lst:
                if(lst.count(word) > 1):
                    self.acceptable = False
                    return self.acceptable
            for word in lst:
                if self.dict.get(word):
                    self.dict[word] += 1
                else:
                    self.dict[word] = 1
            self.acceptable = True
            self.set.add(allresults.group('aim_name'))
            return self.acceptable
        else:
            self.acceptable = False
            return self.acceptable
