class AcyclicGraph:

    def __init__(self):
        self.v = {}
        self.root = None

    def add(self, key, value):
        if key in self.v:
            self.v[key].append(value)
        else:
            self.v[key] = [value]

        if self.root is None:
            self.root = key

    def get_path_lens(self):
        len = {}

        def max_len(name, depth):
            len[name] = depth
            if name in self.v:
                for v in self.v[name]:
                    max_len(v, depth + 1)

        max_len(self.root, 0)
        return len


g = AcyclicGraph()

n = int(input())
for i in range(n):
    name1, _, name2 = input().lower().split()
    g.add(name2, name1)

print(max(g.get_path_lens().values()) + 1)