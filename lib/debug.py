#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.category import Category

import ipdb

def reset_database():
    Category.drop_table()
    Category.create_table()
    
    # Create seed data
    tv = Category.create("Electronics", "TV")
    print(tv) 
    
    table = Category.create("Furniture", "Tables")
    print(table)  
    
    fruit = Category.create("Food", "Fruits")
    print(fruit) 
    
    f = Category.create("Clothing", "Women")
    print(f)  
    
    football = Category.create("Sports", "Football")
    print(football)
    
    kitchenware = Category.create("Home Decor", "Kitchenware")
    print(kitchenware)
    
    novels = Category.create("Books", "Novels")
    print(novels)
    
    textbooks = Category.create("Books", "Textbooks")
    print(textbooks)
    
    shoe = Category.create("Sport Equipment", "Running Shoe")
    print(shoe)
    
    system = Category.create("Software", "Operating Systems")
    print(system)
    
    cookware = Category.create("Kitchen", "Cookware")
    print(cookware)
    
    vegetable = Category.create("Food", "Vegetable")
    print(vegetable)
    
    vegetable = Category.create("Home Appliances", "Refrigerators")
    print(vegetable)

reset_database()
ipdb.set_trace()
