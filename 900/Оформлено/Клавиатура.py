keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
t = input()
s = input()
for x in s:
    i = keyboard.find(x)
    if t == "R":
        print(keyboard[i-1], end="")
    else:
        print(keyboard[i+1], end="")
