#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.category import Category

import ipdb

def reset_database():
    Category.drop_table()
    Category.create_table()
    
    # Create seed data
    
    electronic = Category.create("Electronics")
    furniture = Category.create("Furniture")
    food = Category.create("Food")
    clothing = Category.create("Clothing")
    sport = Category.create("Sport Equipment")
    book = Category.create("Books")
    kitchen = Category.create("Kitchen")
    home = Category.create("Home Appliances")
    
reset_database()
ipdb.set_trace()
