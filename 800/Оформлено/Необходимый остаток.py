n_sets = int(input())
for i in range(n_sets):
    delim, ost, _max_k = [int(x) for x in input().split()]
    var = _max_k // delim * delim
    if var + ost <= _max_k:
        print(var + ost)
    elif var - delim + ost > 0:
        print(var - delim + ost)
