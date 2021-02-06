n, m, k = map(int, input().split())
n_row = (k-1) // (2*m) + 1
mod = (k-1) % (2*m)
n_par = mod // 2 + 1

print(n_row, n_par, end=" ")
if k % 2 == 1:
    print("L")
else:
    print("R")

