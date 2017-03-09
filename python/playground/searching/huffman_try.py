import queue

class huffman_node(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right

    def __getattr__(self, attr):
        if attr == child:
            return ((self.left, self.right))

sample = [(2, '2'), (1, '4'), (1, '6'), (2, '7'), (1, '9')]


def create_tree(frequency):
    p = queue.Queue()
    for value in frequency:
        p.put(value)
    while p.qsize() > 1:
        l, r = p.get(), p.get()
        print(l[0], r[0])
        node = huffman_node(l, r)
        p.put((l[0] + r[0], node))
    return p.get()

node = (create_tree(sorted(sample)))
print(node)


def walk_tree(node, prefix='', code={}):
    if isinstance(node[1].left[1], huffman_node):
        walk_tree(node[1].left, prefix + '0', code)
    else:
        code[node[1].left[1]] = prefix + '0'

    if isinstance(node[1].right[1], huffman_node):
        walk_tree(node[1].right, prefix + '1', code)
    else:
        code[node[1].right[1]] = prefix + '1'

    return (code)

code = walk_tree(node)
for i in sorted(sample, reverse=True):
    print('%s  %d  %s' % (i[1], i[0], code[i[1]]))
