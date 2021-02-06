n, m, k = map(int, input().split())
prices = list(map(int, input().split()))
left = m - 1
right = m + 1
while True:
    if left >= 1:
        price = prices[left - 1]
        if price <= k and price != 0:
            print(10 * (m - left))
            break
        left -= 1
    if right <= n:
        price = prices[right - 1]
        if price <= k and price != 0:
            print(10 * (right - m))
            break
        right += 1
