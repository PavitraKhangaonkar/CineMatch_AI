import streamlit as st
import pickle
import pandas as pd
import requests
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")


# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# Must be the first Streamlit command
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",  # Use the full screen width
    initial_sidebar_state="expanded"
)

def fetch_poster(movie_id):
    try:
        url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        data = requests.get(url, timeout=5)
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path= "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except Exception as e:
        st.warning(f"Could not fetch poster: {str(e)}")
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
    recommended_movies_names =[]
    recommended_movies_posters =[]
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
       
        recommended_movies_posters.append(fetch_poster(movie_id))
         #fetch poster from api
        recommended_movies_names.append(movies.iloc[i[0]].title)

    return recommended_movies_names, recommended_movies_posters

st.header("Movie Recommender System with AI")
movies = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies)

similarity = pickle.load(open("similarity.pkl", "rb"))


movies_list = movies['title'].values
selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies_list
)

if st.button('show Recommendation '):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4 , col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])