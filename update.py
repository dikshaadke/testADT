import streamlit as st
from pymongo import MongoClient
import os

# MongoDB setup
conn_str = "mongodb+srv://imdb_adt:imdb_adt@cluster0.rcvxgzc.mongodb.net"
client = MongoClient(conn_str, serverSelectionTimeoutMS=60000)
db = client['Moviedatabase']
collection = db['moviedata']

# Streamlit UI
st.title("Movie Review Manager")

# Input for movie name and review ID
movie_name = st.text_input("Enter the movie name:", "Parasite_2019")
review_id = st.text_input("Enter the review ID to mark as helpful:", "")

# Button to mark review as helpful
if st.button('Mark Review as Helpful'):
    try:
        review_id_obj = ObjectId(review_id)
        # MongoDB operation to update the review
        update_criteria = {
            "_id": review_id_obj,
            "MovieName": movie_name.strip()
        }
        update_action = {
            "$inc": {
                "helpful": 1,
                "total_votes": 1
            }
        }
        result = collection.update_one(update_criteria, update_action)
        
        # Display the result
        if result.matched_count > 0:
            st.write(f"Review updated successfully. Matched Count: {result.matched_count}, Modified Count: {result.modified_count}")
        else:
            st.write("No matching document found.")
    except Exception as e:
        st.write("An error occurred:", e)




        
