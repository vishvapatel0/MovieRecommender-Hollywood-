import streamlit as st
import pickle
import requests

def fetch_pos(mov_id):
    requests.get()


st.title('Movie Recommender System')
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recMovie(movie):
    x = 0
    for i in movies:
        if i == selected_movie:
            movie_index = x
            break
        x += 1

    movie_location = movie_index
    distance = similarity[movie_location]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for j in movies_list:
        recommended_movies.append(j[0])
    return recommended_movies


movies_all = pickle.load(open('new_movies.pkl', 'rb'))
movies = movies_all['title'].values

selected_movie = st.selectbox(
    'Select one movie that you like',
    movies, index=None)

if st.button('Recommend'):
    recommendation = recMovie(selected_movie)

    for i in recommendation:
        with st.container():
            st.write(movies[i])
    st.balloons()