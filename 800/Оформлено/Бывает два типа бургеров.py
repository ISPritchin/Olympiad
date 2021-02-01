n_sets = int(input())

for _ in range(n_sets):
    bun, beef, chicken = map(int, input().split())
    h_price, c_price = map(int, input().split())
    res = 0
    if h_price > c_price:
        n_beef = min(bun // 2, beef)
        bun -= 2*n_beef
        beef -= n_beef
        n_chicken = min(bun // 2, chicken)
        bun -= 2*n_chicken
        chicken -= n_chicken
    else:
        n_chicken = min(bun // 2, chicken)
        bun -= 2*n_chicken
        chicken -= n_chicken
        n_beef = min(bun // 2, beef)
        bun -= 2*n_beef
        beef -= n_beef
    print(n_chicken*c_price + n_beef*h_price)
