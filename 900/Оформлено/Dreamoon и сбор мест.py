n_sets = int(input())
for _ in range(n_sets):
    n, x = map(int, input().split())
    places = set(list(map(int, input().split())))
    place = 1
    j = 0
    while j != x:
        if place not in places:
            j += 1
        place += 1
    while place in places:
        place += 1
    print(place - 1)
