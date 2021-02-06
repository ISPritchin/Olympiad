n = int(input())
open_left_scenario = 0
open_right_scenario = 0
open_all = 0
close_all = 0
for i in range(n):
    l, r = map(int, input().split())
    if l == 0:
        open_left_scenario += 1
        close_all += 1
    else:
        open_right_scenario += 1
        open_all += 1
    if r == 0:
        open_right_scenario += 1
        close_all += 1
    else:
        open_left_scenario += 1
        open_all += 1
print(min(open_left_scenario, open_right_scenario, open_all, close_all))

