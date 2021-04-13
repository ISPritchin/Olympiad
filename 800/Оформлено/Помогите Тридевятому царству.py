before, after = input().split(".")
if before[-1] != "9":
    if float(f".{after}") < 0.5:
        print(before)
    else:
        print(int(before)+1)
else:
    print("GOTO Vasilisa.")
