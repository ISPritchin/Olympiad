s = input()
n = 0
left = s.find("Q")
right = s.rfind("Q")
if left == right:
    print(0)
else:
    for i in range(left, right-1):
        for j in range(i+1, right):
            for k in range(j+1, right+1):
                if s[i] + s[j] + s[k] == "QAQ":
                    n += 1
    print(n)

# можно сделать решение за O(N)
