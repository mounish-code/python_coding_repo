def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return(text)

def main():
    msg = input("")
    print(convert(msg))
main()