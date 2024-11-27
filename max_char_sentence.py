"""
Find maxium number of times a chacter appears in a senstence with its number of occurance.
"""


def find_max_char(sentence):
    """This function helps to find maxium number of times 
    a chacter appears in a senstence with its number of occurance.

    Args:
        sentence (string): Insert sentence

    Returns:
        tuple: first sorted tuple with highest occured character and its occurance count
    """
    char_dict = {}
    for char in sentence:
        if char == ' ':
            continue
        elif char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    char_frequency_sorted = sorted(
        char_dict.items(), key=lambda kv: kv[1], reverse=True)

    return char_frequency_sorted[0]


mySentence = "This is a common interview question "
print(find_max_char(mySentence))
