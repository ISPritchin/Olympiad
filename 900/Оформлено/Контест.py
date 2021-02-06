def get_res(b, t):
    return max(3*b / 10, b - b/250*t)


a, b, c, d = map(int, input().split())
misha = get_res(a, c)
vasya = get_res(b, d)

if vasya > misha:
    print("Vasya")
elif vasya < misha:
    print("Misha")
else:
    print("Tie")
