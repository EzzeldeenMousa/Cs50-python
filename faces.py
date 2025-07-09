def emojize(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

def main():
    user_input = input("input: ")
    output = emojize(user_input)
    print("output:", output)
main()
