import streamlit as st
import pandas as pd
from conection import connect_to_db, insert_merged_data_in_bulk

def _display_dataframe(df):
    st.write('Combined Dataframe')
    st.write(df)

def _extract_data_from_excel(excel):

    try:
        df1 = pd.read_excel(excel)
        st.write(df1)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []

        st.title("Upload list of employees excel")

st.title("Please upload the list of employees")

uploaded_file1 = st.file_uploader("Employee list", type=["xls", "xlsx"], key="file_uploader_1")
if uploaded_file1 is not None:
    st.write("First file was uploaded successfully.")
    _extract_data_from_excel(uploaded_file1)

st.title("Please upload the list of Roles")

uploaded_file2 = st.file_uploader("Role list", type=["xls", "xlsx"], key="file_uploader_2")
if uploaded_file2 is not None:
    st.write("First file was uploaded successfully.")
    _extract_data_from_excel(uploaded_file2)

if st.button("Join DataFrame"):
    df1=pd.read_excel(uploaded_file1)
    df2=pd.read_excel(uploaded_file2)
    if df1 is not None and df2 is not None:
        df=pd.concat([df1,df2],axis=1)
        st.session_state['df']=df
        _display_dataframe(df)
    else:
        st.write('Please upload info')


if st.button("Upload data in Data Base"):
    if 'df' in st.session_state and not st.session_state['df'].empty:
        df = st.session_state['df']
        insert_merged_data_in_bulk(df)
    else:
        st.write('No DataFrame to upload. Please join the DataFrames first.')
