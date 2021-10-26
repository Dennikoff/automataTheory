import string
import random
import rstr as r

Pattern_Correct1 = r"([A-Za-z\._][A-Za-z0-9\._]{5,10}:([A-Za-z\._][A-Za-z0-9\.\_]{3,8} {1,3}){1,5}$)"
Pattern_Close1 = r"([A-Za-z\._][A-Za-z0-9\._]{5,15} [A-Za-z0-9]{1,3}:([A-Za-z\._][A-Za-z0-9\.\_]{3,8} {1,3}){1,5}$)"
Pattern_Incorrect = r"([a-zA-Z ]{1,3}[ 0-9]{1,3}){4,20}"
Pattern_Incorrect_Symbols = r"[A-Za-z][\#\$\%\\][A-Za-z0-9]{5,8}:([A-Za-z][A-Za-z0-9]{5,8} ){4,7}"
Pattern_Long = r"[a-z][a-z0-9]:([a-z][a-z0-9]{60,100} ){100,1311}"
def generate(j):
    lst = []
    for _ in range(j):
        lst.append(r.xeger(Pattern_Long))
    return lst
    # lst = []
    # for _ in range(j):
    #     rand = random.random()
    #     if rand < 0.5:
    #         lst.append(r.xeger(Pattern_Correct1))
    #     elif rand < 0.7:
    #         if random.random() < 0.5:
    #             lst.append(r.xeger(Pattern_Close1))
    #         else:
    #             str = r.xeger(Pattern_Correct1)
    #             strsub = ""
    #             for i in str:
    #                 if i == ":":
    #                     break
    #                 strsub += i
    #             str += ' ' + strsub
    #             lst.append(str)
    #     else:
    #         if random.random() < 0.5:
    #             if random.random() < 0.5:
    #                 lst.append(r.xeger(Pattern_Incorrect))
    #             else:
    #                 lst.append(r.xeger(Pattern_Incorrect))#r.rstr(string.digits + string.ascii_letters + '._: ', 30, 70, include=':'))
    #         else:
    #             lst.append(r.xeger(Pattern_Incorrect_Symbols))
    # return lst

# print(r.xeger(Pattern_Correct1))
# print(r.xeger(Pattern_Close1))
# #print(r.xeger(Pattern_Close2))
# print(r.xeger(Pattern_Incorrect))
# print(r.xeger(Pattern_Incorrect_Symbols))
# print(r.rstr(string.digits + string.ascii_letters + '._: ', 30, 70, include=':'))
