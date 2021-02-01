n, k = map(int, input().split())
scores = list(map(int, input().split()))
n_students = 0
for i, score in enumerate(scores, 1):
    if score > 0 and score >= scores[k-1]:
        n_students += 1
    else:
        break
print(n_students)