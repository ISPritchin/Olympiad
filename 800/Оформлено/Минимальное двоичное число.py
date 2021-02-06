n = int(input())
s = input()
n1 = s.count("1")
n0 = n - n1
if n == 1:
    print(s)
else:
    print("1" + n0 * "0")
