_ = int(input())
boys = list(map(int, input().split()))
_ = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

n_pairs = 0
for boy in boys:
    for i in range(len(girls)):
        if abs(boy - girls[i]) <= 1:
            girls[i] = -1
            n_pairs += 1
            break
print(n_pairs)
