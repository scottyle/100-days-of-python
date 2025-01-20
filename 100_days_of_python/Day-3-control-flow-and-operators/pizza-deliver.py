print("Welcome to Python Pizza Deliveries!")

# Get user inputs and normalize them to uppercase
size = input("What size pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Initialize total cost
total_cost = 0

# Validate pizza size
if size in ["S", "M", "L"]:
    # Determine base price
    if size == "S":
        total_cost += 15
    elif size == "M":
        total_cost += 20
    elif size == "L":
        total_cost += 25

    # Add pepperoni cost
    if pepperoni == "Y":
        total_cost += 2 if size == "S" else 3

    # Add extra cheese cost
    if extra_cheese == "Y":
        total_cost += 1

    # Display the final bill
    print(f"Your final bill is: ${total_cost}")
else:
    print("Invalid pizza size entered. Please restart and choose S, M, or L.")
