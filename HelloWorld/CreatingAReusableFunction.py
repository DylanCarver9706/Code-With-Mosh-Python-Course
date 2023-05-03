def emoji_converter(message):
    words = message.split(' ') # splits the message variable up into multiple strings anywhere there is a space
    emojis = {
    ":)": "😀",
    ":(": "☹️"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))