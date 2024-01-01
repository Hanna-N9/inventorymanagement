from models.category import Category
from models.product import Product
from texttable import Texttable
from colorama import Fore, Style

def exit_program():
    print("  Thank you for checking out our interactive program! Goodbye!\n")
    exit()
    
#For category

def list_categories():
   categories = Category.get_all()
   table = Texttable()
   table.add_rows([["ID", "NAME"]] + [[category.id, category.name] for category in categories]) #Add rows to the table
   print("\n")
   print(table.draw())
   
def create_category():
   name = input("Enter the category's name: ")
   try:
       category = Category.create(name)
       print(Fore.GREEN, f"Success: {category}", Style.RESET_ALL,)
   except Exception as exc:
       print(Fore.RED, "Error creating category: ", Style.RESET_ALL, exc)
    
def delete_category():
   id_ = input("Enter the category's ID: ")
   if category := Category.find_by_id(id_):
       category.delete()
       print(Fore.GREEN, f"Category's ID {id_} is deleted.", Style.RESET_ALL)
   else:
       print(Fore.RED, f"Category's ID {id_} was not found.", Style.RESET_ALL)
   
def find_category_by_name():
 name = input("Enter the category's name: ")
 category = Category.find_by_name(name)
 if category:
     table = Texttable()
     table.add_rows([["ID", "NAME"]] + [[category.id, category.name]]) #Add rows to the table
     print("\n")
     print(table.draw())
 else:
     print(Fore.RED, f"No category found with the name: {name}.", Style.RESET_ALL)
       
def find_category_by_id():
 id_ = input("Enter the category's ID: ")
 category = Category.find_by_id(id_)
 if category:
     table = Texttable()
     table.add_rows([["ID", "NAME"]] + [[category.id, category.name]]) 
     print("\n")
     print(table.draw())
 else:
     print(Fore.RED, f"No category found with the ID: {id_}", Style.RESET_ALL)
     
def view_products_of_category():
   id_ = input("Enter the category's ID: ")
   if category := Category.find_by_id(id_):
       products = category.products()
       table = Texttable()
       table.set_cols_width([2, 10, 10, 50, 10, 10, 10]) #Set the width of the columns
       table.add_rows([["ID", "NAME", "PRICE", "DESCRIPTION", "QUANTITY IN STOCK", "SUB_CATEGORY", "CATEGORY_ID"]] + [[product.id, product.name, product.price, product.description, product.quantity_in_stock, product.sub_category, product.category_id] for product in products]) #Add rows to the table
       print("\n")
       print(table.draw())
   else:
       print(Fore.RED, f"No category found with the ID: {id_}", Style.RESET_ALL)
       
       
#For product
        
def list_products():
  products = Product.get_all()
  table = Texttable()
  table.set_cols_width([2, 10, 10, 50, 10, 10, 10]) 
  table.add_rows([["ID", "NAME", "PRICE", "DESCRIPTION", "QUANTITY IN STOCK", "SUB_CATEGORY", "CATEGORY_ID"]] + [[product.id, product.name, product.price, product.description, product.quantity_in_stock, product.sub_category, product.category_id] for product in products]) 
  print("\n")
  print(table.draw())
         
def create_product():
  name = input("Enter the product's name: ")
  price = float(input("Enter the product's price: "))
  description = input("Enter the product's description: ")
  quantity_in_stock = int(input("Enter the product's quantity in stock: "))
  sub_category = input("Enter the product's sub-category: ")
  category_id = int(input("Enter the product's category's ID: "))
  try:
      product = Product.create(name, price, description, quantity_in_stock, sub_category, category_id)
      print(Fore.GREEN, f"Success: {product}", Style.RESET_ALL)
  except Exception as exc:
      print(Fore.RED, "Error creating product: ", Style.RESET_ALL, exc)

def delete_product():
   id_ = input("Enter the product's ID: ")
   if product := Product.find_by_id(id_):
       product.delete()
       print(Fore.GREEN, f"Product's ID {id_} is deleted.", Style.RESET_ALL)
   else:
       print(Fore.RED, f"Product's ID {id_} was not found", Style.RESET_ALL)
        
def find_product_by_name():
    name = input("Enter the product's name: ")
    product = Product.find_by_name(name)
    if product:
        table = Texttable()
        table.set_cols_width([2, 10, 10, 50, 10, 10, 10]) 
        table.add_rows([["ID", "NAME", "PRICE", "DESCRIPTION", "QUANTITY IN STOCK", "SUB_CATEGORY", "CATEGORY_ID"]] + [[product.id, product.name, product.price, product.description, product.quantity_in_stock, product.sub_category, product.category_id]]) 
        print("\n")
        print(table.draw())
    else:
        print(Fore.RED, f"No product found with the name: {name}", Style.RESET_ALL)

def find_product_by_id():
  id_ = input("Enter the product's ID: ")
  product = Product.find_by_id(id_)
  if product:
      table = Texttable()
      table.set_cols_width([2, 10, 10, 50, 10, 10, 10]) 
      table.add_rows([["ID", "NAME", "PRICE", "DESCRIPTION", "QUANTITY IN STOCK", "SUB_CATEGORY", "CATEGORY_ID"]] + [[product.id, product.name, product.price, product.description, product.quantity_in_stock, product.sub_category, product.category_id]])
      print("\n")
      print(table.draw())
  else:
      print(Fore.RED, f"No product found with the ID: {id_}", Style.RESET_ALL)
      
       

#Some functions from above use Texttable to display tables, and the ones below are what they look like without using the Texttable module. 

#From category side
    
""" def list_categories():
   categories = Category.get_all()
   for category in categories:
       print(category) 

#Concise       
def find_category_by_name():
   name = input("Enter the category's name: ")
   category = Category.find_by_name(name)
   print(category) if category else print(f"Category {name} not found")

#For a beginner in Python to read this code or for a user to clearly understand what is on the output - user-friendly as it provides detailed feedback to the user. 
def find_category_by_name():
 name = input("Enter the category's name: ")
 category = Category.find_by_name(name)
 if category:
     print(f"Category: {category}")
 else:
     print(f"No category found with name: {name}") 
     
def find_category_by_id():
   id_ = input("Enter the category's id: ")
   category = Category.find_by_id(id_)
   if category:
       print(f"Category: {category}")
   else:
       print(f"No category found with id: {id_}")
       
def view_products_of_category():
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        products = category.products()
        for product in products:
            print(product)
        else:
            print(f"No category found with id: {id_}")  """
    

#From product side
       
""" def list_products():
   products = Product.get_all()
   for product in products:
       print(product)
       
def find_product_by_name():
 name = input("Enter the product's name: ")
 product = Product.find_by_name(name)
 if product:
     print(f"Product: {product}")
 else:
     print(f"No product found with name: {name}")

def find_product_by_id():
  id_ = input("Enter the product's id: ")
  product = Product.find_by_id(id_)
  if product:
      print(f'Product: {product}')
  else:
      print(f'No product found with id: {id_}') """
