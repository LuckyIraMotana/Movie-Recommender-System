import pickle
import streamlit as st
import requests
import time

# Cache for movie posters to avoid repeated API calls
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_cached_poster(movie_title):
    return fetch_poster_uncached(movie_title)

def fetch_poster_uncached(movie_title):
    # Try multiple sources for movie posters
    try:
        # First try: Use a free movie poster API
        import urllib.parse
        encoded_title = urllib.parse.quote(movie_title)
        
        # Try OMDB API (free tier)
        omdb_url = f"http://www.omdbapi.com/?t={encoded_title}&apikey=trilogy"
        response = requests.get(omdb_url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            if data.get('Poster') and data['Poster'] != 'N/A':
                return data['Poster']
        
        # Fallback: Try TMDB with better error handling
        tmdb_url = f"https://api.themoviedb.org/3/search/movie?api_key=a5b85f5cad8ef94d307fdc40786fa9db&query={encoded_title}"
        response = requests.get(tmdb_url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            if data.get('results') and len(data['results']) > 0:
                poster_path = data['results'][0].get('poster_path')
                if poster_path:
                    return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        
        # If all APIs fail, use a better placeholder
        return f"https://via.placeholder.com/300x450/1a1a1a/ffffff?text={movie_title.replace(' ', '+')}"
        
    except Exception as e:
        print(f"Error fetching poster for {movie_title}: {e}")
        return f"https://via.placeholder.com/300x450/1a1a1a/ffffff?text={movie_title.replace(' ', '+')}"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster using movie title
        movie_title = movies.iloc[i[0]].title
        recommended_movie_posters.append(get_cached_poster(movie_title))
        recommended_movie_names.append(movie_title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
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





