def convert(text):
    text = text.replace(':)', '😁')
    text = text.replace(':(', '😭')
    return text

def main():
    user_input = input('Enter text: ')
    result = convert(user_input)
    print(result)


main()