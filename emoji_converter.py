"""
Emoji converter converts short messages to emojis if present in dictionary. Else, the word
remians same.
"""
def emjoi_converter(message):
    emojis = {
        ":)": "😊",
        ":(": "😔",
        ";)": "😜"
    }
    words = message.split(" ")
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

# Get the user input
user = input("> ")

print(emjoi_converter(user))
