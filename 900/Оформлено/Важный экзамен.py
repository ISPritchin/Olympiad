from collections import Counter

n, m = list(map(int, input().split()))
answers = []
for i in range(n):
    answers.append(input())
nb = list(map(int, input().split()))

r = 0
for i, _ in enumerate(zip(*answers)):
    r += nb[i] * max(Counter(_).values())
print(r)