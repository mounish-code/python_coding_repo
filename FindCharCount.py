name = input("Enter a name: ")

letter_count = {}

for letter in name:
    if letter == " ":
        continue

    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

for letter, count in letter_count.items():
    print(letter, "comes", count, "time")
