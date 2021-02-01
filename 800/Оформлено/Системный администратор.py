def print_server_info(server, n):
    if n * 5 <= server:
        print("LIVE")
    else:
        print("DEAD")


server_a = server_b = 0
na = nb = 0
n = int(input())

for i in range(n):
    server, good, _ = map(int, input().split())
    if server == 1:
        server_a += good
        na += 1
    else:
        server_b += good
        nb += 1

print_server_info(server_a, na)
print_server_info(server_b, nb)
