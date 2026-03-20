import streamlit as st
import pandas as pd
import pickle

# ---------------------------------------------------
# Load the data
# ---------------------------------------------------
movies = pd.read_pickle('movie_list (1).pkl')

with open('similarity (1).pkl', 'rb') as f:
    similarity = pickle.load(f)

# ---------------------------------------------------
# Recommendation function
# ---------------------------------------------------
def recommend(movie):
    try:
        index = movies[movies['title'].str.lower() == movie.lower()].index[0]
    except IndexError:
        return ['Movie not found']
    
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)
    return [movies.iloc[i[0]].title for i in distances[1:6]]

# ---------------------------------------------------
# Streamlit UI
# ---------------------------------------------------
st.title('Movie Recommendation System')

movie_list = movies['title'].values
selected_movie = st.selectbox('Select a Movie', movie_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for movie in recommendations:
        st.write(movie)

