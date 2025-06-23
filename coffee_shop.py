def show_menu():
    print("☕ Welcome to Python Coffee!")
    print("Here's our menu:")
    print("1. Espresso - $2.50")
    print("2. Latte    - $3.50")
    print("3. Cappuccino - $3.00")
    print("4. Quit")

def get_order(customer_name):
    menu = {
        "1": ("Espresso", 2.50),
        "2": ("Latte", 3.50),
        "3": ("Cappuccino", 3.00)
    }

    while True:
        choice = input("Please select your coffee (1-3) or 4 to quit: ")
        if choice == "4":
            print(f"Thank you for visiting!, {customer_name}!")
            break
        elif choice in menu:
            coffee, price = menu[choice]
            quantity = input(f"How many {coffee}s would you like, {customer_name}? ")
            
            if quantity.isdigit():
                quantity = int(quantity)
                total = price * quantity
                print(f"\n✔ {customer_name}, you ordered {quantity} {coffee}(s).")
                print(f"💵 Total: ${total:.2f}\n")
            else:
                print("❌ Invalid quantity. Please enter a number.\n")
        else:
            print("❌ Invalid choice. Please choose from the menu.\n")

def main():
    customer_name = input("Please enter your name: ").title()
    print(f"\nWelcome, {customer_name}!\n")
    show_menu()
    get_order(customer_name)

if __name__ == "__main__":
    main()
    
    

