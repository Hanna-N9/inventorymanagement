#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.category import Category
from models.product import Product
import ipdb

def reset_database():
    Category.drop_table()
    Category.create_table()
    Product.drop_table()
    Product.create_table()
    
    # Create seed data
    
    #For categories table
    electronic = Category.create("Electronics")
    furniture = Category.create("Furniture")
    food = Category.create("Food")
    clothing = Category.create("Clothing")
    sport = Category.create("Sport Equipment")
    book = Category.create("Books")
    kitchen = Category.create("Kitchen")
    home = Category.create("Home Appliances")
    #If any specific record from the top is deleted, the products assigned to that category is moved to this General category 
    general = Category.create("General")

    
    #For products table
    Product.create("iPhone 15 Pro", 999.99, "A powerful smartphone with great camera capabilities.", 50, "iPhone", electronic.id)

reset_database()
ipdb.set_trace()
