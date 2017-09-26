# !/usr/bin/env python3
'''
Is_member assignment, CIS 210 

Author: Zhipeng Xie

Credits: 'python.org' official document

To show whether a number is a member in a tuple
'''


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

example = database((24, 25, 26, 28), 27)
print(example)
print('****************')

example = database((1, 3, 5, 7), 4)
print(example)
print('****************')

example = database((0, 1, 4, 5, 6, 8), 4)
print(example)
print('****************')

example = database((0, 1, 2, 3, 4, 5, 6), 3)
print(example)
print('****************')

example = database((1, 3), 1)
print(example)
print('****************')

example = database((), 1)
print(example)
print('****************')

example = database((43,), 44)
print(example)
print('****************')

example = database((42,), 42)
print(example)
print('****************')

example = database((1,8,19,26,42,50,55,180,200), 26)
print(example)
print('****************')
# Challenge ONE

class starr(object):
    def __init__(self, max):
        self.max = max

    def _num_of_starr(self, n):
        '''
        Effect: Using recursive method to calculate
        the total number of the n row starr

        Input: Row number

        Output: Number of starr
         '''
        if n == 1:
            return 1
        else:
            return self._num_of_starr(n - 1) * 2 + n

    def __str__(self):
        '''
        Effect: To print the starr

        No input

        Output: The starrs of Nth row

        Example:
        >>> for i in range(1, 4):
                print(starr(i))
        '*
         ****
         ***********'
        '''
        result = '%s' % (self._num_of_starr(self.max) * '*')
        return result

print('Star printer begin:\n')
for i in range(1, 4):
    print(starr(i))

# Challenge TWO

class another_database(database):
    '''
    Inherited from the database class
    '''
    def _convertor(self, nested_list):
        '''
        (number or Iterable thing) -> list

        Effect: To convert the nested list or tuple into
        flat list

        Input: Number or Iterable object

        Output: Flat list containg all the elements of nested 
        list

        >>> print(self._convertor((1, (2,(3),4), (5, 6)), 3))
        [1, 2, 3, 4, 5, 6]
        '''
        result = []
        for ele in nested_list:
            if isinstance(ele, int):
                result.append(ele)
            else:
                result.extend(self._convertor(ele))
        return result

    def __init__(self, tmp_tuple, target):
        '''
        Setting the original data and sorting it

        Input: Raw tuple

        No output
        '''
        self.original_data = self._convertor(tmp_tuple)
        self.original_data = sorted(self.original_data)
        self.target = target

print(another_database((1, (2,(3),4), (5, 6)), 3))
'''
result:
To find: 3
In the sequence: [1, 2, 3, 4, 5, 6]
Recursive result: True
Iterative result: True
'''