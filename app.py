import streamlit as st
import pickle
import requests
import pandas as pd
import time
import os
import gdown

st.set_page_config(layout="wide")
st.title('Movie Recommender System')

def download_file_from_gdrive(file_id, output_path):
    """Download file from Google Drive if it doesn't exist locally"""
    if not os.path.exists(output_path):
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url, output_path, quiet=False)

def fetch_poster(movie_id):
    api_key = "c4676125ff34068b5733dc6284b3f133"
    url = f"https://api.themoviedb.org/3/movie/{int(movie_id)}?api_key={api_key}&language=en-US"
    retries = 15
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('poster_path'):
                    return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
            elif response.status_code == 404:
                print(f"Movie with ID {movie_id} not found (404).")
                break
        except requests.exceptions.RequestException as e:
            print(f"Network error for movie_id {movie_id}: {e}. Retrying ({i + 1}/{retries})...")
            time.sleep(i + 1)
    return "https://via.placeholder.com/500x750/666666/ffffff?text=Poster+Not+Available"

def recommend(movie):
    import numpy as np
    from scipy.sparse import issparse
    
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    
    # Handle sparse matrix
    if issparse(similarity):
        distances = similarity[int(movie_index)].toarray().flatten()
    else:
        distances = similarity[int(movie_index)]
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        movie_title = movies_df.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_id))
        time.sleep(0.4)
    return recommended_movies, recommended_posters

try:
    # Google Drive file IDs
    MOVIES_FILE_ID = "1-RLBsi_30ONtDFcL8fT_G1WXNbtDDPgH"
    SIMILARITY_FILE_ID = "1_qdH6bU_8d6brd4YpdDhi__6_u2mE2xB"
    
    # Download files if not present
    with st.spinner('Loading movie data...'):
        download_file_from_gdrive(MOVIES_FILE_ID, 'movies2.pkl')
        download_file_from_gdrive(SIMILARITY_FILE_ID, 'similarity2.pkl')
    
    # Load the pickle files
    movies_df = pickle.load(open('movies2.pkl', 'rb'))
    movies_list = sorted(movies_df['title'].values)
    similarity = pickle.load(open('similarity2.pkl', 'rb'))
    
    selected_movie = st.selectbox(
        'Select a movie!',
        options=['Select a movie....'] + list(movies_list),
        index=0
    )
    
    if st.button("Recommend"):
        if selected_movie != 'Select a movie....':
            with st.spinner('Getting recommendations...'):
                recommendations, posters = recommend(selected_movie)
            st.subheader(f"Movies similar to '{selected_movie}':")
            cols = st.columns(len(recommendations))
            for idx, col in enumerate(cols):
                with col:
                    st.image(posters[idx])
                    st.write(f"**{recommendations[idx]}**")
        else:
            st.warning("Please select a movie first!")
            
except FileNotFoundError:
    st.error("One of the pickle files (movies2.pkl, similarity2.pkl) was not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")