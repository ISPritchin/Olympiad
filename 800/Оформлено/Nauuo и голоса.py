x, y, z = map(int, input().split())
if x + z < y:
    print("-")
elif y + z < x:
    print("+")
elif x == y and z == 0:
    print(0)
elif x == 0 and y == 0 or x == y == z or x + z >= y or y + z >= x:
    print("?")
