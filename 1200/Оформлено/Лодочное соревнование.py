from collections import Counter

n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    ws = list(map(int, input().split()))
    sws = dict(Counter(ws))
    res = {}
    for w1 in sws:
        k1 = sws[w1]
        for w2 in sws:
            if w2 > w1:
                continue
            k2 = sws[w2]
            sum_w = w1 + w2
            if w1 == w2 and k1 >= 2:
                if sum_w not in res:
                    res[sum_w] = 0
                res[sum_w] += k1 // 2
            elif w1 != w2:
                if sum_w not in res:
                    res[sum_w] = 0
                res[sum_w] += min(k1, k2)

    m = 0
    for n_commands in res:
        if res[n_commands] > m:
            m = res[n_commands]
    print(m)
