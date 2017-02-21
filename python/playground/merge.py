#!/usr/bin/env python3



class database(object):
    def __init__(self, tmp_data):
        self.original_data = tmp_data
        self.counter = 0
        print(self.mergeSort())
        print(self.counter)

    def mergeSort(self):
        if len(self.original_data) != 0:
            self.sorted_data = self._mergeSort(self.original_data)
            return self.sorted_data
        else:
            return []

    def _mergeSort(self, tmp_list):
        len_of_list = len(tmp_list)
        if len_of_list == 1:
            return tmp_list
        mid_pos = len_of_list // 2
        listA = tmp_list[:mid_pos]
        listB = tmp_list[mid_pos:len_of_list]
        listA = self._mergeSort(listA)
        listB = self._mergeSort(listB)
        return self._mergeAll(listA,listB)


    def _mergeAll(self, tmp_listA, tmp_listB):
        tmp_list = []
        len_of_a = len(tmp_listA)
        len_of_b = len(tmp_listB)
        pointerA = 0
        pointerB = 0
        while(pointerA < len_of_a and pointerB < len_of_b):
            self.counter += 1
            if tmp_listA[pointerA] < tmp_listB[pointerB]:
                tmp_list.append(tmp_listA[pointerA])
                pointerA += 1
            elif tmp_listA[pointerA] > tmp_listB[pointerB]:
                tmp_list.append(tmp_listB[pointerB])
                pointerB += 1
        if pointerA == len_of_a:
            tmp_list.extend(tmp_listB[pointerB:])
        elif pointerB == len_of_b:
            tmp_list.extend(tmp_listA[pointerA:])
        return tmp_list

example = database([-1, 0, 2, -2, 3, 6, -3, 5, 1, 4])
