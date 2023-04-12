import streamlit as st
import pickle
import pandas as pd
import requests


def poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b075ee7c6e87de1d28d291ed67dd1f00&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    path = data['poster_path']
    path = "https://image.tmdb.org/t/p/w500/"+path
    print(path)
    return path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch banner from API
        recommended_movies_poster.append(poster(movie_id))

    return recommended_movies, recommended_movies_poster


# Reading the input files
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies)
print(movies)
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select Movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])