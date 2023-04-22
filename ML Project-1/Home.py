import pandas as pd
import streamlit as st

st.title(":red[Open Pubs Applicaion ]")

st.header(":blue[About the Dataset]")

df = pd.read_csv("cleaned_open_pubs.csv")
st.subheader("Head of the Data")
st.dataframe(df.head())
st.subheader("Tail of the Data")
st.dataframe(df.tail())

st.subheader("Shape of the Dataset")
st.write(df.shape)
st.write("Total number of Pubs:", df.shape[0])
st.write("Total number of columns:", df.shape[1])

st.subheader("Description of the Dataset")
st.dataframe(df.describe())

st.subheader("Null Values in the Dataset")
st.text(df.isnull().sum())

st.subheader("Duplicate Values in the Dataset")
st.markdown(df.duplicated().sum())

st.subheader("Correlation of our Dataset")
st.dataframe(df.corr())

st.subheader("Covariance of our Dataset")
st.dataframe(df.cov())

