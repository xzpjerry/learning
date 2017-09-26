# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str([self.start, self.end])

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        current_start = None
        current_end = None
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if current_start!= None and current_end!= None:

                if interval.start <= current_end:
                    current_end = max(current_end, interval.end)
                    current_start = min(current_start, interval.start)
                else:
                    result.append(Interval(current_start, current_end))
                    current_start = interval.start
                    current_end = interval.end

            else:
                current_start = interval.start
                current_end = interval.end

        if current_start != None and current_end != None:
            result.append(Interval(current_start, current_end))

        return result

for thing in Solution().merge([Interval(1,4), Interval(0,4)]):
    print(thing)
