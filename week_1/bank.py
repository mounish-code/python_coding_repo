greeting = input("Greeting: ").strip().capitalize()

if "Hello" in greeting:
    print("$0")
elif "H" in greeting and "Hello" not in greeting:
    print("$20")
else:
    print("$100")