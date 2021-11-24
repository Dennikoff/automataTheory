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
        self.minDka = compile_('[a-zA-Z]([a-zA-Z][0-9])*')
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
        self.minDka = compile_('([a-zA-Z][0-9])+')
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


if __name__ == '__main__':
    unittest.main()
