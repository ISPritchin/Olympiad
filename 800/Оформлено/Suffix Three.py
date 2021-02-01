suf_dict = {
    "po": "FILIPINO",
    "desu": "JAPANESE",
    "masu": "JAPANESE",
    "mnida": "KOREAN"
}

n_sets = int(input())
for i in range(n_sets):
    word = input()
    for suf in suf_dict:
        if word.endswith(suf):
            print(suf_dict[suf])
            break

