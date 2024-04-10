def display_menu(menu):
    print("Menu:")
    for item, details in menu.items():
        print(f"{item}: ${details['price']}")

def select_menu():
    print("Select a menu:")
    print("1. Regular Menu")
    print("2. Vegetarian Menu")
    choice = input("Enter your choice: ")
    if choice == '1':
        return regular_menu
    elif choice == '2':
        return vegetarian_menu
    else:
        print("Invalid choice! Using regular menu by default.")
        return regular_menu

def place_order(menu):
    order = {}
    while True:
        display_menu(menu)
        choice = input("Enter the item you'd like to order (or 'done' to finish): ").lower()
        if choice == 'done':
            break
        if choice not in menu:
            print("Invalid item! Please choose from the menu.")
            continue
        try:
            quantity = int(input(f"Enter the quantity of {choice}: "))
        except ValueError:
            print("Invalid quantity! Please enter a valid integer.")
            continue
        order[choice] = quantity
    return order

def calculate_total(order, menu):
    total = 0
    for item, quantity in order.items():
        total += menu[item]['price'] * quantity
    return total

def generate_bill(order, menu):
    print("\nBill:")
    print("Food Name\t\tPrice\t\tQuantity\tAmount")
    for item, quantity in order.items():
        price = menu[item]['price']
        amount = price * quantity
        print(f"{item}\t\t${price}\t\t{quantity}\t\t{amount}")
    total_cost = calculate_total(order, menu)
    print(f"\nTotal Cost: ${total_cost:.2f}")

def main():
    # Get customer details
    customer_name = input("Enter customer name: ")
    customer_phone = input("Enter customer phone number: ")

    # Menu selection
    menu = select_menu()

    # Place order
    order = place_order(menu)

    # Generate bill
    generate_bill(order, menu)

    # Display customer details
    print("\nCustomer Details:")
    print(f"Name: {customer_name}")
    print(f"Phone: {customer_phone}")

# Define menus
regular_menu = {
    "burger": {"price": 5.99},
    "pizza": {"price": 8.99},
    "fries": {"price": 2.49},
    "salad": {"price": 4.99}
}

vegetarian_menu = {
    "veggie burger": {"price": 6.99},
    "vegetarian pizza": {"price": 9.99},
    "fries": {"price": 2.49},
    "salad": {"price": 4.99}
}

if __name__ == "__main__":
    main()
