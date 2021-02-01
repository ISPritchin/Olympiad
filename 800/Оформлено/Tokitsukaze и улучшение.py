health = int(input())
if health % 4 == 0:
    print(1, "A")
elif health % 4 == 1:
    print(0, "A")
elif health % 4 == 2:
    print(1, "B")
else:
    print(2, "A")
