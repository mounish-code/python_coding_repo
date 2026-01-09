camelCase = input("camelCase: ")
snake_case = ""

for x in camelCase:
    if x.isupper():
        snake_case += "_" + x.lower()
    else:
        snake_case += x

print(f"snake_case: {snake_case}")