#!/usr/bin/env python3



class database(object):
    def __init__(self, tmp_tuple):
        self.counter = 0
        self.original_data = []
        for ele in tmp_tuple:
            self.original_data.append(ele)

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


    def _mergeAll(self, listA, listB):
        tmp_listA = listA
        tmp_listB = listB
        tmp_list = []
        pointerA = 0
        pointerB = 0
        while(pointerA < len(tmp_listA) and pointerB < len(tmp_listB)):
            if tmp_listA[pointerA] < tmp_listB[pointerB]:
                self.counter += 1
                tmp_list.append(tmp_listA[pointerA])
                pointerA += 1
            elif tmp_listA[pointerA] > tmp_listB[pointerB]:
                self.counter += 1
                tmp_list.append(tmp_listB[pointerB])
                pointerB += 1
        if pointerA == len(tmp_listA):
            tmp_list.extend(tmp_listB)
        elif pointerB == len(tmp_listB):
            tmp_list.extend(tmp_listA)
        return tmp_list

example = database((9,8,7,6,5,4,3,2,1,0,-1))
print(example.mergeSort())
print(example.counter)