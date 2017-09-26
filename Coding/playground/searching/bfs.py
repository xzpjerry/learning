from tree import Node, tree
from queue import Queue


class bfs_tree(tree):

    def bfs(self, target):
        self.visited = []
        Q = Queue()
        Q.put(self.root)

        while not Q.empty():
            current = Q.get()
            print(current.value)
            if current.value == target:
                return True
            if current.left != None:
                if current.left not in self.visited:
                    self.visited.append(current.left)
                    Q.put(current.left)
            if current.right != None:
                if current.right not in self.visited:
                    self.visited.append(current.right)
                    Q.put(current.right)
        return False

if __name__ == '__main__':
    example = bfs_tree([10, 5, 1, 2, 7, 9, 12])
    print(example)
    print(example.bfs(13))
'''
1 2 5 7 9 10 12
7
2
10
1
5
9
12
False
'''