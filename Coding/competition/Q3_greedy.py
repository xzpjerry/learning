
class Solution(object):

    def __init__(self, talks):
        '''
        At first, we need to classfy every talk by its consuming time

        For example: 
            if the talks are [(1,2), (2,3), (3,4), (1,3)], there are
                2 kinds of consuming time, one is 1 and another is 2

            The self.talk_time_len should look like
            {1: [(1,2), (2,3), (3,4)], 2:[(1,3)]}
        '''

        self.talk_time_len = {}
        self.min_start = None
        self.max_end = None

        for talk in talks:
            start, end = talk
            if self.min_start == None:
                self.min_start = start
            else:
                self.min_start = min(self.min_start, start)

            if self.max_end == None:
                self.max_end = end
            else:
                self.max_end = max(self.max_end, end)

            if self.talk_time_len.get(end - start):
                self.talk_time_len[end - start].append(talk)
            else:
                self.talk_time_len[end - start] = [talk]

        self.greedy_pick()

    def greedy_pick(self):
        '''
        Build a time schedule table to memorize availability of each time

        The structure i:{'start':True, 'end':True}  means
            at ith second, it's available to start and end a talk

        i:{'start':False, 'end':True} means
            at ith second, it's available to end a talk, but cannot start a talk

        '''
        self.available_dict = {i: {'start': True, 'end': True}
                               for i in range(self.min_start, self.max_end + 1)}
        self.result = 0
        for length in self.talk_time_len:
            for talk in self.talk_time_len[length]:
                start, end = talk
                if self.available_dict[start]['start'] and self.available_dict[end]['end']:
                    self.available_dict[start]['start'] = False
                    self.available_dict[end]['end'] = False
                    if end - start > 1:
                        for i in range(start + 1, end):
                            self.available_dict[i]['start'] = False
                            self.available_dict[i]['end'] = False
                else:
                    self.result += 1

    def __str__(self):
        return str(self.result)


if __name__ == '__main__':
    '''
    sample input:
        2 
        4 
        1 2
        2 3
        3 4
        1 3
        7
        1 3
        3 6
        6 8
        1 4
        2 4
        5 7
        5 8
    sample output:
        1
        4
    '''

    num_cases = int(input())
    for case in range(num_cases):
        num_talks = int(input())
        talks = []
        for i in range(num_talks):
            start, end = input().split()
            talks.append((int(start), int(end)))

        a = Solution(talks)
        print(a)
