print("Welcome to currency converter".upper())

while True:
    try:
        rupee_amount = float(input("Enter the rupee value: "))
        currency_to_convert = input("1. USD, 2. Euro, 3. Pound, 4. Nepal Rupee, 5. Cambodia (Riel): ")

        if currency_to_convert == '1':
            usd = rupee_amount / 83
            print(rupee_amount, "Indian Rupees =", usd, "US Dollars")
            
        elif currency_to_convert == '2':
            euro = rupee_amount / 91
            print(rupee_amount, "Indian Rupees =", euro, "Euros")
           
        elif currency_to_convert == '3':
            pound = rupee_amount / 67
            print(rupee_amount, "Indian Rupees =", pound, "Pounds")
        elif currency_to_convert == '4':
            nepal_rupee = rupee_amount * 1.60
            print(rupee_amount, "Indian Rupees =", nepal_rupee, "Nepali Rupees")
        elif currency_to_convert == '5':
            riel = rupee_amount * 49.31
            print(rupee_amount, "Indian Rupees =", riel, "Riels")
        else:
            print("Invalid input. Please enter a valid option.")
            continue  # Restart the loop for a new input

        break  # Exit the loop if input is valid

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for rupee amount.")
