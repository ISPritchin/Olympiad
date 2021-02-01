n, k = map(int, input().split())
n_diploma = n // (2*(k+1))
n_gr = n_diploma * k
n_without = n - n_diploma - n_gr
print(n_diploma, n_gr, n_without)