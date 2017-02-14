# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.plainele = None
        self.tmp_list = None
        self.ori_list = nestedList
        self.ended = False
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        for element in self.ori_list:
            if isInteger(element):
                self.plainele = element
            else:
                self.tmp_list = getList(element)
                while getList(self.tmp_list) != None:
                    self.tmp_list = getList(self.tmp_list)
                for ele in self.tmp_list:
                    yield ele
            yield self.plainele
        ended = True
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        return self.ended


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())