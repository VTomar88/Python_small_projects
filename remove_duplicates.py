"""
The aim of this script is to provide function to remove duplicates.
"""

def remove_duplicates(list):
    # Create an emty list
    uniques = []

    for item in list:
        # Check for duplicates and skip them
        if item not in uniques:
            uniques.append(item)

    return uniques

def main():
    list = [1,1,2,3,4,4,5,7,7, 9]
    print(remove_duplicates(list))

if __name__ == "__main__":
    main()
