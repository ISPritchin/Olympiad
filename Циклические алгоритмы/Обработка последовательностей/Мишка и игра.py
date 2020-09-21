# https://codeforces.com/problemset/problem/703/A

n = int(input())

rm = rc = 0
for i in range(n):
    m, c = [int(x) for x in input().split()]
    if m > c:
        rm += 1
    elif c > m:
        rc += 1

if rm == rc:
    print("Friendship is magic!^^")
elif rm > rc:
    print("Mishka")
else:
    print("Chris")
