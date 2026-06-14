import streamlit as st
import pandas as pd
from src.sentiment import label

st.set_page_config(page_title="Sentiment Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv('data/results.csv')

df = load_data()


st.title("Sentiment Dashboard")
total_reviews = len(df)
positive_count = len(df[df['sentiment'] == 'positive'])
negative_count = len(df[df['sentiment'] == 'negative'])

col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", total_reviews)
col2.metric("Positive", positive_count)
col3.metric("Negative", negative_count)


st.subheader("Sentiment Distribution")
st.bar_chart(df['sentiment'].value_counts())


st.subheader("Most Positive Reviews")
st.table(df[df['sentiment'] == 'positive'].sort_values(by='score', ascending=False).head(5))


st.subheader("Test Sentiment Live")
user_input = st.text_input("Enter a sentence:")
if user_input:
    res_label, res_score = label(user_input)
    st.write(f"Label: {res_label}, Score: {res_score}")