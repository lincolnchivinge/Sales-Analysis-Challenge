# Import pertinent python libraries
import csv
from pathlib import Path



# Establish current directory
current_dir = ("c:/Users/Lincoln/Desktop/Personal/UZ MDS/Adv Programming for Data Analytics/Sales-Analysis-Challenge/Resources")
print(current_dir)


# Set file paths for menu data and sales data
menu_csv = ('c:/Users/Lincoln/Desktop/Personal/UZ MDS/Adv Programming for Data Analytics/Sales-Analysis-Challenge/Resources/menu_data.csv')
sales_csv = ('c:/Users/Lincoln/Desktop/Personal/UZ MDS/Adv Programming for Data Analytics/Sales-Analysis-Challenge/Resources/sales_data.csv')


# Establish variables
menu = []
sales = []
report = {}
quantity = []
menu_item = []



# Read menu data
with open(menu_csv) as menu_data:
    
    csv_reader_menu = csv.reader(menu_data, delimiter = ',')
    
    menu_header = next(csv_reader_menu)
        
    # loop through data and create menu list
    for row in csv_reader_menu:
        
        menu.append(row)
    


# Read sales data
with open(sales_csv) as sales_data:
    
    csv_reader_sales = csv.reader(sales_data, delimiter = ',')
    
    sales_header = next(csv_reader_sales)
    
    # loop through data and create sales list
    for row in csv_reader_sales:
        
        sales.append(row)
    
    
# create Quantity and Menu-Item lists
for sale in sales:
    quantity.append(sale[3])
    menu_item.append(sale[4])
    
    
    
    
    
# Checkpoints    
print(menu_header)    
print(sales_header)
#print(menu[0:5])
print(sales[0:5])