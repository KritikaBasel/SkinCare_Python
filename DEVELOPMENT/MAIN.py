from OPERATION import selling,restocking
from READ import reading

def main_class():
    """
    Summary:
        this function display the main menu of the WE CARE system and also
        handels user interaction.
        there are option to display,sell to customers,restock or exit the
        program.

    Parameters:
        None

    Returns:
        None

    Raises:
        ValueError:If any non numeric values are given when number
        should be (1-4).
"""
    while True:
        print("*-*"*35)
        print("\n\t\t\t*=== -------------- WE CARE ------------------ ===*")
        print("*-*"*35)
        print("\n")
        print("\t\t\t   WELCOME TO THE 'WE CARE' SKIN CARE COMPANY")
        print("_"*105)
        print("\n")
        print("\t\t  Insert one of the following command to connect with WE CARE")
        print("\n")
        print("1. Display the available products")
        print("2. To Sell from WE CARE to customer")
        print("3. To restock products from Supplier")
        print("4. To exit from the program")
        
        user_choice = input("\nPlease choose an option (1-4): ")
        
        if user_choice == '1':#to display the file
            reading()
        elif user_choice == '2':#selling to the customers
            selling()
        elif user_choice == '3':#restoking from the vendor
            restocking()  
        elif user_choice == '4':
            #user input to make sure
            decision = input("Are you sure you want to exit? (yes/no): ").lower()
            if decision == 'yes':
                print("\n\n\nThank you for choosing WE CARE. Hope you had a great experience here!!")
                break
            elif decision == 'no':
                continue
            else:
                print("Invalid input! Please enter 'yes' or 'no'")
        else:
            print("\nInvalid choice! Please choose options 1-4")

main_class()

