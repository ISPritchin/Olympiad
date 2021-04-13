n_sets = int(input())
for _ in range(n_sets):
    px, py = map(int, input().split())
    s = input()
    r = [0, 0, 0, 0]
    for x in s:
        if x == "U":
            r[0] += 1
        elif x == "D":
            r[1] += 1
        elif x == "L":
            r[2] += 1
        else:
            r[3] += 1

    if (py <= 0 and r[1] >= -py or py >= 0 and r[0] >= py) and \
        (px <= 0 and r[2] >= -px or px >= 0 and r[3] >= px):
        print("YES")
    else:
        print("NO")
