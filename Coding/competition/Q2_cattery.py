#!/usr/bin/env/python3
def main():
    def str_handler(raw_str):
        vectors = []
        vector_way = (1, 0)
        current = (0, 0)

        for move in raw_str:
            if move == 'S' or move == 'F':
                current = (current[0] + vector_way[0],
                           current[1] + vector_way[1])
            elif move == 'L':
                vector_way = (-vector_way[1], vector_way[0])
                current = (current[0] + vector_way[0],
                           current[1] + vector_way[1])
            elif move == 'R':
                vector_way = (vector_way[1], -vector_way[0])
                current = (current[0] + vector_way[0],
                           current[1] + vector_way[1])

            vectors.append(current)
        return vectors

    def solution(vectors):
        '''
        Main idea is to use the fact that Cross product
        of two vector is the area of parallelogram builed 
        by these two vector
        '''
        def cross(v1, v2):
            return v1[0] * v2[1] - v1[1] * v2[0]

        area = 0.0
        for i in range(len(vectors) - 1):
            area += cross(vectors[i], vectors[i + 1])
        area /= 2
        return area

    num_test_case = int(input('num_input:'))

    for case in range(num_test_case):

        the_string = input('string:')

        handled_info = str_handler(the_string)

        print(solution(handled_info))

main()