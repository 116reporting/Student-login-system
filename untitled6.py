import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection with increased timeout settings
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Bloodysweet19",
        database="student",
        connection_timeout=600,  # 10 minutes
        allow_local_infile=True
    )

    if conn.is_connected():
        print("Connected to MySQL database")

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SELECT query
    query = "SELECT * FROM login LIMIT 0, 1000"
    cursor.execute(query)
    
    # Fetch the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
