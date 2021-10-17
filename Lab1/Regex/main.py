import random
import sys
import regex
import datetime as dt
import randomizer as ran

# rg = regex.Regex()
# rg.checkStringRG("kek: lol orbidol")
# print(rg.aim)
retcode = 0
success = 0
dictstr = {}
choice = int(input("Откуда вы хотите читать\n1-Файл\n2-Клавиатура\n3-Генерация\n4-Запись в файл\n"))
if choice == 1:
    fname = input("Введите имя файла\n")
    f = open(fname+'.txt', 'r')
    rg = regex.Regex()
    date = dt.datetime.now()
    for line in f:
        line = line[:-1]
        if not(rg.checkStringRG(line)):
            result = "not acceptable"
            retcode = 1
        else:
            result = "acceptable"
        print('The string "%s" is %s.\n' % (line, result))
    print(dt.datetime.now() - date)
    f.close()
    statistics = {}
    for i in rg.set:
        if rg.dict.get(i) != None:
            statistics[i] = rg.dict[i]
    print(statistics)

elif choice == 2:
    rg = regex.Regex()
    str = input("Введите строчку\n")
    retcode = 0
    if not(rg.checkStringRG(str)):
        result = "not acceptable"
        retcode = 1
    else:
        result = "acceptable"
    print('The string "%s" is %s.\n' % (str, result))
elif choice == 3:
    rg = regex.Regex()
    k = int(input("Введите кол-во строк"))
    lst = ran.generate(k)
    date = dt.datetime.now()
    for i in lst:
        if rg.checkStringRG(i) == False:
            result = "not acceptable"
            retcode = 1
        else:
            result = "acceptable"
        print(f"The string \"{i}\" is {result}")
    print(dt.datetime.now() - date)
elif choice == 4:
    fname = input("Введите имя файла\n")
    f = open(fname+'.txt', 'w')
    strList = ['mep: x1 x2 x3 x4', 'mephi: x1 x2 x3 x3', 'mephi: mephi x2 x3 x4', 'masdfagg', 'mehi: x1_ x3.x3.x1 ff. x3 ff','mephi::ffdsf gg ddf', 'mephi:x1fdsf fds x2']
    for _ in range(760):
        f.write(strList[random.randint(0, 6)]+'\n')
    f.close()
sys.exit(retcode)
# '.' is 46, 'num' 48-57 ':' is 58, 'A' is 65 'Z' is 90, '_' is 95, 'a' is 97 'z' is 122