class TagCloud:
    """
    A class to manage a collection of tags and their frequencies.

    This class is case-insensitive, meaning tags like 'Python' and 'python'
    are treated as the same tag. Supports operations like adding tags,
    retrieving frequencies, setting frequencies, and iterating through tags.
    """

    def __init__(self):
        """
        Initialize an empty TagCloud instance with a private dictionary 
        to store tags and their counts.
        """
        self.__tags = {}

    def add(self, tag):
        """
        Add a tag to the cloud, incrementing its count.

        Args:
            tag (str): The tag to add.
        """
        # Convert tag to lowercase for case-insensitivity
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        """
        Get the frequency of a tag.

        Args:
            tag (str): The tag whose count to retrieve.

        Returns:
            int: The frequency of the tag (0 if the tag does not exist).
        """
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        """
        Set the frequency of a tag.

        Args:
            tag (str): The tag to set the frequency for.
            count (int): The new frequency of the tag.
        """
        self.__tags[tag.lower()] = count

    def __len__(self):
        """
        Get the number of unique tags in the cloud.

        Returns:
            int: The number of unique tags.
        """
        return len(self.__tags)

    def __iter__(self):
        """
        Iterate over the tags in the cloud.

        Returns:
            Iterator: An iterator over the tag keys.
        """
        return iter(self.__tags)

# Example Application: Word Frequency Counter
def word_frequency_counter(text):
    """
    Count the frequency of words in a given text using the TagCloud class.

    Args:
        text (str): Input text to analyze.

    Returns:
        TagCloud: A TagCloud instance containing word frequencies.
    """
    # Initialize a TagCloud instance
    tag_cloud = TagCloud()
    
    # Clean and split the text into words
    words = text.split()
    for word in words:
        # Remove punctuation and add each word to the cloud
        clean_word = ''.join(filter(str.isalnum, word))
        tag_cloud.add(clean_word)

    return tag_cloud

# Example Usage
text = "Python is great! Python is fun. python, python, PYTHON."
cloud = word_frequency_counter(text)

# Using all magic methods
print("Word Frequencies:")
for tag in cloud:
    print(f"{tag}: {cloud[tag]}")  # Iteration (__iter__) and retrieval (__getitem__)

print("\nTotal unique words:", len(cloud))  # Length (__len__)

cloud["python"] = 10  # Set item (__setitem__)
print("\nUpdated frequency for 'python':", cloud["python"])  # Get item (__getitem__)
