d = {
    "purple": "Power",
    "green": "Time",
    "blue": "Space",
    "orange": "Soul",
    "red": "Reality",
    "yellow": "Mind",
}

all_colors = list(d.keys())

n = int(input())
colors = [input() for i in range(n)]

print(len(d) - len(colors))
for color in all_colors:
    if color not in colors:
        print(d[color])
