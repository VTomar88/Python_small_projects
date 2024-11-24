"""
The functions in this script find maximum and minimum numbers in a list.
"""

def max_num(list):
    """
    Finds the maximum number in the list
    input: list with numbers
    output: maximum number
    """
    # Initialize max_num with first item in the list
    max_num = list[0]
    for item in list:
        # Check if item is a number
        if type(item) == int or type(item) == float:
            # Check if max_num is still a maximum number
            if max_num < item:
                max_num = item
        # If not a number then continue to next item
        else:
            continue
    return max_num

def min_num(list):
    """
    Finds the minimum number in the list
    input: list with numbers
    output: minimum number
    """
    # Initialize max_num with first item in the list
    min_num = list[0]
    for item in list:
        # Check if item is a number
        if type(item) == int or type(item) == float:
            # Check if max_num is still a maximum number
            if min_num > item:
                min_num = item
        # If not a number then continue to next item
        else:
            continue
    return min_num

def main():
    list = [1, 2, 3, 33, -4, 0, 'a']
    print(f"Min: {min(list)}")
    print(f"Max: {max(list)}")

if __name__ == "__main__":
    main()
