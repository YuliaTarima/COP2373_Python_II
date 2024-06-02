# YuliaTarima_Chapter1_Assignment1A

"""
This application is to pre-sell a limited number of cinema tickets.
No more than total available tickets (20) can be sold.
Each buyer can buy up to 4 tickets.

User is prompted for the desired number of tickets.
After their purchase, number of remaining tickets is displayed.

Process repeats until all tickets have been sold,
after which the total number of buyers is displayed.
"""


def main():
    # Function to handle the ticket selling process
    def sell_tickets():
        # Initialize the total number of tickets available
        total_tickets = 20
        # Initialize the counter for the number of buyers
        buyers_count = 0

        # Loop until all tickets are sold
        while total_tickets > 0:

            # Display the number of remaining tickets
            print(f"\nThere are {total_tickets} tickets remaining.")

            # Prompt the user for the desired number of tickets
            tickets_requested = int(input(
                "How many tickets would you like to purchase (up to 4)? "))

            # Validate the number of tickets requested
            # Show error if buying not within range of 1-4 tickets
            if tickets_requested < 1 or tickets_requested > 4:
                print(
                    f"Invalid number of tickets: {tickets_requested}."
                    "\nYou can purchase between 1 and 4 tickets.")

            # Show error if buying more than available tickets
            elif tickets_requested > total_tickets:
                print(
                    f"Invalid number of tickets: {tickets_requested}"
                    f"Only {total_tickets} tickets remaining. "
                    "\nPlease enter a valid number.")

            else:
                # Deduct the requested tickets from the total
                total_tickets -= tickets_requested
                # Increment the buyers count
                buyers_count += 1
                # Display number of remaining tickets after purchase
                print(
                    f"You have successfully purchased "
                    f"{tickets_requested} ticket(s)."
                    f"\nTickets remaining: {total_tickets}.")

        # After all tickets are sold, display total number of buyers
        print(
            f"\nAll tickets are sold out. "
            f"\nTotal number of buyers: {buyers_count}")

    # Call the function to start the ticket selling process
    sell_tickets()


# Execute the main function
if __name__ == "__main__":
    main()
