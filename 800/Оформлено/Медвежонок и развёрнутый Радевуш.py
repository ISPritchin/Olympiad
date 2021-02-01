n, c = map(int, input().split())

p = list(map(int, input().split()))
t = list(map(int, input().split()))


def get_res(ps, ts):
    s = 0
    t_sum = 0
    for p, t in zip(ps, ts):
        t_sum += t
        s += max(0, p - c * t_sum)
    return s


limak = get_res(p, t)
radewoosh = get_res(reversed(p), reversed(t))

if limak > radewoosh:
    print("Limak")
elif limak < radewoosh:
    print("Radewoosh")
else:
    print("Tie")
