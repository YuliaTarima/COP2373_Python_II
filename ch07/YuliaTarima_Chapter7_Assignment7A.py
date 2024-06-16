# YuliaTarima_Chapter7_Assignment7A

"""
This program reads the text, then it displays the sentences
and counts the number of sentences contained within the text.

It uses a regular expression with “The Look-Ahead Feature”
to read multiple sentences and determine
the number of sentences—within complicated text.
The pattern also can read sentences with multiple spaces between them,
and sentences that begin with numbers.
"""

import re

"""
Extract sentences from the given text based on a regular expression.
Args:
    text (str): The input text from which to extract sentences.
Returns:
    List[str]: A list of sentences matching the pattern.
"""


def getSentences(text):
    # start with a capital letter or a number ([A-Z0-9])
    # followed by any content (.*?) up to
    # a period (.), exclamation mark (!), or question mark (?) ([.!?])
    # sentence must be followed
    # either by a space and another capital letter/digit (\s+[A-Z0-9])
    # or be at the end of the string ($).
    pattern = r'[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|$)'
    # match sentences that span multiple lines or start with numbers
    matches = re.findall(pattern, text,
                         flags=re.DOTALL | re.MULTILINE)
    return matches


def main():
    """
    Main function to execute the program with hard-coded text.
    It extracts sentences from the hard-coded text and displays them
    along with the count of sentences.
    """
    # Hard-coded text for demonstration
    text = """
        1nce upon a time this is a sentence starting with a number. 
                   Multiple spaces can separate sentences. 
        This is a regular sentence. This is a question? 
        This is an exclamation!
        6 sentences total.
        """

    # Get sentences from the text
    sentences = getSentences(text)

    # Display the sentences
    print("Sentences:")
    for sentence in sentences:
        print(sentence)

    # Display the count of sentences
    print(f"\nTotal number of sentences: {len(sentences)}")


if __name__ == "__main__":
    main()
