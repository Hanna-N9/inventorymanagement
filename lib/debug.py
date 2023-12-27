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
        
    #For categories table
    electronic = Category.create("Electronics")
    furniture = Category.create("Furniture")
    sport = Category.create("Sport Equipment")
    home = Category.create("Home Appliances")
    kitchen = Category.create("Kitchen")
    #If any specific record from the top is deleted, the products assigned to that category is moved to this General category 
    general = Category.create("General")

    
    #For products table
    Product.create("iPhone 15 Pro", 999.99, "A powerful smartphone with great camera capabilities.", 50, "iPhone", electronic.id)
    Product.create("Samsung TV", 1000.00, "42-inch LED TV", 100, "TV", electronic.id)
    Product.create("Camera Model X", 599.99, "High-quality digital camera", 105, "Compact Cameras", electronic.id)
    Product.create("Drone XYZ", 599.99, "High-quality drone with 4K camera", 71, "Drone", electronic.id)
    Product.create("Headphones Model X", 299.99, "High-quality headphones with noise-cancelling feature", 53, "Headphones", electronic.id)
    
    Product.create("Wooden Table", 135.00, "Sturdy wooden table", 290, "Tables", furniture.id)
    Product.create("Chair", 75.00, "Comfortable office chair", 305, "Chairs", furniture.id)
    Product.create("Bench", 200.00, "Comfortable wooden bench", 50, "Benches", furniture.id)
    Product.create("Bedside Table", 150.00, "Solid Wood Bedside Table", 53, "Tables", furniture.id)
    Product.create("Bean Bag", 45.00, "Comfortable bean bag chair suitable for living room", 50, "Chairs", furniture.id)
    
    Product.create("Football Ball", 49.99, "Leather football ball", 85, "Sports Equipment", sport.id)
    Product.create("Nike Air Max Plus TN", 100.00, "Comfortable running shoes", 209, "Shoes", sport.id)
    Product.create("Basketball", 39.99, "High-quality leather basketball", 134, "Sports Equipment", sport.id)
    Product.create("Nike Air Jordan", 200.00, "High-quality basketball shoes", 202, "Shoes", sport.id)
    Product.create("Fitbit Versa", 129.99, "Smart fitness tracker with heart rate monitoring", 100, "Sports Equipment", sport.id)

    Product.create("Kettle", 29.99, "Stainless steel kettle for boiling water", 100, "Home Appliances", home.id)
    Product.create("Electric Fan", 19.99, "High-speed, quiet electric fan", 109, "Home Appliances", home.id)
    Product.create("Water Purifier", 299.99, "High-quality water purifier", 55, "Household Items", home.id)
    Product.create("Vacuum Cleaner", 299.99, "High performance vacuum cleaner", 51, "Appliance", home.id)
    Product.create("Coffee Maker", 199.99, "High-quality coffee maker with automatic brewing", 85, "Kitchen Appliances", home.id)

    Product.create("Stainless Steel Knife", 20.00, "High quality stainless steel knife", 100, "Cutlery", kitchen.id)
    Product.create("Can Opener", 19.99, "5-in-1 can opener for pulling tabs, crowns caps, unscrewing tops, and opening jar lids and cans safely, easily, and cleanly", 54, "Can Opener", kitchen.id)
    Product.create("Set of Wooden Spoons", 15.00, "Handcrafted wooden spoons", 30, "Cutlery", kitchen.id)
    Product.create("Cutting Board", 29.99, "Sturdy and durable cutting board made from high-quality wood", 102, "Kitchen Tools", kitchen.id)
    Product.create("Slow Cooker", 129.95, "A versatile slow cooker for various types of cooking", 76, "Slow Cooker", kitchen.id)



reset_database()
ipdb.set_trace()
