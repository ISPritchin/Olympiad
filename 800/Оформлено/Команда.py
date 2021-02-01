n_tasks = int(input())
n_sol_tasks = 0
for _ in range(n_tasks):
    a = map(int, input().split())
    if sum(a) >= 2:
        n_sol_tasks += 1
print(n_sol_tasks)