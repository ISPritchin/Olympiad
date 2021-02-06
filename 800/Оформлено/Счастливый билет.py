n = int(input())
number = list(map(int, input()))
if number.count(4) + number.count(7) == len(number) and sum(number[:len(number) // 2]) == sum(number[len(number) // 2:]):
    print("YES")
else:
    print("NO")
