import pandas as pd
import mysql.connector


def get_table_names(host, user, password, database):
    try:
        # Establish a database connection
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a query to retrieve table names
        query = f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = '{database}'"
        cursor.execute(query)

        # Fetch all the rows
        tables = cursor.fetchall()

        # Print table names
        # for (table_name,) in tables:
        #     print(table_name)

    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            return tables
        
        

def table_to_dataframe(host, user, password, database, table_name):
    try:
        # Establish a database connection
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Use backticks around the table name in the query
        query = f"SELECT * FROM `{table_name}`"

        # Use pandas to read the query into a DataFrame
        df = pd.read_sql(query, conn)

        return df

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return None
    finally:
        if conn.is_connected():
            conn.close()