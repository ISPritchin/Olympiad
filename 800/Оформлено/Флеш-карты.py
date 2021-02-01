n = int(input())
file_size = int(input())
flash_size = [int(input()) for i in range(n)]

flash_size.sort(reverse=True)
i = 0
s = 0
while i < n:
    s += flash_size[i]
    i += 1
    if s >= file_size:
        break
print(i)
