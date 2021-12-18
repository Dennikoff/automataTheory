import unittest
from checkString import check_string
from main import compile_


class Test1(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('kek|lol|orbidol')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'kek')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'lol')[1], True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'orbidol')[1], True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'keklol')[1], False)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, 'klol')[1], False)

    def test_string6(self):
        self.assertEqual(check_string(self.minDka, 'loll')[1], False)


class Test2(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('l(d|l)...')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'llllllllllddddldldld')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'lddddddddddddddddddddd')[1], True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'ldddddddddddddldddldldldldldddld')[1], True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'dddddddddddddddl')[1], False)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, 'dllllllllllllllllllllllll')[1], False)

    def test_string6(self):
        self.assertEqual(check_string(self.minDka, '')[1], False)


class Test3(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('[a-zA-Z]([a-zA-Z]|[0-9])*')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'kek441')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'shmek')[1], True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'YaVolnaNovayaVolna')[1], True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'a')[1], True)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, 'abrikosNaYugeRos_')[1], False)

    def test_string6(self):
        self.assertEqual(check_string(self.minDka, '666MORGENSHTERN666')[1], False)

    def test_string7(self):
        self.assertEqual(check_string(self.minDka, '')[1], False)


class Test4(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('([a-zA-Z]|[0-9])+')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, '888echpochmak888')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'yaGenadiyGorin')[1], True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, '')[1], False)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, '456 abrikos Na Yuge Ros')[1], False)


class Test5(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('a.b.o.b.a')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'aboba')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'a.b.o.b.a')[1], False)


class Test6(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('ha{3}')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'haaa')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'haaaa')[1], False)


class Test7(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('string1|string%*|string%||string%.|string%[%]%{%}')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'string*')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'string|')[1], True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'string[]{}')[1], True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'string.')[1], True)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, 'string%.')[1], False)


class Test8(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('[a-z0-9]{5,10}')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'keklol222')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, '0123456789')[1], True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, '1a2b3c4d')[1], True)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, '1234')[1], False)

    def test_string5(self):
        self.assertEqual(check_string(self.minDka, '12345678910')[1], False)


class Test9(unittest.TestCase):
    def setUp(self):
        self.minDka = compile_('c{15,}')
    def test_string1(self):
        self.assertEqual(check_string(self.minDka, 'ccccccccccccccc')[1], True)

    def test_string2(self):
        self.assertEqual(check_string(self.minDka, 'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')[1], True)

    def test_string3(self):
        self.assertEqual(check_string(self.minDka, 'cccccccccc')[1], False)

    def test_string4(self):
        self.assertEqual(check_string(self.minDka, 'ccccccccccccccccccccccccccccccca')[1], False)


if __name__ == '__main__':
    unittest.main()
