message = input(">")
words = message.split(' ') # splits the message variable up into multiple strings anywhere there is a space
emojis = {
    ":)": "😀",
    ":(": "☹️"
}
print(words)
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)


