# YuliaTarima_Chapter4_Assignment4A

"""
This application lists 30 words and phrases
commonly found in spam messages.
It prompts the user to enter an email message and then
scans the message for each of the 30 keywords or phrases.
For each occurrence of one of these within the message,
a point to the message's "spam score" is added.
Next, it calculates the likelihood that the message is spam,
based on the number of points received.
Then, it displays the user's spam score,
the likelihood of message being a spam,
and the words/phrases which caused it to be spam.
The program uses a timer to calculate how long the code runs for
and displays the elapsed time at completion.
"""

import time

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


# Function to record how long the code runs for
def make_timer():
    # holds the time at which make_timer() was called
    start_time = time.time()
    # anonymous function calculating difference between the start_time
    # and current time (when the lambda function is called)
    return lambda: time.time() - start_time


def main():
    # Prompt user to enter email message
    # Convert message to lowercase for case-insensitive comparison
    email_message = input("Enter your email message: ").lower()

    # Create timer function to measure execution time
    timer = make_timer()

    # Introduce some delay for demonstration purposes
    time.sleep(1)

    # Calculate spam score and get flagged keywords
    spam_score, flagged_keywords = calculate_spam_score(email_message)

    # Determine spam likelihood
    spam_likelihood = determine_spam_likelihood(spam_score)

    # Calculate elapsed time
    elapsed_time = timer()

    # Display spam score, likelihood, flagged keywords, elapsed time
    print("\nSpam Analysis Results:")
    print("Spam Score:", spam_score)
    print("Likelihood of spam:", spam_likelihood)
    print("Words and phrases that increased the spam score:",
          ", ".join(flagged_keywords))
    print(f"\nElapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
