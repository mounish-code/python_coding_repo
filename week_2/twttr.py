user = input("Input: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for letter in user:
    if letter not in vowels:
        print(letter, end= "")
