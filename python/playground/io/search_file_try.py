import os

class searcher(object):

    def __init__(self, target, cwd = os.getcwd()):
        self.cwd = cwd 
        self.target = target
        self.dir_path = []
        self.sum_path = []
        self.result = []
        self.find_dir(self.cwd)
        self.search_file()

    def find_dir(self, path):
        sum_path = [os.path.join(path,x) for x in os.listdir(path)]
        self.sum_path.append(sum_path)
        for dir_or_file in sum_path:
            if os.path.isdir(dir_or_file):
                self.find_dir(dir_or_file)

    def search_file(self):
        for all_dir_path in self.sum_path:
            for dir_path in all_dir_path:
                if self.target in os.path.split(dir_path)[1] and os.path.isfile(dir_path):
                    self.result.append(dir_path)

    def __str__(self):
        result ='Searching result:'
        for ele in self.result:
            result += '\n' + ele
        return result

example = searcher('py', '/users/zippo/projects/python')
print(example)
