import sqlite3

def query_database():
    # Connect to the SQLite database
    connection = sqlite3.connect('instance/db.sqlite')

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Query to list all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Print out the list of tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # Close the cursor and connection
    cursor.close()
    connection.close()

# Call the function to query the database
query_database()

