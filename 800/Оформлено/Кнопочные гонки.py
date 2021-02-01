s, v1, v2, t1, t2 = map(int, input().split())
time1 = t1 + v1*s + t1
time2 = t2 + v2*s + t2
if time1 < time2:
    print("First")
elif time1 > time2:
    print("Second")
else:
    print("Friendship")

