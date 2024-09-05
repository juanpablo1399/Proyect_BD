import streamlit as st
import pandas as pd

def _extract_data_from_excel1(excel_file1):

    try:
        df1 = pd.read_excel(excel_file1)
        st.write(df1)  # Displays the dataframe
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []

        st.title("Upload list of employees excel")


st.title("Please upload the list of employees")

uploaded_file1 = st.file_uploader("Employee list", type=["xls", "xlsx"], key="file_uploader_1")
if uploaded_file1 is not None:
    st.write("First file was uploaded successfully.")
    _extract_data_from_excel1(uploaded_file1)



def _extract_data_from_excel2(excel_file2):
    
    try:
        df2 = pd.read_excel(excel_file2)
        st.write(df2)  # Displays the dataframe
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []

st.title("Please upload the list of Roles")

uploaded_file2 = st.file_uploader("Role list", type=["xls", "xlsx"], key="file_uploader_2")
if uploaded_file2 is not None:
    st.write("First file was uploaded successfully.")
    _extract_data_from_excel2(uploaded_file2)
    