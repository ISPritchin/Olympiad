n_sets = int(input())

for _ in range(n_sets):
    x = input()
    a = (int(x[0])-1)*10
    b = sum((i for i in range(1, len(x)+1)))
    print(a + b)
