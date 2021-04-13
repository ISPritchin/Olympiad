word = input()
if word[-1] not in "euioa" and word[-1] != "n":
    print("NO")
else:
    for i in range(1, len(word)):
        if word[i-1] == "n":
            continue
        if word[i-1] not in "euioa" and word[i] not in "euioa":
            print("NO")
            break
    else:
        print("YES")
