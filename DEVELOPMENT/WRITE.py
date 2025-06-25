import datetime
def bill_for_customers(items_bought,customer_name,phone_number,amt_spent):
    '''
    Summary:This file generate and saves a text invoice of a customer
    if they purchase anything.
    the invoice is saved in txt file where customer details and all the
    necessary details are stored.

    Parameters:
    items_bought(list of dictionary):In this list following information is included:
        'name'(Str):name of the product
        'quantity(int)':quantity purchased
        'brand'(str):brand of the product bought
        'free'(int):number of free item if got any
        'price'(int):price per item
        'total'(int):total price after free gifts
    customer_name(str):Customer's name
    phone_number(str):Cuctomer's phone number
    amt_apent(int):Total amount customer spent on total

    Returns:
    str:fileName (str) of the invoice which is stored on disk.

    Raises:
    TypeError:If incorrect data types are passes for any parameter.
'''
    now = datetime.datetime.now()
    date = str(now.year) + "-" + str(now.month) + "-" + str(now.day) 
    fileName="Bill_for C "+customer_name+"_"+date+".txt"
    

    with open (fileName,'w')as file:
        #to print the invoice of customers
        file.write("           === WE CARE BEAUTY STORE ===\n")
        file.write("\t   == INVOICE OF PURCHASE ==\n")
        file.write("\n")
        file.write("Customer: " + customer_name + "\t\t\tDate: "+date+"\n" )
        file.write("Phone Number:"+phone_number+"\n")
        
        file.write("-"*60)
        #writing in the txt file
        for item in items_bought:
            #customers purchase 
            file.write("\n")
            file.write("\tProduct"+"\t"*4+item['name'] + "\n") 
            file.write( "\tQuantity"+"\t"*3+str(item['quantity']) + "\n" )
            file.write( "\tBrand"+"\t"*4+item['brand']+ "\n")
            file.write( "\tFree"+"\t"*4+ str(item['free']) + "\n" )
            file.write( "\t Price"+"\t"*4+"Rs. "+str(item['price']))
            file.write("\n")
        file.write("-"*60)
        file.write("\n")
        file.write("\tTotal"+"\t"*5 +str(item['total'])+"\n")
        file.write("-"*60)
        file.write("\n")
        #saving the invoice with the user's name and date
        file.write("\nInvoice saved as:"+fileName)
        file.write("\n")
        #displays how much amount is spent
        file.write("Total Amount spent RS."+ str(amt_spent) +"\n")
        file.write("ThankYou for shopping with us!\n")

    return fileName

def bill_for_vendors(restocked_items,total_cost,supplier_name,phone_number):
    ''' Summary:
            This function generates and saves a text invoice
            to restock items in the store.
            this invoice includes supplier details,list of items restocked
            with its price and quantity.
        Parameters:
            restocked_items(lists of dict): it is list of dictionary
            which contains following information:
                'name'(str):name of the product
                'brand'(str):brand of the product
                'quantity'(str):quantity bought
                'cost_price'(int):original price 
                'total'(int):total anount together
            total_cost(int):total cost of all the items
            supplier_name(str):name of the supplier]
            phone_number(str):phone number of vendor

        Returns:
            str:filename(str) of the invoice file is create and is saved in disks.
        Raises:
            TypeError:if any of the parameter is passes with incorrect type.
            
)
            
'''
    now = datetime.datetime.now()
    date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

    filename="Bill for S"+ supplier_name+"_"+date+".txt"
#opens a new file in vendor's name and date
    with open(filename,'w')as file:
        #format for the display
        file.write("       === WE CARE BEAUTY STORE ===\n")
        file.write("\t   == INVOICE OF RESTOCK ==\n")
        file.write("Supplier Name : " + supplier_name + "\t\t\tDate: " +date+"\n")
        file.write("Phone: " + phone_number + "\n")
        file.write("-"*75)
        for item in restocked_items:
            #necessary information to display  restock
            file.write("\n")
            file.write("\tProduct"+"\t"*4+item['name'] + "\n")
            file.write("\tBrand"+"\t"*5  +item['brand'] + "\n") 
            file.write("\tQty"+"\t"*5+ str(item['quantity']) + "\n" )
            file.write("\tUnit Price" +"\t"*4+"Rs. " + str(item['cost_price']))
            file.write("\n" )
        file.write("-"*75)
        file.write("\n")
        file.write("\tTotal"+"\t"*4+"Rs. " + str(item['total'])+"\n")
        file.write("-"*75)
        file.write("\n")
        #total cost spent
        file.write("Total Cost"+"Rs. " + str(item['total']))
        # writes saves the invoice as
        file.write("\nInvoice saved as:"+filename)
        file.write("\n")
        file.write("Restocking Complete.\n")

    return filename
        
        
        
    

    
