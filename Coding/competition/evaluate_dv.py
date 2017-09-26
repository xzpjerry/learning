class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        Given a / b = 2.0, b / c = 3.0. 
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
        return [6.0, 0.5, -1.0, 1.0, -1.0 ].

        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        class graph(object):

            def __init__(self, equations, values):

                self.nodes = []
                self.edges = {}
                counter = 0
                for equation in equations:

                    if equation[0] not in self.nodes:
                        self.nodes.append(equation[0])
                        self.edges[equation[0]] = [
                            (equation[1], values[counter])]
                    else:
                        self.edges[equation[0]].append(
                            (equation[1], values[counter]))
                    if equation[1] not in self.nodes:
                        self.nodes.append(equation[1])
                        self.edges[equation[1]] = [
                            (equation[0], 1 / values[counter])]
                    else:
                        self.edges[equation[1]].append(
                            (equation[0], 1 / values[counter]))
                    counter += 1

                print(self.nodes, self.edges)

            def get_answer(self, querie):
                start = querie[0]
                stack = [start]
                current = None
                suffix = []
                while stack:
                    current = stack.pop()
                    if current == querie[1]:
                        break
                    for connected in self.edges[current]:
                        stack.append(connected[0])
                        suffix.append(connected[1])

        a = graph(equations, values)


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
a = Solution()
a.calcEquation(equations, values, queries)
