import mysql.connector
import os
import streamlit as st

def insert_merged_data_in_bulk(df, table_name='employees_roles'):
    connection = None
    cursor = None

    try:
        
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            st.write("Connected to the database successfully.")
            cursor = connection.cursor()

            
            create_table_if_not_exists(connection)

            s
            df.rename(columns={"phone number": "phonenumber"}, inplace=True)

            
            df['startdate'] = pd.to_datetime(df['startdate'], errors='coerce')
            df['enddate'] = pd.to_datetime(df['enddate'], errors='coerce')

            insert_query = f"""
            INSERT INTO {table_name} (name, startdate, phonenumber, email, enddate, role, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            merge_data = df[['name', 'startdate', 'phonenumber', 'email', 'enddate', 'role', 'description']].to_records(index=False).tolist()

            
            cursor.executemany(insert_query, merged_data)
            connection.commit()

            st.write(f"{cursor.rowcount} rows inserted successfully.")

    except mysql.connector.Error as e:
        st.write(f"Error: {e}")
        if connection:
            connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


st.title("Upload the list of employees and roles")


uploaded_file1 = st.file_uploader("Employee", type=["xls", "xlsx"], key="file_uploader_1")
df1 = None
if uploaded_file1 is not None:
    df1 = _extract_data_from_excel1(uploaded_file1)


uploaded_file2 = st.file_uploader("Role", type=["xls", "xlsx"], key="file_uploader_2")
df2 = None
if uploaded_file2 is not None:
    df2 = _extract_data_from_excel2(uploaded_file2)


if st.button("Join DataFrames and Insert into Database"):
    if df1 is not None and df2 is not None:
        df = pd.concat([df1, df2], axis=1)  
        _display_dataframe(df)  
        
        
        insert_merged_data_in_bulk(df)
    else:
        st.write("Please upload both Excel files before merging.")