n, n_abon, c, c_abon = [int(x) for x in input().split()]
print(min([
    n*c,
    n // n_abon * c_abon + (n % n_abon) * c,
    (n // n_abon + 1) * c_abon
]))