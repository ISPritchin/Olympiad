s = bin(int(input()))[2:]
for i, x in enumerate(s):
    if x == '1':
        print(len(s)-i, end=' ')
