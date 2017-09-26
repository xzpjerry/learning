
def main():

    test_case = int(input())
    for case in range(test_case):
        num_talks = int(input())
        if num_talks < 1:
            print(num_talks)
            continue

        talks = [(1,2), (3,4), (1,3), (2,3)]
        max_end_time = 4
        '''
        max_end_time = 0
        for a_talk in range(num_talks):
            start = int(input())
            end = int(input())
            max_end_time = max(max_end_time, end)
            talks.append((start, end))
        '''
        DP_table = {talk:1 for talk in talks}
        def DP(i, j, DP_table):
            if DP_table.get((i, j)):
                return DP_table[(i, j)]

            DP_table[(i, j)] = max(DP(i, k, DP_table) + DP(k, j, DP_table) + 1 for k in range(i + 1, j))

            return DP_table[(i, j)]

        print('********************')
        print(DP(1, max_end_time, DP_table))
        print(DP_table)

main()        