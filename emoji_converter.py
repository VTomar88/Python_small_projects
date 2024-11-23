"""
Emoji converter converts short messages to emojis if present in dictionary. Else, the word
remians same.
"""
emojis = {
    ":)": "😊",
    ":(": "😔",
    ";)": "😜"
}

user = input("> ")
words = user.split(" ")
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
