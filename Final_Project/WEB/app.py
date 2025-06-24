import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Get the absolute path to the current directory
basedir = os.path.abspath(os.path.dirname(__file__))                                                            # Get the directory where this script is located

# Path to the database file in the parent 'Software' folder
db_path = os.path.abspath(os.path.join(basedir, "..", "Software", "database.db"))                               # Change this to your actual database path
db_uri = f"sqlite:///{os.path.abspath(db_path)}"                                                                # SQLite database URI

app = Flask(
    __name__,
    template_folder=os.path.join(basedir, 'templates'),                                                         # Template folder path
    static_folder=os.path.join(basedir, 'static')                                                               # Static folder path
)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri                                                                  # Set the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                                                            # Disable track modifications to save resources
db = SQLAlchemy(app)                                                                                            # Initialize the SQLAlchemy object

class Item(db.Model):                                                                                           # Define the Item model
    __tablename__ = 'products'                                                                                  # Table name in the database
    id = db.Column('Id', db.Integer, primary_key=True)                                                          # Primary key column
    name = db.Column('Name', db.String(80), nullable=False)                                                     # Name column, cannot be null
    quantity = db.Column('Quantity', db.Integer, nullable=False)                                                # Quantity column, cannot be null
    value = db.Column('Value', db.Float, nullable=False)                                                        # Value column, cannot be null

    def to_dict(self):                                                                                          # Method to convert Item object to dictionary
        return {                                                                                                # Convert the Item object to a dictionary
            'name': self.name,
            'quantity': self.quantity,
            'value': self.value,
            'id': self.id,
        }

@app.route("/api/items", methods=['GET'])                                                                       # API endpoint to get all items                       
def get_items():                                                                                                # Define the function to handle the request                        
    try:
        items = Item.query.all()                                                                                # Query all items from the database   
        items_data = [item.to_dict() for item in items]                                                         # Convert each item to a dictionary       
        return jsonify(items_data)                                                                              # Return the items as JSON response      
    except Exception as e:                                                                                      # Handle any exceptions that occur   
        return jsonify({"error": str(e)}), 500                                                                  # Return an error message if an exception occurs    

@app.route("/")                                                                                                 # Route for the index page
def index():                                                                                                    # Define the function to handle the request
    items = Item.query.all()                                                                                    # Query all items from the database
    return render_template("index.html", items=items)                                                           # Render the index template with items

@app.route('/catalog')                                                                                          # Route for the catalog page
def catalog():                                                                                                  # Define the function to handle the request
    items = Item.query.all()                                                                                    # Query all items from the database
    return render_template("catalog.html", items=items)                                                         # Render the catalog template with items

if __name__ == "__main__":                                                                                      # Check if this script is run directly
    # Create tables and run the app if they do not exist
    with app.app_context():                                                                                     # Create an application context for database operations
        db.create_all()                                                                                         # Create all tables defined by SQLAlchemy models
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")                                                    # Run the Flask application in debug mode if FLASK_DEBUG is set to 1