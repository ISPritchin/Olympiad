last_letter = 'a'
word = input()

r = 0
for letter in word:
    az_direction = abs(ord(letter) - ord(last_letter))
    za_direction = 26 - az_direction
    r += min(za_direction, az_direction)
    last_letter = letter
print(r)
