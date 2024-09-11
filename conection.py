import mysql.connector
import os
import streamlit as st
import pandas as pd

def connect_to_db():
    connection = None

    try:
        
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            st.write("Connected to the database successfully.")
            return connection
            

    except mysql.connector.Error as e:
        st.write(f"Error: {e}")
        if connection is not None:
            connection.rollback()



def insert_merged_data_in_bulk(df, table_name='employees_roles'):
    connection = connect_to_db()
    
    if connection is None:
        st.write('Failed to connect to Database')
        return

    cursor = connection.cursor()

    try:
        df.rename(columns={"phone number": "phonenumber"}, inplace=True)
        
        df['startdate'] = pd.to_datetime(df['startdate'], errors='coerce').dt.strftime('%Y-%m-%d')
        df['enddate'] = pd.to_datetime(df['enddate'], errors='coerce').dt.strftime('%Y-%m-%d')

        insert_query = f"""
        INSERT INTO {table_name} (name, startdate, phonenumber, email, enddate, role, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        data_concat = df[['name', 'startdate', 'phonenumber', 'email', 'enddate', 'role', 'description']].values.tolist()

        cursor.executemany(insert_query, data_concat)
        connection.commit()

        st.write(f"{cursor.rowcount} rows inserted successfully.")

    except mysql.connector.Error as e:
        st.write(f"Error inserting data: {e}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

