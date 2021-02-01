n_sets = int(input())
for _ in range(n_sets):
    _ = input()
    money_arr = list(map(int, input().split()))
    money_arr.sort()
    max_profit = 0
    for i in range(len(money_arr)):
        n_customers = len(money_arr) - i
        cost = money_arr[i]
        max_profit = max(max_profit, cost*n_customers)
    print(max_profit)