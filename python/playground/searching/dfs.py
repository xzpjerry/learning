from tree import Node, tree


class dfs_tree(tree):

    def dfs(self, target):
        visited, stack = [], [self.root]

        while stack:
            node = stack.pop()
            print(node.value)
            if node.value == target:
                return True
            visited.append(node)
            stack.extend(filter(None, [node.right, node.left]))
        return False

if __name__ == '__main__':
    example = dfs_tree([7, 2, 10, 1, 5, 9, 12])
    print(example)
    print(example.dfs(13))

'''
1 2 5 7 9 10 12
7
2
1
5
10
9
12
False
'''