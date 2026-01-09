msg = input("What do you wanna say: ").strip()
words = msg.split()
print(*words, sep="...")