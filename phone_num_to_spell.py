"""
This simple script can be used to spell a phone number digits.
"""
# Define dictionary to store spells of numbers
num_conversion = {
    "0": "Zero",
    "1":"One", 
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
    }

# Initialize
phone_spell = ""

# Ask for user's phone number
phone_num = input("Phone: ")

# Convert digits to phone spell
for item in phone_num:
    phone_spell += num_conversion.get(item, "!") + " "

print(phone_spell)