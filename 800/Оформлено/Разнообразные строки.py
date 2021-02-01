n_sets = int(input())
for i in range(n_sets):
    s = input()
    ls = len(s)
    min_code = min([ord(c) for c in s])
    for i in range(min_code, min_code+ls):
        if chr(i) not in s:
            print("NO")
            break
    else:
        print("YES")
