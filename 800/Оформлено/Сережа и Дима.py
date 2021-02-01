n = int(input())
cards = [int(x) for x in input().split()]
a = b = 0
i = 0
j = len(cards)-1
f = 0
while i <= j:
    if cards[i] < cards[j]:
        if f == 0:
            a += cards[j]
        else:
            b += cards[j]
        j -= 1
    else:
        if f == 0:
            a += cards[i]
        else:
            b += cards[i]
        i += 1
    f = (f+1) % 2
print(a, b)
