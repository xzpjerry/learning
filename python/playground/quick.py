
class database(object):

    def __init__(self, alist):
        self.original_data = alist
        self.counter = 0
        print(self._quick(self.original_data))
        print(self.counter)

    def _quick(self, tmp_list):
        tmp_small_list = []
        tmp_big_list = []
        if len(tmp_list) <= 1:
            return tmp_list
        else:
            pivot = tmp_list[0]
            the_range = range(1, len(tmp_list))
            for i in the_range:
                self.counter += 1
                if tmp_list[i] < pivot:
                    tmp_small_list.append(tmp_list[i])
                else:
                    tmp_big_list.append(tmp_list[i])
            tmp_small_list.append(pivot)
            return self._quick(tmp_small_list) + self._quick(tmp_big_list)


example = database([-1, 0, 2, -2, 3, 6, -3, 5, 1, 4])
