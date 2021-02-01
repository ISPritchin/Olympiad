n = int(input())
for i in range(n):
    word = "hate" if i % 2 == 0 else "love"
    end = "that" if i != n-1 else "it"
    print(f"I {word} {end} ", end="")
