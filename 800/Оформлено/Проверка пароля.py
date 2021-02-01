s = input()
len_flag = upper_flag = lower_flag = digit_flag = False
len_flag = len(s) >= 5

i = 0
while (upper_flag == False or lower_flag == False or digit_flag == False) and i < len(s):
    if 'a' <= s[i] <= 'z':
        lower_flag = True
    elif 'A' <= s[i] <= 'Z':
        upper_flag = True
    elif '0' <= s[i] <= '9':
        digit_flag = True
    i += 1

if len_flag and upper_flag and lower_flag and digit_flag:
    print("Correct")
else:
    print("Too weak")