#converts the characters into asterisk
def convert(phrase):
    converted = ""
    for char in phrase:
        if char in ("AEIOUaeiou"):
            converted = converted + '*'
        else:
            converted = converted + char
    return converted

phrase = input('Enter a phrase:  ')
print(convert(phrase))
