import sqlite3

CONN = sqlite3.connect('product_inventory.db')
CURSOR = CONN.cursor()