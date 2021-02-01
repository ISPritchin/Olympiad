n = int(input())
offers = list(map(int, input().split()))

if offers[0] < offers[1]:
    max_i = 1
    max_offer = offers[1]
    second_i = 0
    second_offer = offers[0]
else:
    max_i = 0
    max_offer = offers[0]
    second_i = 1
    second_offer = offers[1]

for i, offer in enumerate(offers):
    if i < 2:
        continue
    if offer > max_offer:
        second_i = max_i
        second_offer = max_offer
        max_i = i
        max_offer = offer
    elif offer > second_offer:
        second_offer = offer
        second_i = i

print(max_i+1, second_offer)

