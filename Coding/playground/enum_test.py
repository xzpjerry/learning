#!/usr/bin/env python3

from enum import Enum, unique


@unique
class weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

date = weekday(1)
print(date)