# !/usr/bin/env python3
'''
Test Is_member assignment, CIS 210 

Author: Zhipeng Xie

Credits: 'python.org' official document

Testing function in Is_member.py 
'''
import unittest

class database(object):
    def __init__(self, tmp_tuple, target):
        '''
        (Tuple, number) -> None

        Effect: To initail the class, sorting the
        tuple and setting the target

        Input: Tuple needed to search and target

        No output at this moment
        '''
        self.original_data = tmp_tuple
        self.original_data = sorted(self.original_data)
        self.target = target

    def __str__(self):
        '''
        () -> None

        Effect: Make the class printing friendly

        No input needed

        Output: Formatted output result
        >>>  example = database((), 1)
             print(example)
        'To find: 1
        In the sequence: []
        Recursive result: False
        Iterative result: False'
        >>>  example = database((2,1), 1)
             print(example)
        'To find: 1
        In the sequence: [2,1]
        Recursive result: True
        Iterative result: True'
        '''
        result = 'To find: %d' % self.target
        result += '\nIn the sequence: %s' % str(self.original_data)
        result += '\nRecursive result: %s' % self._isMemberR(
            self.original_data)
        result += '\nIterative result: %s' % self._isMemberI()
        return result

    def _isMemberR(self, data):
        '''
        (tuple) -> Bool

        Effect: Using recursive method to determine
        whether the target is in the tuple or not

        Input: A tuple, this tuple will become smaller(half of the privious 
        tuple) after the comparsion between target and the mid of the tuple

        Output: The bool result of whether the target is the member or not

        >>>  example = database((), 1)
             print(example._isMemberR(example.original_data))
        'False'
        >>>  example = database((2,1), 1)
             print(example._isMemberR(example.original_data))
        'True'
        '''
        len_of_data = len(data)
        Half_of_len = len_of_data // 2
        # base case 1: The cases which shows target is not in the tuple
        if (len_of_data == 1 and data[0] != self.target) or len_of_data == 0:
            return False
        elif self.target > data[Half_of_len]:
            return self._isMemberR(data[Half_of_len:len_of_data])
        elif self.target < data[Half_of_len]:
            return self._isMemberR(data[:Half_of_len])
        # base case 2: After Eliminating all the impossible, what we have now
        # must be the truth
        else:
            return True

    def _isMemberI(self):
        '''
        (None) -> None

        Effect: Using iterative method to determine whether the target
        is in the tuple

        No Input needed

        Output: The bool result of whether the target is the member or not

        >>>  example = database((), 1)
             print(example._isMemberI())
        'False'
        >>>  example = database((2,1), 1)
             print(example._isMemberI())
        'True'
        '''
        tmp_last_pos = len(self.original_data) - 1
        tmp_start_pos = 0
        while tmp_start_pos <= tmp_last_pos:
            pos_of_mid = tmp_start_pos + (tmp_last_pos) // 2
            if self.original_data[pos_of_mid] == self.target:
                return True

            elif tmp_last_pos == tmp_start_pos:
                return self.original_data[tmp_last_pos] == self.target

            elif self.original_data[pos_of_mid] < self.target:
                tmp_start_pos = pos_of_mid + 1

            elif self.original_data[pos_of_mid] > self.target:
                tmp_last_pos = pos_of_mid - 1

            else:
                print('something wrong')
        return False


class test_isMember(unittest.TestCase):

    def test_is_member(self):
        '''
        (None) -> None

        Effect: To test is_member functions in the database class

        No input needed

        Nothing return, but print result

        >>> unnittest.main()
        Test will start
        Testing: ((23, 24, 25, 26, 27), 5)
        Passed!
        Testing: ((0, 1, 2, 3, 4, 5, 6), 3)
        Passed!
        Testing: ((0, 1, 4, 5, 6, 8), 4)
        Passed!
        Testing: ((43,), 44)
        Passed!
        Testing: ((), 99)
        Passed!
        Testing: ((99, 100), 101)
        Passed!
        Testing: ((42,), 42)
        Passed!
        Testing: ((1, 3, 5, 7), 4)
        Passed!
        Testing: ((1, 3), 1)
        Passed!
        Testing: ((2, 10), 10)
        Passed!
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.001s       # 1 test means this ONE test-function

        OK
        '''
        test_cases = {((1,3,5,7), 4):False, ((23,24,25,26,27), 5): False,
                     ((0, 1, 4, 5, 6, 8), 4): True, ((0, 1, 2, 3, 4, 5, 6), 3): True,
                     ((1,3),1): True, ((2,10),10): True, ((99, 100), 101): False,
                     ((42,), 42): True, ((43,), 44): False, ((), 99): False
                     }
        for test_case in test_cases:
            print('Testing:' ,test_case)
            tmp_case = database(test_case[0], test_case[1])
            self.assertEqual(tmp_case._isMemberI(), test_cases[test_case])
            self.assertEqual(tmp_case._isMemberR(tmp_case.original_data), test_cases[test_case])
            print('Passed!')

        return None


if __name__ == '__main__':
    print('Test will start')
    unittest.main()

'''
Since I've used the unittest, I think I've already implement the
challenges as well
'''
