x, y, z = map(int, input().split())
a, b, c = map(int, input().split())
if x > a:
    print("NO")
else:
    a -= x
    if y > a + b:
        print("NO")
    elif y + z > a + b + c:
        print("NO")
    else:
        print("YES")
