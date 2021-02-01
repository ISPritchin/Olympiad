n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    s = input()
    i_start = s.find("A")
    if i_start == -1:
        print(0)
        continue
    r = 0
    cr = 0
    for x in s[i_start+1:]:
        if x == "P":
            cr += 1
            if cr > r:
                r = cr
        else:
            cr = 0
    print(r)