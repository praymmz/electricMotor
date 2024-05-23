import unittest

def add(x, y):
    return x + y

class Test_Case_01(unittest.TestCase):
    
    def test_add_01(self):
        result = add(2, 4)
        print(f'两数和为: { result }')

    def test_add_02(self):
        result = add(5, 7)
        print(f'两数和为: { result }')

if __name__ == '__main__':
    unittest.main()
