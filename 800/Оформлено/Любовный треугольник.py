n = int(input())
arr = list(map(lambda x: int(x)-1, input().split()))
for i, x in enumerate(arr):
    a = i
    b = arr[i]
    c = arr[b]
    ca = arr[c]
    if ca == a and a != b and b != c and c != a:
        print("YES")
        break
else:
    print("NO")
