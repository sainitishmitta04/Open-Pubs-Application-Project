import streamlit as st
import pandas as pd
import os

#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH1 = os.path.join(dir_of_interest, "cleaned_open_pubs.csv")
df = pd.read_csv(DATA_PATH1)


st.header(":blue[Location of all Bars in UK]")
local_author = st.selectbox('Select Local Authority : ', set(df['local_authority']))
button_1 = st.button("Submit")

if button_1:
    st.snow()
    df_new = df.loc[(df['local_authority'] == local_author)]
    st.subheader(":violet[Total Number of Pubs in this location are:]")
    st.write(df_new.shape[0])
    st.map(df_new)
    st.subheader(":green[List of Pubs]")
    st.dataframe(df_new)
