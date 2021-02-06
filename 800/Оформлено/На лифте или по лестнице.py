x, y, z, t1, t2, t3 = map(int, input().split())
lift_time = abs(z-x)*t2 + t3 + t3 + abs(y-x)*t2 + t3
stairs_time = t1*abs(y-x)

if lift_time <= stairs_time:
    print("YES")
else:
    print("NO")
