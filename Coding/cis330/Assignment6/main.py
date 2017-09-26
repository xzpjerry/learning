

class dictionary_part(object):
    def __init__(self, filename):
        self._load_dictionary(filename)

    def _load_dictionary(self, filename):
        with open(filename, 'r') as f:
            self.dict_table = {}
            for line in f.readlines():
                self.dict_table[line.strip()] = True

    def is_word(self, word):
        return True if self.dict_table.get(word) else False


def DP(astring, dict_table):
    global DP_table
    if DP_table.get(astring):
        return DP_table[astring]

    temp_result = dict_table.is_word(astring)
    if not temp_result:
        for i in range(1, len(astring)):

            temp_result = DP(astring[:i], dict_table)[
                0] and DP(astring[i:], dict_table)[0]

            if temp_result:

                DP_table[astring] = (temp_result, DP(astring[:i], dict_table)[
                                     1] + DP(astring[i:], dict_table)[1])
                return DP_table[astring]

        DP_table[astring] = (temp_result, None)

    else:
        DP_table[astring] = (temp_result, [astring])

    return DP_table[astring]


def DPI(astring, dict_table):
    global DPI_table
    def find_the_first_word():
        for i in range(len(astring)):
            if dict_table.is_word(astring[:i]):
                DPI_table[astring[:i]] = (True, [astring[:i]])
                return i

    first_pos = find_the_first_word()
    if first_pos == None:
        return False

    for i in range(first_pos, len(astring)):
        if dict_table.is_word(astring[:i]):
            DPI_table[astring[:i]] = (True, [astring[:i]])
        if DPI_table.get(astring[:i]):

            for k in range(i, len(astring) + 1):
                if dict_table.is_word(astring[i:k]):
                    DPI_table[astring[i:k]] = (True, [astring[i:k]])
                if DPI_table.get(astring[i:k]):
                    DPI_table[astring[:k]] = (True, DPI_table[astring[:i]][
                                              1] + DPI_table[astring[i:k]][1])

    return DPI_table[astring] if DPI_table.get(astring) else (False, None)


if __name__ == '__main__':

    dictionary_file_name = 'diction10k.txt'
    word_judge = dictionary_part(dictionary_file_name)

    test_case_num = int(input())
    current_case_num = 1
    while test_case_num:
        print('Case #%s' % current_case_num)
        astring = input()
        DP_table = {}
        DPI_table = {}
        print(astring)

        print('Recursive attempt:')
        DP_result = DP(astring, word_judge)
        if DP_result[0]:
            print('YES, can be split')
            print(DP_result[1])
        else:
            print('NO, cannot be split')
        # print(DP_table)

        print('Iterative attempt:')
        DPI_result = DPI(astring, word_judge)
        if DPI_result[0]:
            print('YES, can be split')
            print(DPI_result[1])
        else:
            print('NO, cannot be split')
        # print(DPI_table)

        print('\n')

        test_case_num -= 1
        current_case_num += 1
