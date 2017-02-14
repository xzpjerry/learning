# !/usr/bin/env python3
'''
String_reverse.  CIS 210

Authors:  Zhipeng Xie

Credits: 'python.org' document

To reverse the inputed String in
recursive way and iterative way.
'''


class strReverse:

    def __init__(self, TXT):
        '''
        (String) -> None

        Effect: Initial the original_str, and call 
        two main function.

        Input: Target String

        Output: None

        '''
        self.original_str = TXT
        self.iterative_str = ''
        self.recursive_str = ''
        self.strReverseI()
        self.recursive_str = self.strReverseR(self.original_str)

    def strReverseR(self, TXT):
        '''
        (String) -> String

        Effect: Using recursive method to get the
        reversion of TXT.

        Input: Target String

        Output: Reversed String

        >>> print( self.recursive_str = self.strReverseR('') )
        ''
        >>> print( self.recursive_str = self.strReverseR('a') )
        'a'
        >>> print( self.recursive_str = self.strReverseR('abc') )
        'cba'
        '''
        if(len(TXT) == 2):
            first, second = TXT[1], TXT[0]
            return first + second
        elif(len(TXT) <= 1):
            return TXT
        else:
            Last_two_str = TXT[len(TXT) - 2: len(TXT)]
            The_rest_str = TXT[:len(TXT) - 2]
            result = self.strReverseR(Last_two_str) + self.strReverseR(The_rest_str)
            return result

    def strReverseI(self):
        '''
        (String) -> String

        Effect: Using iterative method to get the
        reversion of TXT.

        Input: Target String

        Output: Reversed String

        print( self.recursive_str = self.strReverseR('') )

        >>>self.original_str = ''
           self.strReverseI()
           print(self.iterative_str)
        ''
        >>>self.original_str = 'a'
           self.strReverseI()
           print(self.iterative_str)
        'a'
        >>> self.original_str = 'abc'
           self.strReverseI()
           print(self.iterative_str)
        'cba'
        '''
        for i in range(len(self.original_str) - 1, -1, -1):
            self.iterative_str += self.original_str[i]

    def __str__(self):
        '''
        None -> None

        To make the class print comparsion of
        the results of reversion of string by
        two methods.

        no input output

        >>> print(strReverse('hannah'))
        'Recursive result: hannah
         Iterative result: hannah'
        >>> print(strReverse(''))
        'Recursive result:
         Iterative result: '
         >>> print(strReverse('a'))
        'Recursive result: a
         Iterative result: a'
        '''
        return 'Recursive result: %s \nIterative result: %s' % (self.recursive_str, self.iterative_str)


a = strReverse('hannah')
print(a)
