import datetime
'''this READ.py file allows all the file in this program to display the
available stock of the shop and displays the imformation to the user
for buying and restocking'''
def reading():
    '''Summary:
        this function reads the data from'READ.txt', and displays
        it in a tabular format with calculated seling price
        and returns the data as a dictionary
        
    Parameters:None

    Returns:
        it returns disc_ where the key is product ID(int),
        and list containing:
        [Product Name(str),Brand(str),Available Quantity(str),Price(str),Country Of origin(str)].
    Raises:
        FileNotFoundError:if 'READ.txt'file doesnot exist.
        
        '''
#read the existing document
    print("-" * 110)
    print("ID","\t","Product Name","\t\t","Brand","\t\t","Available Quantity","\t","Price","\t\t","Country Of origin")
    print("-" * 110)
    
#To read from the txt file
    with open('READ.txt', 'r') as file:
        store = file.read()

    listen = store.split('\n')#splits the column
    file.close()
    disc_ = {}

    for i in range(len(listen)):
        disc_[i + 1] = listen[i].split(',')#splits according to ,.

    for key, value in disc_.items():
        print(key, end='\t')
        
        for i in range(len(value)):
            if i == 3:#the selling price calculation
                cost_price = int(value[i])
                selling_price = cost_price * 2
                print(selling_price, end='\t\t')
            elif i == 0:#to make the indentation correct
                print(value[i], end='\t\t')
            else:#to make the indentation correct
                print(value[i], end='\t\t')
        print()
    print('-' * 110)
    
    return disc_

