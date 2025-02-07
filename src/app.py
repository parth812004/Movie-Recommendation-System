import pickle
import gzip
import streamlit as st
import requests
from requests.exceptions import ConnectionError
import time

compressed_file_path = "/Users/parthsoni/Documents/GitHub/Movie-Recommendation-System/src/model/similarity.pkl.gz"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.header('Movie Recommender System')
movies = pickle.load(open('/Users/parthsoni/Documents/GitHub/Movie-Recommendation-System/src/model/movie_list.pkl','rb'))
with gzip.open(compressed_file_path, "rb") as f:
    similarity = pickle.load(f)

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