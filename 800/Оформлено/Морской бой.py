def rec(w, h):
    return h*2 + (w+2)*2


w1, h1, w2, h2 = map(int, input().split())
if w1 == w2:
    print(rec(w1, h1+h2))
else:
    b = rec(w1, h1) - w2
    t = rec(w2, h2-1) - w2 - 2
    print(b + t)
