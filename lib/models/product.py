#To understand what codes mean, refer to the category.py file with similar codes.

from models.__init__ import CURSOR, CONN
from models.category import Category

class Product:
    
    # Dictionary of objects saved to the database.
    all = {}
    
    #Initialize attributes of the class
    def __init__(self, name, price, description, quantity_in_stock, sub_category, category_id, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.quantity_in_stock = quantity_in_stock
        self.sub_category = sub_category
        self.category_id = category_id

    #Ex. product = Product("iPhone", 999.99, "High performance smartphone", 9000, "Smartphones", 1) => print(repr(product)) => Outputs: <Product 1: iPhone, 999.99, High performance smartphone, 9000, Smartphones, Category ID: 1>
    def __repr__(self):
        return (
            f"<Product {self.id}: {self.name}, {self.price}, {self.description}, {self.quantity_in_stock}, {self.sub_category}, " + 
            f"Category ID: {self.category_id}>"
            )

    #The table has seven columns  
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            description TEXT,
            quantity_in_stock INTEGER,
            sub_category TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id))
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS products;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
            INSERT INTO products (name, price, description, quantity_in_stock, sub_category, category_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.price, self.description, self.quantity_in_stock, self.sub_category)) 
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self 
        
    @classmethod
    def create(cls, name, price, description, quantity_in_stock, sub_category, category_id):
        product = cls(name, price, description, quantity_in_stock, sub_category, category_id)
        product.save()
        return product
    
    def update(self):
        sql = """
            UPDATE products
            SET name = ?, price = ?, description = ?, quantity_in_stock = ?, sub_category = ?, category_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.description, self.quantity_in_stock, 
                             self.sub_category, self.category_id, self.id))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM products
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None 
        
    @classmethod
    def instance_from_db(cls, row):
        # Check the dictionary for  existing instance using the row's primary key
        product = cls.all.get(row[0])
        if product:
            # ensure attributes match row values in case local instance was modified
            product.name = row[1]
            product.price = row[2]
            product.description = row[3]
            product.quantity_in_stock = row[4]
            product.sub_category = row[5]
            product.category_id = row[6]  
        else:
            # not in dictionary, create new instance and add to dictionary
            product = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            product.id = row[0]
            cls.all[product.id] = product
        return product
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM products
        """
        rows = CURSOR.execute(sql).fetchall() 
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM products
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM products
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
   