n = int(input())
a = list(map(int, input().split()))

i = 0
while a[i] == 1:
    i += 1

j = 0
while a[len(a) - 1 - j] == 1:
    j += 1

a_scenario = i + j

i = 0
r_max = 0
r = 0
while i < n:
    if a[i] == 1:
        r += 1
    else:
        r_max = max(r, r_max)
        r = 0
    i += 1
else:
    r_max = max(r, r_max)

b_scenario = r_max

print(max(a_scenario, b_scenario))

