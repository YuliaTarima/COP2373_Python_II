# YuliaTarima_Chapter2_Assignment2A

"""
This application lists 30 words and phrases
commonly found in spam messages.
It prompts the user to enters an email message and then
scans the message for each of the 30 keywords or phrases.
For each occurrence of one of these within the message,
a point to the message's "spam score" is added.
Next, it calculates the likelihood that the message is spam,
based on the number of points received.
Then, it displays the user's spam score,
the likelihood of message being a spam,
and the words/phrases which caused it to be spam.
"""

# Common spam keywords and phrases
spam_keywords = ["free", "viagra", "make money fast",
                 "limited time offer", "congratulations",
                 "urgent", "act now", "click here", "discount",
                 "cash prize", "guaranteed", "special promotion",
                 "no obligation", "unsubscribe", "double your",
                 "incredible deal", "risk-free",
                 "you've been selected",
                 "earn money from home", "save big", "100% satisfied",
                 "lowest price", "order now", "increase sales",
                 "lose weight fast", "call now", "no credit check",
                 "investment opportunity", "best offer",
                 "act immediately"]


# Calculate the spam score of the email message
# Collect the flagged keywords influencing the spam score
def calculate_spam_score(email_message):
    # Initialize spam score and flagged keywords
    spam_score = 0
    flagged_keywords = []

    # Check each keyword in the message
    for keyword in spam_keywords:
        # For each occurrence:
        if keyword in email_message:
            # increase the spam score
            spam_score += 1
            # collect the flagged spam keyword
            flagged_keywords.append(keyword)
    # Return the accumulated spam score and flagged keywords
    return spam_score, flagged_keywords


# Determine likelihood of spam based on spam score
def determine_spam_likelihood(spam_score):
    if spam_score >= 10:
        return "High"
    elif spam_score >= 5:
        return "Medium"
    else:
        return "Low"


def main():
    # Prompt user to enter email message
    # Convert message to lowercase for case-insensitive comparison
    email_message = input(
        "Enter your email message: ").lower()

    # Calculate spam score and get flagged keywords
    spam_score, flagged_keywords = calculate_spam_score(email_message)

    # Determine spam likelihood
    spam_likelihood = determine_spam_likelihood(spam_score)

    # Display spam score, spam likelihood, and flagged spam keywords
    print("Spam Score:", spam_score,
          "\nLikelihood of spam:", spam_likelihood,
          "\nWords and phrases that increased the spam score:",
          ", ".join(flagged_keywords))


if __name__ == "__main__":
    main()
