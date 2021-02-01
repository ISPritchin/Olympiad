def count_gl(s):
    r = 0
    for x in s:
        if x in "auioe":
            r += 1
    return r


poem = [input() for i in range(3)]

n_gl = list(map(count_gl, poem))
if n_gl == [5, 7, 5]:
    print("YES")
else:
    print("NO")
