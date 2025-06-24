# Import necessary libraries
import sqlite3
import os 
import customtkinter as ctk
import tkinter.ttk as ttk
from CTkMessagebox import CTkMessagebox

# Set the appearance mode and color theme for the application
ctk.set_appearance_mode("dark")                                                                                         # Set the appearance mode to dark
ctk.set_default_color_theme("dark-blue")                                                                                # Set the default color theme to dark blue

# Style any colors to the application
PRIMARY_COLOR = "#7b2222"                                                                                             # Define a primary color for the application
SECONDARY_COLOR = "#f5f6fa"                                                                                           # Define a secondary color for the application
TEXT_COLOR = "#222"                                                                                                     # Define a text color for the application
BUTTON_COLOR = "#7b2222"                                                                                              # Define a button color for the application
BUTTON_HOVER = "#a83232"                                                                                              # Define a button hover color for the application
BUTTON_TEXT = "#fff"                                                                                                    # Define a button text color for the application

# The function to connect to database
def create_connection():
    db_path = os.path.join(os.path.dirname(__file__), "database.db")            # Define the path to the SQLite database file
    conn = sqlite3.connect(db_path)                                                                               # Connect to the SQLite database (or create it if it doesn't exist)
    return conn                                                                                                         # Return the connection object

# The function to create a table in the database
def create_table(conn):
    try:
        cursor = conn.cursor()                                                                                          # Create a cursor object to execute SQL commands
        # Create a table named 'products' if it doesn't exist
        cursor.execute("""CREATE TABLE IF NOT EXISTS products (
            Name TEXT NOT NULL,
            Quantity INTEGER NOT NULL,
            Value REAL NOT NULL,
            Id INTEGER PRIMARY KEY AUTOINCREMENT
        )""")
        conn.commit()                                                                                                   # Commit the changes to the database 
    except sqlite3.Error as e:                                                                                          # Handle any SQLite errors
        print(f"Database error: {e}")                                                                                   # Show an error message if there is an issue creating the table

#The function to connect to the database
def insert_product(conn, name, quantity, value):
    try:
        cursor = conn.cursor()                                                                                          # Create a cursor object to execute SQL commands
        cursor.execute("INSERT INTO products (Name, Quantity, Value) VALUES (?, ?, ?)", (name, quantity, value))        # Insert the product into the database
        conn.commit()                                                                                                   # Commit the changes to the database
        CTkMessagebox(title="Success", message=f"Product {name} added successfully", icon="check")                      # Print a success message
    except sqlite3.Error as e:                                                                                          # Handle any SQLite errors
        CTkMessagebox(title="Error", message=f"Error: {e}", icon="cancel")                                              # Print the error message

# The function to show the main menu
class AddProductPage(ctk.CTkFrame):                                                                                     # Create a class for the AddProductPage, which inherits from ctk.CTkFrame
    def __init__(self, master, conn, show_main_menu):                                                                   # Initialize the AddProductPage class with master widget, database connection, and a function to show the main menu
        super().__init__(master, fg_color=SECONDARY_COLOR)                                                              # Call the parent class constructor
        self.conn = conn                                                                                                # Store the database connection
        self.show_main_menu = show_main_menu                                                                            # Store the function to show the main menu
        ctk.CTkLabel(self, text="Add Product", font=("Arial", 18), text_color=PRIMARY_COLOR).pack(pady=10)              # Create a label for the AddProductPage
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Product Name")                                           # Create an entry widget for the product name
        self.name_entry.pack(pady=5)
        self.qty_entry = ctk.CTkEntry(self, placeholder_text="Quantity")                                                # Create an entry widget for the product quantity
        self.qty_entry.pack(pady=5)
        self.value_entry = ctk.CTkEntry(self, placeholder_text="Unit Value")                                            # Create an entry widget for the product value
        self.value_entry.pack(pady=5)
        ctk.CTkButton(self, text="Add", command=self.add_product,                                                       # Create a button to add the product, which calls the add_product method when clicked
                      fg_color=BUTTON_COLOR,
                      hover_color=BUTTON_HOVER,
                      text_color=BUTTON_TEXT,
                      font=("Arial", 14, "bold"),
                      width=180, height=36,
                      corner_radius=8
                      ).pack(pady=12)
        ctk.CTkButton(self, text="Back", command=self.show_main_menu,                                                   # Create a button to go back to the main menu, which calls the show_main_menu function when clicked
                      fg_color="#aaa", hover_color="#888",
                      text_color="#fff", font=("Arial", 12, "bold"),
                      width=120, height=32, corner_radius=8).pack(pady=5)

    def add_product(self):                                                                                              # Define the method to add a product
        name = self.name_entry.get().strip()                                                                            # Get the product name from the entry widget
        qty = self.qty_entry.get().strip()                                                                              # Get the product quantity from the entry widget
        value = self.value_entry.get().strip()                                                                          # Get the product value from the entry widget
        
        if not name:
            CTkMessagebox(title="Error", message="Please enter a product name.", icon="cancel")                         # Show an error message if the product name is empty
            return                                                                                                      # Return from the method to prevent further execution
        try:                                                                                                            # Try to convert the input values to the appropriate types
            quantity = int(qty)                                                                                         # Get the product quantity from the entry widget and convert it to an integer
            value = float(value)                                                                                        # Get the product value from the entry widget and convert it to a float
            if quantity < 0 or value < 0:                                                                               # Check if the quantity or value is negative
                raise ValueError
        except ValueError:                                                                                              # If there is a ValueError (e.g., if the input cannot be converted to an integer or float)
            CTkMessagebox(title="Error", message="Quantity and value must be positive numbers.", icon="cancel")         # Show an error message
            return                                                                                                      # Return from the method to prevent further execution
        
        insert_product(self.conn, name, quantity, value)                                                                # Call the insert_product function to insert the product into the database
        self.name_entry.delete(0, 'end')                                                                                # Clear the product name entry widget
        self.qty_entry.delete(0, 'end')                                                                                 # Clear the product quantity entry widget
        self.value_entry.delete(0, 'end')                                                                               # Clear the product value entry widget                                                                                  # Clear the product ID entry widget

# The function to actually remove a product in the data base
def remove_product_data(conn, id):                                                                                      # Define the function to remove a product from the database
    cursor = conn.cursor()                                                                                              # Create a cursor object to execute SQL commands
    cursor.execute("DELETE FROM products WHERE Id = ?", (id,))                                                          # Delete the product with the specified ID from the database
    conn.commit()                                                                                                       # Commit the changes to the database
    if cursor.rowcount > 0:                                                                                             # Check if any rows were affected
        CTkMessagebox(title="Success", message=f"Product with ID {id} removed successfully.", icon="check")             # Show a success message if the product was removed
    else:
        CTkMessagebox(title="Error", message=f"No product found with ID {id}.", icon="cancel")                          # Show an error message if no product was found with the specified ID

# The function to remove a product from the database
class RemoveProductPage(ctk.CTkFrame):                                                                                  # Create a class for the RemoveProductPage, which inherits from ctk.CTkFrame
    def __init__(self, master, conn, show_main_menu):                                                                   # Initialize the RemoveProductPage class with master widget, database connection, and a function to show the main menu
        super().__init__(master, fg_color=SECONDARY_COLOR)                                                                                        # Call the parent class constructor
        self.conn = conn                                                                                                # Store the database connection
        self.show_main_menu = show_main_menu                                                                            # Store the function to show the main menu

        ctk.CTkLabel(self, text="Remove Product",                                                                       # Create a label for the RemoveProductPage
                     font=("Arial", 20, "bold"),
                     text_color=PRIMARY_COLOR).pack(pady=20)
        self.id_entry = ctk.CTkEntry(self, placeholder_text="Product ID", width=220)                                    # Create an entry widget for the product ID
        self.id_entry.pack(pady=8)                                                                                      # Pack the entry widget into the frame
        ctk.CTkButton(self, text="Remove", command=self.remove_product,                                                 # Create a button to remove the product, which calls the remove_product method when clicked
                      fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
                      text_color=BUTTON_TEXT, font=("Arial", 14, "bold"),
                      width=180, height=36, corner_radius=8).pack(pady=12)
        ctk.CTkButton(self, text="Back", command=self.show_main_menu,                                                   # Create a button to go back to the main menu, which calls the show_main_menu function when clicked
                      fg_color="#aaa", hover_color="#888",
                      text_color="#fff", font=("Arial", 12, "bold"),
                      width=120, height=32, corner_radius=8).pack(pady=4)

    def remove_product(self):                                                                                           # Define the method to remove a product
        try:
            product_id = int(self.id_entry.get())                                                                               # Get the product ID from the entry widget and convert it to an integer
        except ValueError:                                                                                              # If there is a ValueError (e.g., if the input cannot be converted to an integer)
            CTkMessagebox(title="Error", message="Please enter a valid ID.", icon="cancel")                             # Show an error message
            return                                                                                                      # Return from the method to prevent further execution
        remove_product_data(self.conn, product_id)                                                                              # Call the remove_product_data function to remove the product from the database
        self.id_entry.delete(0, 'end')                                                                                  # Clear the product ID entry widget

# The function to edit a product in the database
class EditProductPage(ctk.CTkFrame):                                                                                    # Create a class for the EditProductPage, which inherits from ctk.CTkFrame
    def __init__(self, master, conn, show_main_menu):                                                                   # Initialize the
        super().__init__(master, fg_color=SECONDARY_COLOR)                                                              # Call the parent class constructor
        self.conn = conn                                                                                                # Store the database connection
        self.show_main_menu = show_main_menu                                                                            # Store the function to show the main menu

        ctk.CTkLabel(self, text="Edit Product", font=("Arial", 20, "bold"),                                             # Create a label for the EditProductPage
                     text_color=PRIMARY_COLOR).pack(pady=20)
        
        # Step 1: ask for ID
        self.id_entry = ctk.CTkEntry(self, placeholder_text="Enter Product ID")                                         # Create an entry widget for the product ID
        self.id_entry.pack(pady=5)                                                                                      # Pack the entry widget into the
        ctk.CTkButton(self, text="Edit", command=self.ask_field,                                                        # Create a button to edit the product, which calls the edit_product method when clicked
                      fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
                      text_color=BUTTON_TEXT, font=("Arial", 14, "bold"),
                      width=180, height=36, corner_radius=8).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=self.show_main_menu,                                                   # Create a button to go back to the main menu, which calls the show_main_menu function when clicked
                      fg_color="#aaa", hover_color="#888",
                      text_color="#fff", font=("Arial", 12, "bold"),
                      width=120, height=32, corner_radius=8).pack(pady=5)

        # Step 2: Ask which option the user wants to change (hidden by default)
        self.field_frame = ctk.CTkFrame(self, fg_color=SECONDARY_COLOR)                                                 # Create a frame to hold the options for editing
        self.field_var = ctk.StringVar(value="name")                                                                    # Create a StringVar to hold the selected option
        ctk.CTkLabel(self.field_frame, text="Select field do you want to edit:",                                        # Create a label for the options
                     font=("Arial", 14), text_color=PRIMARY_COLOR).pack(pady=5)
        ctk.CTkRadioButton(self.field_frame, text="Name", variable=self.field_var, value="name", text_color="#333").pack(anchor="w")         # Create a radio button for editing the name
        ctk.CTkRadioButton(self.field_frame, text="Quantity", variable=self.field_var, value="quantity", text_color="#333").pack(anchor="w") # Create a radio button for editing the quantity
        ctk.CTkRadioButton(self.field_frame, text="Value", variable=self.field_var, value="value", text_color="#333").pack(anchor="w")       # Create a radio button for editing the value
        ctk.CTkButton(self.field_frame, text="Next", command=self.show_edit_field,
                      fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
                      text_color=BUTTON_TEXT, font=("Arial", 12, "bold"),
                      width=120, height=32, corner_radius=8).pack(pady=8)                                               # Create a button to proceed to the next step, which calls the show_edit_field method when clicked

        # Step 3: Field edit widgets (hidden by default)
        self.edit_frame = ctk.CTkFrame(self, fg_color=SECONDARY_COLOR)                                                  # Create a frame to hold the widgets for editing the selected field
        self.edit_entry = ctk.CTkEntry(self.edit_frame, placeholder_text="Enter new value", width=220)                  # Create an entry widget for entering the new value
        self.edit_entry.pack(pady=8)                                                                                    # Pack the entry widget into the edit frame
        ctk.CTkButton(self.edit_frame, text="Save", command=self.save_edit,                                             # Create a button to save the changes, which calls the save_edit method when clicked
                      fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
                      text_color=BUTTON_TEXT, font=("Arial", 12, "bold"),
                      width=120, height=32, corner_radius=8).pack(pady=8)
        ctk.CTkButton(self.edit_frame, text="Back", command=self.back_to_menu,                                          # Create a button to go back to the main menu, which calls the show_main_menu function when clicked
                      fg_color="#aaa", hover_color="#888",
                      text_color="#fff", font=("Arial", 12, "bold"),
                      width=120, height=32, corner_radius=8).pack(pady=4)
    
    def ask_field(self):
        self.product_id = self.id_entry.get()                                                                           # Get the product ID from the entry widget
        if not self.product_id.isdigit():                                                                               # Check if the product ID is a digit
            CTkMessagebox(title="Error", message="Please enter a valid ID.", icon="cancel")                             # Show an error message if the product ID is not valid
            return                                                                                                      # Return from the method to prevent further execution
        #Check if product exists in the database
        cursor = self.conn.cursor()                                                                                     # Create a cursor object to execute SQL commands
        cursor.execute("SELECT * FROM products WHERE Id = ?", (self.product_id,))                                       # Check if the product with the specified ID exists in the database
        if cursor.fetchone() is None:                                                                                   # If the product does not exist
            CTkMessagebox(title="Error", message=f"No product found with ID {self.product_id}.", icon="cancel")         # Show an error message
            return                                                                                                      # Return from the method to prevent further execution
        self.id_entry.configure(state="disabled")                                                                       # Disable the ID entry widget to prevent further changes
        self.field_frame.pack(pady=10)                                                                                  # Show the field selection frame by

    def show_edit_field(self):
        self.field_frame.pack_forget()                                                                                  # Hide the field selection frame
        field = self.field_var.get()                                                                                    # Get the selected field from the StringVar
        if field == "name":                                                                                             # If the selected field is name
            self.edit_entry.configure(placeholder_text="Enter new name")                                                # Set the placeholder text for the entry widget to "Enter new name"
        elif field == "quantity":                                                                                       # If the selected field is quantity
            self.edit_entry.configure(placeholder_text="Enter new quantity")                                            # Set the placeholder text
        elif field == "value":                                                                                          # If the selected field is value
            self.edit_entry.configure(placeholder_text="Enter new value")                                               # Set the placeholder text
        self.edit_frame.pack(pady=10)                                                                                   # Show the edit frame by packing it into the main window

    def save_edit(self):
        field = self.field_var.get()                                                                                    # Get the selected field from the StringVar
        value = self.edit_entry.get()                                                                                   # Get the new value from the entry widget
        cursor = self.conn.cursor()                                                                                     # Create a cursor object to execute SQL commands
        try:
            if field == "name":                                                                                         # If the selected field is name
                cursor.execute("UPDATE products SET Name = ? WHERE Id = ?", (value, int(self.product_id)))              # Update the product name in the database
            elif field == "quantity":                                                                                   # If the selected field is quantity
                cursor.execute("UPDATE products SET Quantity = ? WHERE Id = ?", (int(value), int(self.product_id)))
            elif field == "value":                                                                                      # If the selected field is value
                cursor.execute("UPDATE products SET Value = ? WHERE Id = ?", (float(value), int(self.product_id)))
            self.conn.commit()                                                                                          # Commit the changes to the database
            if cursor.rowcount > 0:                                                                                     # Check if any rows were affected
                CTkMessagebox(title="Success", message=f"Product with ID {self.product_id} updated successfully.", icon="check")  # Show a success message if the product was updated
            else:
                CTkMessagebox(title="Error", message=f"No product found with ID {self.product_id}.", icon="cancel")     # Show an error message if no product was found with the specified ID
        except ValueError:                                                                                              # If there is a ValueError (e.g., if the input cannot be converted to an integer or float)
            CTkMessagebox(title="Error", message="Please enter a valid number for quantity or value.", icon="cancel")
        except sqlite3.Error as e:                                                                                      # Handle any SQLite errors
            CTkMessagebox(title="Error", message=f"Error: {e}", icon="cancel")                                          # Show an error message with the SQLite error
        self.reset_fields()                                                                                             # Reset the fields after saving the changes

    def back_to_menu(self):
        self.reset_fields()                                                                                             # Reset the fields before going back to the main menu
        self.show_main_menu()                                                                                           # Call the show_main_menu function to go back to the main menu

    def reset_fields(self):
        self.id_entry.configure(state="normal") # Reset the ID entry widget to allow further changes
        self.id_entry.delete(0, 'end')                                                                                  # Clear the product ID entry widget
        self.field_frame.pack_forget()                                                                                  # Hide the field selection frame
        self.edit_frame.pack_forget()                                                                                   # Hide the edit frame
        self.edit_entry.delete(0, 'end')                                                                                # Clear the entry widget for editing the selected field

# The function to list all products registered in database
class ListProductsPage(ctk.CTkFrame):                                                                                   # Create a class for the ListProductsPage, which inherits from ctk.CTkFrame
    def __init__(self, master, conn, show_main_menu):                                                                   # Initialize the ListProductsPage class with master widget, database connection, and a function to show the main menu
        super().__init__(master, fg_color=SECONDARY_COLOR)                                                              # Call the parent class constructor
        self.conn = conn                                                                                                # Store the database connection
        self.show_main_menu = show_main_menu                                                                            # Store the function to show the main menu
        self.items_per_page = 10
        self.current_page = 1                                                                                           # Initialize the current page to 1
        self.total_products = self.get_total_products()                                                                 # Get the total number of products in
        
        ctk.CTkLabel(self, text="List of Products", font=("Arial", 20, "bold"),
                     text_color=PRIMARY_COLOR).pack(pady=20)                                                            # Create a label for the ListProductsPage
        self.filter_var = ctk.StringVar(value="ALL")                                                                    # Create a StringVar to hold the filter option (not used in this version)
        self.filter_box = ctk.CTkComboBox(self, values=["All", "By Name", "By Quantity", "By Value"],                   # Create a combo box for filtering options
                                           variable=self.filter_var, width=200, height=32,
                                           fg_color=SECONDARY_COLOR, text_color=TEXT_COLOR,)
        self.filter_box.pack(pady=8)                                                                                    # Pack the combo box into the frame
        self.filter_box.set("All")                                                                                      # Set the default value of the combo box
        filters = ["All", "By Name", "By Quantity", "By Value"]                                                         # Define the filter options for the combo box
        self.filter_box.configure(values=filters)                                                                       # Configure the combo box with the filter options
        columns = ["ID", "Name", "Quantity", "Value"]                                                                   # Define the column names for the product list
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)                                     # Create a Treeview widget to display the list of products
        self.tree.pack(pady=8)                                                                                          # Pack the Treeview widget into the
        self.tree.heading("ID", text="ID")                                                                              # Set the heading for the ID column
        self.tree.heading("Name", text="Name")                                                                          # Set the heading for the Name column
        self.tree.heading("Quantity", text="Quantity")                                                                  # Set the heading for the Quantity column
        self.tree.heading("Value", text="Value")                                                                        # Set the heading for the Value column
        self.tree.column("ID", width=50, anchor="center")                                                               # Set the width and alignment for the ID column
        self.tree.column("Name", width=140, anchor="center")                                                            # Set the width and alignment for the Name column
        self.tree.column("Quantity", width=80, anchor="center")                                                         # Set the width and alignment for the Quantity column
        self.tree.column("Value", width=80, anchor="center")                                                            # Set the width and alignment for the Value column
        self.tree.pack(pady=8, fill="x", padx=10)                                                                       # Pack the Treeview widget into the frame, filling the x direction and adding padding

        ctk.CTkButton(self, text="Apply filter", command=self.list_products,
                      fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
                      text_color=BUTTON_TEXT, font=("Arial", 14, "bold"),
                      width=180, height=36, corner_radius=8).pack(pady=10)                                              # Create a button to refresh the list, which calls the list_products again when clicked
        ctk.CTkButton(self, text="Back", command=self.show_main_menu,
                      fg_color="#aaa", hover_color="#888",
                      text_color="#fff", font=("Arial", 12, "bold"),
                      width=120, height=32, corner_radius=8).pack(pady=4)                                               # Create a button to go back to the main menu, which calls the show_main_menu function when clicked
        self.pagination_frame = ctk.CTkFrame(self, fg_color=SECONDARY_COLOR)                                            # Create a frame for pagination
        self.pagination_frame.pack(pady=10)                                                                             # Pack the pagination frame into the List
        
        self.list_products()                                                                                            # Call the list_products method to populate the textbox with the current list of products

    def get_total_products(self):
        cursor = self.conn.cursor()                                                                                     # Create a cursor object to execute SQL commands
        cursor.execute("SELECT COUNT(*) FROM products")                                                                 # Execute a SQL command to count the total number of products in the database
        return cursor.fetchone()[0]                                                                                    # Fetch the result and get the count of products

    def update_pagination(self):
        for widget in self.pagination_frame.winfo_children():                                                           # Iterate through each widget in the pagination frame
            widget.destroy()                                                                                            # Destroy the widget to clear the pagination frame
            
        for i in range(1, self.total_page + 1):
            btn = ctk.CTkButton(self.pagination_frame, text=str(i), width=32, 
                                height=32, fg_color=BUTTON_COLOR if i != self.current_page else BUTTON_HOVER,
                                hover_color=BUTTON_HOVER, text_color=BUTTON_TEXT, 
                                command=lambda page=i: self.go_to_page(page))                                           # Create a button for each page
            btn.pack(side="left", padx=2, pady=2)                                                                       # Pack the button into the pagination frame
    
    def go_to_page(self, page):                                                                                         # Define a method to switch to a different page
        self.current_page = page
        self.list_products()                                                                                            # Call the list_products method to populate the Treeview with the current list of products
    
    def list_products(self):                                                                                            # Define the method to list all products
        try:
            # Limpa a tabela antes de inserir novos dados
            for row in self.tree.get_children():                                                                        # Iterate through each row in the Treeview widget
                self.tree.delete(row)                                                                                   # Delete the row from the Treeview widget
            cursor = self.conn.cursor()                                                                                 # Create a cursor object to execute SQL commands
            filtro = self.filter_var.get()                                                                              # Get the selected filter option from the combo
            if filtro == "By Name":                                                                                     # If the filter is set to "By
                cursor.execute("SELECT * FROM products ORDER BY Name")                                                  # Execute a SQL command to select all products ordered by name
            elif filtro == "By Quantity":                                                                               # If the filter is set to "By
                cursor.execute("SELECT * FROM products ORDER BY Quantity")                                              # Execute a SQL command to select all products ordered by quantity
            elif filtro == "By Value":                                                                                  # If the filter is set to "By
                cursor.execute("SELECT * FROM products ORDER BY Value")                                                 # Execute a SQL command to select all products ordered by value
            else:
                cursor.execute("SELECT * FROM products")                                                                # Execute a SQL command to select all products from the database
            products = cursor.fetchall()                                                                                # Fetch all the results from the executed command
            if products:                                                                                                # If there are products in the database
                for product in products:                                                                                # Iterate through each product
                    self.tree.insert("", "end", values=(product[3], product[0], product[1], product[2]))                # Insert the product details into the textbox
        except Exception as e:
            CTkMessagebox(title="Error", message=f"An error occurred while listing products: {e}", icon="cancel")       # Show an error message if there is an exception while listing products

# The function to create a connection to the SQLite database
class MainMenu(ctk.CTkFrame):                                                                                           # Create a class for the MainMenu, which inherits from ctk.CTkFrame
    def __init__(self, master, conn):                                                                                   # Initialize the MainMenu class with master
        super().__init__(master, fg_color=SECONDARY_COLOR)                                                              # Call the parent class constructor with a secondary color for the background
        self.conn = conn                                                                                                # Store the database connection
        ctk.CTkLabel(                                                                                                   # Create a label for the main menu and set its properties
            self,
            text="Welcome to the Inventory Management System",
            font=("Arial", 20, "bold"),
            text_color=PRIMARY_COLOR
        ).pack(pady=20)
        ctk.CTkButton(                                                                                                  # Create a button to add a product to the inventory and set its properties
            self, text="Add Product to inventory",
            command=self.show_add_product,
            fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
            text_color=BUTTON_TEXT, font=("Arial", 14, "bold"),
            width=220, height=40, corner_radius=10
        ).pack(pady=10)
        ctk.CTkButton(                                                                                                  # Create a button to remove a product from the inventory and set its properties
            self, text="Remove Product from inventory",
            command=self.show_remove_product,
            fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
            text_color=BUTTON_TEXT, font=("Arial", 14, "bold"),
            width=220, height=40, corner_radius=10
        ).pack(pady=5)
        ctk.CTkButton(                                                                                                  # Create a button to edit a product in the inventory and set its properties
            self, text="Edit Product in inventory",
            command=self.show_edit_product,
            fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
            text_color=BUTTON_TEXT, font=("Arial", 14, "bold"),
            width=220, height=40, corner_radius=10
        ).pack(pady=5)
        ctk.CTkButton(                                                                                                  # Create a button to list products in the inventory and set its properties
            self, text="List Products in inventory",
            command=self.show_list_products,
            fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER,
            text_color=BUTTON_TEXT, font=("Arial", 14, "bold"),
            width=220, height=40, corner_radius=10
        ).pack(pady=5)
        ctk.CTkButton(                                                                                                 # Create a button to exit the application and set its properties
            self, text="Exit", command=master.quit,
            fg_color="#aaa", hover_color="#888",
            text_color="#fff", font=("Arial", 12, "bold"),
            width=120, height=32, corner_radius=8
        ).pack(pady=10)

    def show_add_product(self):                                                                                         # Define the method to show the AddProductPage
        self.pack_forget()                                                                                              # Hide the main menu
        add_page.pack(fill="both", expand=True)                                                                         # Show the AddProductPage by packing it into the main window

    def show_remove_product(self):                                                                                      # Define the method to show the RemoveProductPage
        self.pack_forget()                                                                                              # Hide the main menu
        remove_page.pack(fill="both", expand=True)                                                                      # Show the RemoveProductPage by packing it into the main window

    def show_edit_product(self):                                                                                        # Define the method to show the EditProductPage
        self.pack_forget()                                                                                              # Hide the main menu
        edit_page.pack(fill="both", expand=True)                                                                        # Show the EditProductPage by packing it into the main window

    def show_list_products(self):                                                                                       # Define the method to show the ListProductsPage
        self.pack_forget()                                                                                              # Hide the main menu
        list_page.pack(fill="both", expand=True)                                                                        # Show the ListProductsPage by packing it into the main window

# The function to create a connection to the SQLite database
def show_main_menu():                                                                                                   # Define the function to show the main menu
    add_page.pack_forget()                                                                                              # Hide the AddProductPage
    remove_page.pack_forget()                                                                                           # Hide the RemoveProductPage
    edit_page.pack_forget()                                                                                             # Hide the EditProductPage
    list_page.pack_forget()                                                                                             # Hide the ListProductsPage
    main_menu.pack(fill="both", expand=True)                                                                            # Show the main menu by packing it into the main window

# The function to create a connection to the SQLite database
if __name__ == "__main__":                                                                                              # If this script is run directly (not imported as a module)
    conn = create_connection()                                                                                          # Create a connection to the database
    create_table(conn)                                                                                                  # Create the products table if it does not exist
    ctk.set_appearance_mode("System")                                                                                   # Set the appearance mode to system
    app = ctk.CTk()                                                                                                     # Create the main application window using customtkinter
    app.title("Inventory Management System")                                                                            # Set the title of the main window
    app.geometry("500x450")                                                                                             # Set the size of the main window                                                                             # Set the icon for the main window
    app.iconbitmap("assets/icon.ico")                                                                                   # Set the icon for the main window

    style = ttk.Style()                                                                                                 # Create a style object for the Treeview widget
    style.configure("Treeview", background=SECONDARY_COLOR, foreground=TEXT_COLOR, rowheight=25, fieldbackground=SECONDARY_COLOR)  # Configure the Treeview style with the secondary color and text color
    style.map("Treeview", background=[('selected', PRIMARY_COLOR), ('!selected', SECONDARY_COLOR)])                     # Map the Treeview style to change the background and foreground colors when selected

    main_menu = MainMenu(app, conn)                                                                                     # Create an instance of the MainMenu class
    add_page = AddProductPage(app, conn, show_main_menu)                                                                # Create an instance of the AddProductPage class
    remove_page = RemoveProductPage(app, conn, show_main_menu)                                                          # Create an instance of the RemoveProductPage class
    edit_page = EditProductPage(app, conn, show_main_menu)                                                              # Create an instance of the EditProductPage class
    list_page = ListProductsPage(app, conn, show_main_menu)                                                             # Create an instance of the ListProductsPage class

    main_menu.pack(fill="both", expand=True)                                                                            # Pack the main menu into the main window to make it visible
    try:
        app.mainloop()                                                                                                  # Start the main event loop of the application
    finally:
        conn.close()                                                                                                    # Close the database connection when the application is closed
