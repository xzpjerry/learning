M = [
    [0, None, None, None, -1, None],
    [1, 0, None, 2, None, None],
    [None, 2, 0, None, None, -8],
    [-4, None, None, 0, 3, None],
    [None, 7, None, None, 0, None],
    [None, 5, 10, None, None, 0]
]


def relax(row, row_num, comparing_row, entrance_wei, M):

    pointer = 0
    for wei in row:
        if comparing_row[pointer] != None:
            if wei == None:
                M[row_num][pointer] = entrance_wei + comparing_row[pointer]
            else:
                M[row_num][pointer] = min(
                    wei, entrance_wei + comparing_row[pointer])
        pointer += 1


current = 0

for i in range(len(M)): #

    pointer = 0
    for row in M: # check each vertex one by one
        if row != M[current]:

            if row[current]: # this vertex can connect to current checking vetex

                relax(row, pointer, M[current], row[current], M)

        pointer += 1

    current += 1

    print(M)
