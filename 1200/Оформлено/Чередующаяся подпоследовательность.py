max_positive_seq = 0
max_negative_seq = float("-inf")

n_sets = int(input())

for i in range(n_sets):
    _ = int(input())
    r = 0
    seq = map(int, input().split())
    for x in seq:
        if x > 0:
            if max_negative_seq != float("-inf"):
                r += max_negative_seq
            max_negative_seq = float("-inf")
            max_positive_seq = max(max_positive_seq, x)
        else:
            if max_positive_seq != 0:
                r += max_positive_seq
            max_positive_seq = 0
            max_negative_seq = max(max_negative_seq, x)
    if max_positive_seq != 0:
        r += max_positive_seq
    else:
        r += max_negative_seq
    print(r)