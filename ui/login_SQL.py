import mysql.connector
from mysql.connector import Error


def create_connection():
    connection = None
    try:
        # Change with your MySQL server details
        connection = mysql.connector.connect(
            host="localhost",
            user="hospital",
            passwd="",
            database="hospital"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

db=create_connection()