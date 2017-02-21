import unittest
from merge import database

class test_case(unittest.TestCase):

    '''
    setUp & tearDown are used to do something
    before and after each test case executes
    '''
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    '''
    each test case should start with 'test_xxx'

    the most common used test is 'assertEqueal(a,b)'
    '''
    def test_init(self):
        empty_list = []
        one_ele_list = [1]
        chr_list = ['d', 'c', 'b', 'a']
        num_list = [5,4,3,2,1]
        
        empty_instance = database(empty_list)
        self.assertEqual(empty_instance.mergeSort(),[])

        one_ele_instance = database(one_ele_list)
        self.assertEqual(one_ele_instance.mergeSort(), [1])

        chr_list_instance = database(chr_list)
        self.assertEqual(chr_list_instance.mergeSort(), ['a','b','c','d'])

        num_list_instance = database(num_list)
        self.assertEqual(num_list_instance.mergeSort(), [1,2,3,4,5])

    def test_anotherTest(self):
        pass

    def test_one_another_test(self):
        pass

if __name__ == '__main__':
    print('hi')
    unittest.main()