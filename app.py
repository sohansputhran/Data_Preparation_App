import streamlit as st
import pandas as pd
import numpy as np

from sklearn import datasets

from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Page Layout and it expands to full width
st.set_page_config(page_title='Data Preparation and Exploratory Data Analysis App',
                   layout='wide')


# Page Title and sub title
st.title("Data Preparation and Exploratory Data Analysis App")
st.write("**Made By: [Sohan Puthran](https://www.linkedin.com/in/sohansputhran/)**")

# Sidebar

# Input your csv
st.sidebar.header('Upload your CSV data')
uploaded_file = st.sidebar.file_uploader("", type=["csv"])

data_selected = False
if not data_selected:
     st.sidebar.header('Or')
     st.info('Awaiting for CSV file to be uploaded.')

if uploaded_file is not None:
     df = pd.read_csv(uploaded_file)
     data_selected = True
     pr = ProfileReport(df, explorative=True)
     st.header('**Input DataFrame**')
     st.write(df.head(5))
     st.write('---')
     st.header('**Exploratory Data Analysis**')
     st_profile_report(pr)
else:
     if st.sidebar.button('Press to use Example Dataset'):
          data = datasets.fetch_california_housing() 
          df = pd.DataFrame(data.data, columns=data.feature_names)
          st.markdown('The **California Housing Prices** dataset is used as the example.')
          st.write(df.head(5))
          data_selected = True

          pr = ProfileReport(df, explorative=True)
          st.write('---')
          st.header('**Exploratory Data Analysis**')
          st_profile_report(pr)