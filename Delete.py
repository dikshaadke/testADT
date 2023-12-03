import streamlit as st
from pymongo import MongoClient
import os

# MongoDB setup
conn_str = "mongodb+srv://imdb_adt:imdb_adt@cluster0.rcvxgzc.mongodb.net/"
client = MongoClient(conn_str, serverSelectionTimeoutMS=60000)
db = client['Moviedatabase']
collection = db['moviedata']

# Streamlit UI
st.title("Movie Review Manager")

# Input for movie name
movie_name = st.text_input("Enter the movie name:", "Parasite_2019")

# Button to delete reviews
if st.button('Delete Non-helpful Reviews'):
    try:
        # MongoDB operation to delete reviews
        delete_criteria = {"MovieName": movie_name.strip(), "helpful": 0}
        result = collection.delete_many(delete_criteria)
        
        # Display the result
        st.write(f"Documents deleted: {result.deleted_count}")
    except Exception as e:
        st.write("An error occurred:", e)
