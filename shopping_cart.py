products_list = []
prices = []
print("Welcome to the shopping Cart Program!")
coupons = ['WELCOME10', 'MARKET5']


while True:
    print("""\nPlease select one of the following:
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Coupons
    6. quit""")
    action = int(input("Please enter an action: "))
    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of the '{item}'? "))
        products_list.append(item)
        prices.append(price)
        print(f"'{item}' has been added to the cart.")
        
    elif action == 2:
        print("The contents of the shopping cart are:")
        for a, product in enumerate(products_list):
            print(f'{a + 1}. {product} - ${prices[a]:.2f}')
    elif action == 3:
        removed_items = int(input("Which item would you like to remove? ")) - 1
        prices.pop(removed_items)
        products_list.pop(removed_items)
        print("Item removed.")

    #Giving a discount to the user
    elif action == 4:
        coupon = input("Type a coupon if you have or type not if don't: ").upper()
        if coupon == coupons[0]:
            discount = sum(prices) * 0.10
            print("You received a discount of 10 percent!")
            print(f"\nThe total price of the items in the shopping cart is {(sum(prices) - discount):.2f}")

        elif coupon == coupons[1]:
            discount = sum(prices) * 0.05
            print("You received a discount of 5 percent!")
            print(f"\nThe total price of the items in the shopping cart is {(sum(prices) - discount):.2f}")

        else:
            print(f"\nThe total price of the items in the shopping cart is {sum(prices):.2f}")

    elif action == 5:
        print("""\nUse the coupon 'WELCOME10' to receive 10 percent of discount
    Use the coupon 'MARKET5' to receive 5 percent of dicount
    """)

    elif action == 6:
        print("Thank you. Goodbye.")
        break





