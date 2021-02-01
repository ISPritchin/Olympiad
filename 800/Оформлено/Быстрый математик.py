a_s = input()
b_s = input()
for a, b in zip(a_s, b_s):
    if a != b:
        print("1", end="")
    else:
        print("0", end="")
