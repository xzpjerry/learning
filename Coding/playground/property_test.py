#!/usr/bin/env python3

class student(object):
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,tname):
        self._name = tname

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, tgrade):
        self._grade = tgrade

    def __str__(self):
        return 'name: ' + self.name + ' ' + 'grade: ' + str(self.grade)

a = student('Tom', 77)
print(a)

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
