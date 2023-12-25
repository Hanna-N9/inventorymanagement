#To understand what codes mean, go to the category.py file with similar codes for more explanation.

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
        
    @property
    def name(self):
        return self._name

    @name.setter    
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        elif not isinstance(name, str):
            raise ValueError("Name must be a string.")
        else:
            raise ValueError("Name cannot be an empty string.")
                
    @property
    def price(self):
        return self._price
      
    @price.setter
    def price(self, price):
        if isinstance(price, float) and price >= 0:
            self._price = price
        elif not isinstance(price, float):
            raise ValueError("Price must be a float.")
        else:
            raise ValueError("Price cannot be negative.")
        
    @property
    def description(self):
        return self._description
 
    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        elif not isinstance(description, str):
            raise ValueError("Description must be a string.")
        else:
            raise ValueError("Description cannot be an empty string.")
  
    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, quantity_in_stock):
        if isinstance(quantity_in_stock, int) and quantity_in_stock > 0:
            self._quantity_in_stock = quantity_in_stock
        elif not isinstance(quantity_in_stock, int):
            raise ValueError("Quantity in stock must be an integer.")
        else:
            raise ValueError("Quantity in stock cannot be less than 0.")
        
    @property
    def sub_category(self):
        return self._sub_category
        
    @sub_category.setter
    def sub_category(self, sub_category):
        if isinstance(sub_category, str) and len(sub_category):
            self._sub_category = sub_category
        elif not isinstance(sub_category, str):
            raise ValueError("Sub-category must be a string.")
        else:
            raise ValueError("Sub-category cannot be an empty string.")
        
    @property
    def category_id(self):
        return self._category_id
   
    @category_id.setter
    def category_id(self, category_id):
        if isinstance(category_id, int) and category_id >= 0 and Category.find_by_id(category_id):
            self._category_id = category_id
        elif not isinstance(category_id, int):
            raise ValueError("category_id must be an integer.")
        elif category_id < 0:
            raise ValueError("category_id cannot be negative.")
        else:
            raise ValueError("category_id must reference a category in the database.")
        
    #Return a product's string   
    #Ex. product = Product("iPhone", 999.99, "High performance smartphone", 9000, "Smartphones", 1) => print(repr(product)) => Outputs: <Product 1: iPhone, 999.99, High performance smartphone, 9000, Smartphones, Category ID: 1>
    def __repr__(self):
        return (
            f"<Product {self.id}: {self.name}, {self.price}, {self.description}, {self.quantity_in_stock}, {self.sub_category}, " + 
            f"Category ID: {self.category_id}>"
        )
        
    #Create a products table in the database. This table has seven columns  
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
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    #Drop the products table from the database.
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS products;
        """
        CURSOR.execute(sql)
        CONN.commit()  
        
    #Save a product to the database.
    def save(self):
        sql = """
            INSERT INTO products (name, price, description, quantity_in_stock, sub_category, category_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.price, self.description, self.quantity_in_stock, self.sub_category, self.category_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self 
        
    #Create a new product with the given attributes and saves it to the database.
    @classmethod
    def create(cls, name, price, description, quantity_in_stock, sub_category, category_id):
        product = cls(name, price, description, quantity_in_stock, sub_category, category_id)
        product.save()
        return product
    
    #Update a product by its id
    def update(self):
        sql = """
            UPDATE products
            SET name = ?, price = ?, description = ?, quantity_in_stock = ?, sub_category = ?, category_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.description, self.quantity_in_stock, 
                             self.sub_category, self.category_id, self.id))
        CONN.commit()
     
    #Deletes a product by its id   
    def delete(self):
        sql = """
            DELETE FROM products
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None 
        
    #Create a product instance from a row of data retrieved from the database.
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
    
    #Retrieve all products from the databas
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM products
        """
        rows = CURSOR.execute(sql).fetchall() 
        return [cls.instance_from_db(row) for row in rows]
    
    #Find a product by its id
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM products
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    #Find a product by its name
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM products
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

        
   
        
    

        
    


  
    
 
    