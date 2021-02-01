n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    s = input()
    nt = s.count("t")
    wc = [x for x in s if x != 't'] + ['t']* nt
    print("".join(wc))
