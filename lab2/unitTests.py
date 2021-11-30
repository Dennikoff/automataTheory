import unittest
from checkString import check_string
from main import compile_


class Test1(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('kek|lol|orbidol')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'kek'), True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'lol'), True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'orbidol'), True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'keklol'), False)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, 'klol'), False)

    def test_string6(self):
        self.assertEqual(check_string(self.minDka, 'loll'), False)


class Test2(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('l(d|l)...')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'lllllllllddddldldldl'), True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'lddddddddddddddddddddd'), True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'ldddddddddddddldddldldldldldddld'), True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'dddddddddddddddl'), False)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, 'dllllllllllllllllllllllll'), False)

    def test_string6(self):
        self.assertEqual(check_string(self.minDka, ''), False)


class Test3(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('[a-zA-Z]([a-zA-Z]|[0-9])*')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'kek441'), True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'shmek'), True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'YaVolnaNovayaVolna'), True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'a'), True)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, 'abrikosNaYugeRos_'), False)

    def test_string6(self):
        self.assertEqual(check_string(self.minDka, '666MORGENSHTERN666'), False)

    def test_string7(self):
        self.assertEqual(check_string(self.minDka, ''), False)


class Test4(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('([a-zA-Z]|[0-9])+')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, '888echpochmak888'), True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'yaGenadiyGorin'), True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, ''), False)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, '456 abrikos Na Yuge Ros'), False)


class Test5(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('a.b.o.b.a')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'aboba'), True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'a.b.o.b.a'), False)


class Test6(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('ha{3}')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'haaa'), True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'haaaa'), False)


class Test7(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('string1|string%*|string%||string%.|string%[%]%{%}')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'string*'), True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'string|'), True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'string[]{}'), True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'string.'), True)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, 'string%.'), False)


# class Test8(unittest.TestCase):
#     def setUp(self):
#         self.minDka = compile_('[a-z0-9]{5,10}')
#     def test_string1(self):
#         self.assertEqual(check_string(self.minDka, 'keklol222'), True)
#
#     def test_string2(self):
#         self.assertEqual(check_string(self.minDka, '0123456789'), True)
#
#     def test_string3(self):
#         self.assertEqual(check_string(self.minDka, '1a2b3c4d'), True)
#
#     def test_string4(self):
#         self.assertEqual(check_string(self.minDka, '1234'), False)
#
#     def test_string5(self):
#         self.assertEqual(check_string(self.minDka, '12345678910'), False)


class Test9(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('c{15,}')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'ccccccccccccccc'), True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'), True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'cccccccccc'), False)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'ccccccccccccccccccccccccccccccca'), False)


if __name__ == '__main__':
    unittest.main()
