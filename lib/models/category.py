from models.__init__ import CURSOR, CONN

class Category:
    
    # Dictionary of objects saved to the database.
    all = {}
    
    #Initialize attributes of the class
    #The id attribute with the default value of None will be assigned a value after saving the object attributes as a new table row.
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
    
    #A special method that provides a string representation for Category class. It returns a string including each attribute of the instance.
    #Ex. category = Category('Electronics', 1), print(repr(category)) ==> Outputs: <Category 1: Electronics>
    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"
    
    #A class method denoted by the @classmethod decorator. cls is used to execute the SQL command to create the categories table in database. The table has two columns, id and name.
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql) #A SQLite cursor object to execute an SQL command
        CONN.commit() #After the SQL command is executed, this syntax commits the performances/changes to save to the database permanently.
    
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
        CURSOR.execute(sql, (self.name,)) #Executes the SQL command and second argument to execute is a list or tuple containing the values to be inserted into the table. 
        CONN.commit()
        self.id = CURSOR.lastrowid #Sets the id attribute of the instance to the ID of the newly inserted row. Lastrowid property of the cursor object returns the ID of the last row that was inserted.
        type(self).all[self.id] = self #Adds the newly created instance to class's all dictionary. Uses the id of the instances as keys and the instances themselves as values. Purpose is to retrieve an instance from the database by its id easily.
     
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
        CURSOR.execute(sql, (self.name, self.id)) #Executes the SQL command, passing in a tuple (self.name, self.id) as the values for the placeholders ? in the SQL command.
        CONN.commit()
     
    #Delete a record from the categories table
    def delete(self):
        sql = """
            DELETE FROM categories
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None #Remove the deleted instance from the class's ALL dictionary and sets the id of the instance to None.

    #A class method that creates a Category instance from a row of data retrieved from the categories table in the database
    #Ensure that each Category instance corresponds to exactly one row in the categories table, and that there is only one Category instance per id 
    @classmethod
    def instance_from_db(cls, row): #A row parameter, tuple or list, contains the data for a single row from the categories table
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
            SELECT *
            FROM categories
        """
        #fetchall is to retrieve all resulting rows. Contain the data for each row from the table.
        rows = CURSOR.execute(sql).fetchall() 
        #A list comprehension to iterate over each row, and for each row, it calls the instance_from_db method to create a Category instance from the row. This results in a list of Category instances representing all records in the table.
        return [cls.instance_from_db(row) for row in rows]
   
    #A class method that retrieves a specific record from the table in the database based on its id 
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM categories
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
            SELECT *
            FROM categories
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    #Retrieve all product records associated with a particular category from the categories table in the database and returns them as a list of Product instances. 
    #Defines a SQL command to select all records from the categories table where the category_id matches the id of the current Category instance. It executes this command using CURSOR.execute(sql, (self.id,)), and fetches all resulting rows with fetchall method. These rows, lists or tuples, contain the data for each product associated with the category.
    
    # def products(self):
    #     from models.product import Product
    #     sql = """
    #         SELECT * FROM categories
    #         WHERE category_id = ?
    #     """
    #     CURSOR.execute(sql, (self.id,),)
    #     rows = CURSOR.fetchall()
    #     return [Product.instance_from_db(row) for row in rows]
    

