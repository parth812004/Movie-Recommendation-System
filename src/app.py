import pickle
import gzip
import streamlit as st
import requests
from requests.exceptions import ConnectionError
import time
import os

compressed_file_path = "src/model/similarity.pkl.gz"
movie_list_path = "src/model/movie_list.pkl"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.header('Movie Recommender System')

try:
    with open(movie_list_path, 'rb') as f:
        movies = pickle.load(f)
except FileNotFoundError:
    st.error(f"File not found: {movie_list_path}")
    st.stop()

try:
    with gzip.open(compressed_file_path, "rb") as f:
        similarity = pickle.load(f)
except FileNotFoundError:
    st.error(f"File not found: {compressed_file_path}")
    st.stop()

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(recommended_movie_names[0])
    with col2:
        st.write(recommended_movie_names[1])
    with col3:
        st.write(recommended_movie_names[2])
    with col4:
        st.write(recommended_movie_names[3])
    with col5:
        st.write(recommended_movie_names[4])