n, d = map(int, input().split())
s = input()
i = 0

r = 0
while i != len(s)-1:
    j = i + 1
    i_next = i
    have_move = False
    while j < len(s) and j < i + d + 1:
        if s[j] == '1':
            i_next = j
            have_move = True
        j += 1
    if not have_move:
        print(-1)
        break
    else:
        r += 1
        i = i_next
else:
    print(r)
