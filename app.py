import streamlit as st
import pandas as pd

from sklearn import datasets

# Page Layout and it expands to full width
st.set_page_config(page_title='Determining Feature Importance - Machine Learning App',
                   layout='wide')



# Page Title and sub title
st.title("Data Preparation and Exploratory Data Analysis App")
st.write("**Made By: [Sohan Puthran](https://www.linkedin.com/in/sohansputhran/)**")

# Sidebar

# Input your csv
st.sidebar.header('Upload your CSV data')
uploaded_file = st.sidebar.file_uploader("", type=["csv"])
st.sidebar.header('Or')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))

else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.sidebar.button('Press to use Example Dataset'):
        data = datasets.load_boston() 
        df = pd.DataFrame(data.data, columns=data.feature_names)
        st.markdown('The ""Boston Housing Prices** dataset is used as the example.')
        st.write(df.head(5))