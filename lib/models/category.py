from models.__init__ import CURSOR, CONN

class Category:
    
    # Dictionary of objects saved to the database.
    all = {}
    
    #Initialize attributes of the class
    #The id attribute with the default value of None will be assigned a value after saving the object attributes as a new table row.
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
    
    #A method that provides a string representation for Category class. It returns a string including each attribute of the instance.
    #Ex. category = Category('Electronics', 1), print(repr(category)) ==> Outputs: <Category 1: Electronics>
    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"
    
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
    
    #A class method denoted by the @classmethod decorator. cls is used to execute the SQL command to create the categories table in database. The table has two columns, id and name.
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        #A SQLite cursor object to execute an SQL command
        CURSOR.execute(sql) 
        #After the SQL command is executed, this syntax commits the performances/changes to save to the database permanently.
        CONN.commit() 
    
    #Drop the categories table from the database if it exist 
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS categories;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    #Insert a new row into the categories table in database with the value of self.name and update the category instance's id with the id of the newly inserted row.
    #Question mark is placeholders for these (CURSOR.execute) values - Update debug.py to see the result of each print statement of values
    def save(self):
        sql = """
            INSERT INTO categories (name)
            VALUES (?)
        """
        #Executes the SQL command and second argument to execute is a list or tuple containing the values to be inserted into the table.
        CURSOR.execute(sql, (self.name,)) #With a trailing comma is when executing a query with a single parameter and neccessary to denote a tuple with a single element. - Purpose to avoid error
        CONN.commit()
        #Sets the id attribute of the instance to the ID of the newly inserted row. Lastrowid property of the cursor object returns the ID of the last row that was inserted.
        self.id = CURSOR.lastrowid 
        #Adds the newly created instance to class's all dictionary. Uses the id of the instances as keys and the instances themselves as values. Purpose is to retrieve an instance from the database by its id easily. 
        type(self).all[self.id] = self     
     
    #Uses an argument to create a new instance of the Category's class with a given name which then calls save method on this new instance to save it to the database. Finally, it returns the newly created instance.
    #Meaning, this will create a new Category instance with the name 'given name's value' to save it to the database and return the new instance.
    @classmethod
    def create(cls, name):
        category = cls(name)
        category.save()
        return category
    
    #Update an existing record in the categories table in the database
    def update(self):
        sql = """
            UPDATE categories
            SET name = ?
            WHERE id = ?
        """
        #Executes the SQL command, passing in a tuple (self.name, self.id) as the values for the placeholders ? in the SQL command.
        CURSOR.execute(sql, (self.name, self.id)) 
        CONN.commit()
     
    def delete(self):
        sql = """
            DELETE FROM categories
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None 
        
    #Delete a record from the categories table and reassign associated products to a different category
    def delete(self):
        #Reassign all products of a deleted specific category to a different category called 'General' by using a find_by_name method that finds a category by its name
        #If the 'General' category exists, it iterates over all products of the current category, changes their category_id to the id of the 'General' category, then saves them.
        general = Category.find_by_name('General') 
        if general:
            for product in self.products():
                # Reassign the category_id of the product to general.id
                product.category_id = general.id
                #Save the updated product
                product.save()
        else:
            print("General category doesn't exist.")
        #Delete the category by its id
        sql = """
            DELETE FROM categories
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        #Remove the deleted instance from the class's ALL dictionary and sets the id of the instance to None.
        self.id = None
        
   #Delete a record from the categories table and reassign associated products as None but this may cause issues/errors
    # def delete(self):
    #    #Set the category_id of the product to None
    #     product.category_id = None
    #     #Save the updated product
    #     product.save()
    # #Delete the category by its id
    # sql = """
    #     DELETE FROM categories
    #     WHERE id = ?
    #     """
    #     CURSOR.execute(sql, (self.id,))
    #     CONN.commit()
    #     del type(self).all[self.id]
    #     #Remove the deleted instance from the class's ALL dictionary and sets the id of the instance to None.
    # self.id = None
        
    #A class method that creates a Category instance from a row of data retrieved from the categories table in the database
    #Ensure that each Category instance corresponds to exactly one row in the categories table, and that there is only one Category instance per id 
    @classmethod
    #A row parameter, tuple or list, contains the data for a single row from the categories table
    def instance_from_db(cls, row): 
        #Checks if a Category instance with the same id, the first element of the row, already exists in the class's all dictionary.
        category = cls.all.get(row[0])
        if category:
           #If exists in dictionary, it updates the name attribute of the existing instance to match the name from the row.
            category.name = row[1]
        else:
            #If that particular instance don't exist, the method creates a new Category instance using the name from the row, assigns the id from the row to the id attribute of the new instance then adds the new instance to the all dictionary, and then returns the new instance.
            category = cls(row[1])
            category.id = row[0]
            cls.all[category.id] = category
        return category
    
    #A class method that retrieves all records from the categories table in the database and returns them as a list of Category instances
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM categories
        """
        #fetchall is to retrieve all resulting rows. Contain the data for each row from the table.
        rows = CURSOR.execute(sql).fetchall() 
        #A list comprehension to iterate over each row, and for each row, it calls the instance_from_db method to create a Category instance from the row. This results in a list of Category instances representing all records in the table.
        return [cls.instance_from_db(row) for row in rows]
   
    #A class method that retrieves a specific record from the table in the database based on its id 
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM categories
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        #It calls the instance_from_db method to create a Category instance from the row. Checks if row is not None,the provided id is found in the categories table then the condition is true, and cls.instance_from_db(row) is evaluated and returned.
        #Else, record with the provided id doesn't exists and returns None.
        return cls.instance_from_db(row) if row else None
    
    #A class method that retrieves a specific record from the table in the database based on its name
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM categories
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    #Fetch all product records in a specific category from the categories table
    #Defines a SQL command to select all records from the categories table where the category_id matches the id of the current Category instance. It executes this command using CURSOR.execute(sql, (self.id,)), and fetches all resulting rows with fetchall method. These rows, lists or tuples, contain the data for each product associated with the category.    
    def products(self):
        from models.product import Product
        sql = """
            SELECT * FROM products
            WHERE category_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [Product.instance_from_db(row) for row in rows]
   

   