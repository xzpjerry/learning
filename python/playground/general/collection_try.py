#!/usr/bin/env python3



if __name__ == '__main__':
    print('******** namedtuple ********')
    from collections import namedtuple
    coordinated_sys = namedtuple('coordinated_sys', ['x', 'y'])
    # a_class_name = namedtuple('a_class_name', [property list])
    example = coordinated_sys(0,0)
    print('x', example.x, '\ny', example.y)
    print('******** namedtuple Done ********')


if __name__ == '__main__':
    print('******** deque ********')
    from collections import deque
    example = deque(['x','y','z'])
    print('Original', example)
    
    print('Im gonna append sth')
    example.append('a')
    print(example)

    print('Im gonna insert at the most left side')
    example.appendleft('b')
    print(example)

    print('Im gonna pop')
    example.pop()
    print(example)

    print('Im gonna pop the most left side')
    example.popleft()
    print(example)
    print('******** deque Done ********')


if __name__ == '__main__':
    print('******** defaultdict ********')
    from collections import defaultdict
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])
    print(dd['key2'])
    print('******** defaultdict done ********')

if __name__ == '__main__':
    print('******** OrderedDict ********')
    from collections import OrderedDict

    example1 = {'a':1, 'b':2, 'c':3}
    print(example1)
    example2 = OrderedDict([('a',1), ('b',2), ('c',3)])
    print(example2, '\n')

    class auto_fifo(OrderedDict):

        def __init__(self, max_size):
            super(auto_fifo, self).__init__()
            self.max_size = max_size

        def __setitem__(self, key, value):
            if key in self:
                del self[key]
                print('Deleted original key/value for', (key, value))
            if len(self) >= self.max_size:
                last_item = self.popitem(last = False)
                print('Deleted', last_item)
            print('Add', (key, value))
            super(auto_fifo, self).__setitem__(key, value)

    example3 = auto_fifo(3)
    example3['a'] = 1
    example3['b'] = 2
    example3['c'] = 3
    print(example3)
    example3['d'] = 4
    print(example3)
    example3['c'] = 5
    print(example3)
    print('******** ordereddict done ********')

if __name__ == '__main__':
    print('******** Counter ********')
    from collections import Counter

    cter = Counter()
    for ch in 'this is a fucking example!':
        cter[ch] += 1

    print(cter)
    print('******** Counter done ********')