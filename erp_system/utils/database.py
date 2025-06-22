import sqlite3
import os

# Define the path for the database file within the erp_system directory
# This makes it relative to the project's root, assuming erp_system is the root
DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database') # Puts db in erp_system/database/
DB_NAME = "erp_main.db"
DB_PATH = os.path.join(DB_DIR, DB_NAME)

def init_db():
    """Initializes the database and creates tables if they don't exist."""
    # Ensure the database directory exists
    os.makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Example: Create an Employees table for the HR module
    # In a real ERP, this would be much more complex and split across many tables/modules
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE,
        phone_number TEXT,
        department TEXT,
        position TEXT,
        hire_date TEXT,
        salary REAL
    )
    """)

    # Example: Create a simple table for Journal Entries for Finance Module
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS journal_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_date TEXT NOT NULL,
        description TEXT,
        account TEXT NOT NULL, -- Could be a foreign key to a Chart of Accounts table
        debit REAL DEFAULT 0,
        credit REAL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Add more table creation statements here as modules are developed
    # e.g., for inventory, sales, procurement etc.

    conn.commit()
    conn.close()
    print(f"Database initialized/checked at {DB_PATH}")

def get_db_connection():
    """Returns a connection to the SQLite database."""
    if not os.path.exists(DB_PATH):
        # This case should ideally be handled by init_db() being called at startup
        print("Database file does not exist. Please initialize the database first.")
        # Optionally, call init_db() here, but it's better to ensure it's called once at startup.
        # init_db()
        return None # Or raise an error

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row # Access columns by name
    return conn

if __name__ == '__main__':
    # This allows running this script directly to initialize the database
    print("Initializing database directly...")
    init_db()
    print("Database initialization complete.")

    # Example of adding a dummy employee if the table is empty
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM employees")
        if cursor.fetchone()[0] == 0:
            print("Adding dummy employee data...")
            try:
                cursor.execute("INSERT INTO employees (first_name, last_name, email, department, position, hire_date, salary) VALUES (?, ?, ?, ?, ?, ?, ?)",
                               ("John", "Doe", "john.doe@example.com", "IT", "Developer", "2023-01-15", 60000))
                conn.commit()
                print("Dummy employee added.")
            except sqlite3.Error as e:
                print(f"Error adding dummy employee: {e}")
        conn.close()
