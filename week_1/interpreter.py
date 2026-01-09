exp = input("Expression: ").strip()

x, y, z = exp.split(" ")
x = int(x)
z = int(z)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    print("provide an expression")

print(float(result))