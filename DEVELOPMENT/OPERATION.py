from READ import reading
import datetime
from WRITE import bill_for_customers, bill_for_vendors

def selling():
    '''
    Summary:
        This function handles the selling to the customers.It allows the user
        to purchase product and they can also get "buy 3 get 1 free"offer,
        updates the product,takes the necessary information fron the user and also
        displays the invoice using 'biil_for_customers' function.
        
    Parameters:
        None
        
    Returns:
        None
        
    Raises:
        ValueError:If non integer value is entered in product id or quantity.
        FileNotFoundError:If 'READ.txt' does not exist os is not accessible.
'''
    all_the_products = reading()
    items_bought = []  # This will store bought items
    amt_spent = 0
    
    while True:
        try:
            #take input of the product id
            product_id = int(input("Enter the product ID that you want to buy (0 to exit): "))

            if product_id == 0:
                break
            
            if product_id not in all_the_products:
                print("Enter a valid product id available!")
                continue
            
            product = all_the_products[product_id]
            product_name = product[0]
            brand = product[1]
            available_qty = int(product[2])
            price = int(product[3]) * 2  # Adjusted for price logic
            
            # Check if product is out of stock
            if available_qty <= 0:
                print("This product is out of stock. Please choose another product.")
                continue  
            
            while True:
                try:
                    qty_to_buy = int(input("How much would you like to buy: "))
                    #checks the quantity is vaild or available or not.   
                    if qty_to_buy <= 0:
                        print("Invalid quantity.")
                        continue
                    if qty_to_buy > available_qty:
                        print("The available quantity is:", available_qty)
                        continue
                    #for the item alredy inserted
                    found = False
                    for item in items_bought:
                        if item['id'] == product_id:
                            item['quantity'] += qty_to_buy
                            total_qty = item['quantity']
                            item['free'] = total_qty // 3
                            paid_items = total_qty + item['free']
                            item['total'] = qty_to_buy * price
                            found = True
                            break
                    #if it is not found update here
                    if not found:
                        total_qty = qty_to_buy
                        free_items = total_qty // 3
                        paid_items = total_qty + free_items
                        item_total = qty_to_buy * price

                        # Update the product info in the list
                        items_bought.append({
                            'id': product_id,
                            'name': product_name,
                            'brand': brand,
                            'quantity': qty_to_buy,
                            'free': free_items,
                            'price': price,
                            'total': item_total
                        })

                    # Updating the quantity in the inventory
                    new_qty = available_qty - paid_items
                    if new_qty < 0:
                        new_qty = 0
                    product[2] = str(new_qty)
                    
                    amt_spent += item_total
                    break
                
                except ValueError:
                    print("Please enter a valid number!")
                
            with open('READ.txt', 'w') as file:
                for pid in sorted(all_the_products.keys()):
                    product = all_the_products[pid]
                    # Write back to file in the original format
                    file.write(','.join(product) + '\n')

            while True:
                #if the user want to continue buying
                again = input("Do you want to buy more product? (yes/no): ").lower()
                if again in ('yes', 'no'):
                    break
                print("Please enter 'yes' or 'no'")
            
            if again == 'no':
                break

        except ValueError:
            print("Error: Please enter a valid number!!!")
            continue

    if not items_bought:
        print("\n No items were purchased.")
        return                
                
# Get customer details for invoice
    print("\n=== CUSTOMER DETAILS FOR INVOICE ===")
    while True:
        customer_name = input("Enter customer name: ")
        if(customer_name.isalpha()):
            break
        else:
            print("Name not valid.")
    while True:
        phone_number = input("Enter phone number: ")
        if(phone_number.isdigit()):
            break
        else:
            print("Enter a vaild phone number")

    filename=bill_for_customers(items_bought,customer_name,phone_number,amt_spent)
    print("\n")
    print("\t\t  === Invoice of purchase ===")
    print("\n")
    print("Customer: " + customer_name + "\t\t\t","Date: " + str(datetime.datetime.now()) )
    
    print("Phone: " + phone_number + "\n")
    print("-" * 65)
    for item in items_bought:
        print("\tProduct","\t"*4+item['name'] + "\n" + "\tQuantity","\t"*4+str(item['quantity']) + "\n" + "\tBrand","\t"*5+str(item['brand']) + "\n" +"\tFree","\t"*5+ str(item['free']) + "\n" +
                   "\tUnit Price","\t"*4+"Rs. "+str(item['price']))
    print("-" * 65)
    print("\tTotal","\t"*5 +str(item['total'])+"\n")
    print("-" * 65)

    print("\nInvoice saved as:", filename)
    print("Total amount: Rs.", amt_spent)
    print("Thank you for your purchase!")
    print("\n"*5)

def restocking():
    '''
    Summary:
        This function handles the restocking preocess of the WE CARE.
        It allows the user to update quantity ,cost price and calculates vat
        and generates invoice using 'bill_for_vendors()' function.
    Parameters:
        None
    Returns:
        None
    Raises:
        ValueError:It is raised if non numeric input is provided in product id,quantity or price.
        FileNotFound:If 'READ.txt' does not exist or is inaccessible.
'''
    products = reading()
    restocked_items = []
    total_cost = 0

    while True:
        try:
            product_id = int(input("\nEnter product ID to restock (0 to finish): "))
        
            if product_id == 0:
                break
            if product_id not in products:
                print("Invalid product ID! Please enter a valid ID from the list.")
                continue
            
            product = products[product_id]
            current_qty = int(product[2])
            cost_price = int(product[3])   # Gets original cost price 
        
            print("\nProduct: " + product[0])
            print("Brand: " + product[1])
            print("Current stock: " + str(current_qty))
            print("Cost price: Rs. " + str(cost_price))
        
            try:
                #Validation of the quantity is checked
                restock_qty = int(input("Enter quantity to add: "))
                if restock_qty==0:
                    break
                if restock_qty <= 0:
                    print("Quantity must be positive!")
                    continue
                #to calculate new price if the price has changed
                new_cost_price = input("Enter new cost price (current: Rs. " + str(cost_price) + "), or press Enter to keep same: ")
            
                if new_cost_price:
                    try:
                        new_cost_price = int(new_cost_price)
                        if new_cost_price <= 0:
                            print("Price must be positive! Keeping original price.")
                        else:
                            cost_price = new_cost_price
                            product[3] = str(cost_price)  
                    except ValueError:
                        print("Invalid price! Keeping original price.")
            
                # Calculate item total
                item_total = restock_qty * cost_price
                total_cost += item_total
                amt_after_vat=(total_cost*0.13)+total_cost
            
                # Add to restocked items list
                restocked_items.append({
                    'name': product[0],
                    'brand': product[1],
                    'quantity': restock_qty,
                    'cost_price': cost_price,
                    'total': total_cost
                })
            
                # Update quantity
                product[2] = str(current_qty + restock_qty)
            
                # Write changes back to file
                with open('READ.txt', 'w') as file:
                    for pid in sorted(products.keys()):
                        p = products[pid]
                        file.write(','.join(p) + '\n')
            
                print("\nSuccessfully added " + str(restock_qty) + " units of " + product[0])
                print("New stock level: " + product[2])

                while True:
                    #if they want to restock more
                    again = input("Do you want to RESTOCK more product? (yes/no): ").lower()
                    if again in ('yes', 'no'):
                        break
                    print("Please enter 'yes' or 'no'")
        
                if again == 'no':
                    break
            except ValueError:
                print("Invalid quantity! Please enter a number.")
            
        except ValueError:
            print("Invalid input! Please enter a number.")
    if not restocked_items:
        print("\n No items were RESTOCKED.")
        return
    #display format for invoice
    print("\n=== SUPLIER DETAILS FOR INVOICE ===")
    supplier_name = input("Enter Vendors name: ")
    while True:
        phone_number = input("Enter phone number: ")
        if(phone_number.isdigit()):
            break
        else:
            print("Enter a valid number.")
    #prints the invoice for supplier
    if restocked_items:
        
        filename = bill_for_vendors(restocked_items,total_cost,supplier_name,phone_number)
        print("\n")
        print("\t\t\t=== SUPPLIERS DETAILS ===")
        print("\n")
        print("Supplier Name : " + supplier_name + "\t\t\t","Date: " + str(datetime.datetime.now()) )
        print("Phone: " + phone_number + "\n")
    
        print("-" * 75)
        for item in restocked_items:
            print("\tProduct","\t"*4+item['name'] + "\n" +"\tBrand","\t"*5  +item['brand'] + "\n" +"\tQty","\t"*5+ str(item['quantity']) + "\n" +
             "\tUnit Price" ,"\t"*4+"Rs. " + str(item['cost_price']))
        print("-" * 75)
        print("\tTotal","\t"*4+"Rs. " + str(item['total']))
        print("-" * 75)
        print("\n")      
        print("TOTAL COST: Rs.", total_cost)
        #vat calculation
        print("Total Cost After VAT",(str(amt_after_vat)))
        print("\nInvoice saved as:", filename)
        print("\nRestocking complete.")
        print("\n" *15)
