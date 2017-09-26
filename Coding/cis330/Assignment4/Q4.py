#!/usr/bin/env python3

import time


graph = {
    'vertices': ['s', 'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 't'],
    'edges': {
        's': [(1, 'a1'), (50, 'b1')],
        'a1': [(1, 's'), (3, 'a2'), (10, 'b1')],
        'b1': [(50, 's'), (20, 'b2'), (10, 'a1')],
        'a2': [(3, 'a1'), (20, 'a3'), (10, 'b2')],
        'b2': [(20, 'b1'), (2, 'b3'), (10, 'a2')],
        'a3': [(20, 'a2'), (30, 't'), (10, 'b3')],
        'b3': [(2, 'b2'), (4, 't'), (10, 'a3')],
        't': [(30, 'a3'), (4, 'b3')]
    }
}


def min_cost(graph):
    current_min_dict = {vertex: None for vertex in graph['vertices']}
    current_min_dict['s'] = 0

    num_vertices = len(graph['vertices'])

    for i in range(num_vertices - 1):

        for vertex in graph['edges']:

            for wei, vt in graph['edges'][vertex]:

                if current_min_dict[vt] == None:
                    current_min_dict[vt] = current_min_dict[vertex] + wei
                else:
                    current_min_dict[vt] = min(
                        current_min_dict[vt], current_min_dict[vertex] + wei)

    return current_min_dict

start = time.time()
print(min_cost(graph))
end = time.time()
print('BF Way in %.7f' % ((end - start) * 1000)) 

'''
*********************
'''


M = 10
A = [1, 3, 20, 30]
B = [50, 20, 2, 4]
current_min_dict = {day: None for day in range(len(A) + 1)}
current_min_dict[0] = (None, 0)


def min_cost_dp(day):

    if current_min_dict[day]:
        return current_min_dict[day]

    # (last_day_city, last_day_min_cost)
    last_day_info = min_cost_dp(day - 1)

    if last_day_info[0] == None:
        first_day_min_wei = min(A[0], B[0])
        nex_day_should_at = A if first_day_min_wei == A[0] else B
        current_min_dict[day] = (nex_day_should_at, first_day_min_wei)
    else:

        opposite_city = A if last_day_info[0] == B else B

        today_min_wei = min(last_day_info[
                            1] + last_day_info[0][day - 1], last_day_info[1] + opposite_city[day - 1] + M)

        nex_day_should_at = last_day_info[0] if today_min_wei == last_day_info[
            1] + last_day_info[0][day - 1] else opposite_city

        current_min_dict[day] = (nex_day_should_at, today_min_wei)

    return current_min_dict[day]

start = time.time()
print(min_cost_dp(len(A)))
end = time.time()
print('DP Way in %.7f' % ((end - start) * 1000))
