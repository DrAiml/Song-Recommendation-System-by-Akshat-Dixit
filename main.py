import streamlit as st
import joblib
import pandas as pd

# Inject custom CSS for a modern, glowing UI
st.markdown("""
    <style>
    /* Global styles */
    .stApp {
        background: linear-gradient(to bottom, #1c2526, #000000);
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }

    /* Title styling */
    h1 {
        color: #00DDEB; /* Vibrant cyan for title */
        text-align: center;
        font-size: 3.2em;
        text-shadow: 0 0 15px rgba(0, 221, 235, 0.6);
        margin-bottom: 25px;
        letter-spacing: 1px;
    }

    /* Subheader styling */
    h3 {
        color: #E0E0E0;
        text-align: center;
        font-size: 1.6em;
        margin-top: 35px;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.3);
    }

    /* Selectbox styling with glow effect */
    .stSelectbox > div > div {
        background-color: #2A2A2A;
        border: 2px solid #00DDEB; /* Cyan border */
        border-radius: 10px;
        color: #FFFFFF;
        padding: 12px;
        box-shadow: 0 0 12px rgba(0, 221, 235, 0.4);
        transition: box-shadow 0.3s ease, border-color 0.3s ease;
    }
    .stSelectbox > div > div:hover {
        box-shadow: 0 0 20px rgba(0, 221, 235, 0.7);
        border-color: #1ED760; /* Spotify green on hover */
    }

    /* Button styling with glow effect */
    .stButton > button {
        background: linear-gradient(45deg, #00DDEB, #1ED760); /* Gradient with cyan and Spotify green */
        color: #000000;
        border: none;
        border-radius: 50px;
        padding: 12px 30px;
        font-size: 1.3em;
        font-weight: 600;
        display: block;
        margin: 25px auto;
        box-shadow: 0 0 15px rgba(0, 221, 235, 0.5);
        transition: box-shadow 0.3s ease, transform 0.3s ease;
    }
    .stButton > button:hover {
        box-shadow: 0 0 25px rgba(0, 221, 235, 0.8), 0 0 10px rgba(29, 185, 84, 0.7);
        transform: translateY(-2px);
        background: linear-gradient(45deg, #1ED760, #00DDEB);
    }

    /* Recommendation cards */
    .recommend-card {
        background-color: #2A2A2A;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .recommend-card:hover {
        transform: scale(1.08);
        box-shadow: 0 8px 20px rgba(0, 221, 235, 0.5);
    }

    /* Image styling */
    img {
        border-radius: 10px;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Text in cards */
    .song-name {
        color: #FFFFFF;
        font-size: 1.1em;
        font-weight: 600;
        margin: 0;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.2);
    }

    /* Hide Streamlit default elements for cleaner UI */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title('🎶 Song Recommendation System')

# Load dataset and similarity matrix
songs = joblib.load("dataset.pkl")  # DataFrame with song data
similarity = joblib.load("similarity.pkl")  # Similarity matrix

# Recommendation function
def recommend(song):
    song_index = songs[songs['music_name'] == song].index[0]  # Get index of selected song
    distances = similarity[song_index]  # Similarity scores for the song
    song_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_songs = []
    for i in song_list:
        song_data = songs.iloc[i[0]]
        recommended_songs.append({
            'name': song_data['music_name'],
            'thumbnail': song_data['thumbnail']  # Fetch thumbnail URL
        })
    return recommended_songs

# Streamlit dropdown
selected_song_name = st.selectbox('🎵 Select a song:', songs['music_name'].values)

if st.button('Recommend Songs'):
    recommendations = recommend(selected_song_name)

    st.subheader("Recommended Songs:")

    # Create horizontal layout with columns for recommendations
    cols = st.columns(5)  # 5 columns for 5 recommendations
    for idx, song in enumerate(recommendations):
        with cols[idx]:
            # Display as a card
            st.markdown('<div class="recommend-card">', unsafe_allow_html=True)
            try:
                st.image(song['thumbnail'], width=150)  # Keep thumbnail size consistent
            except Exception as e:
                st.write("Thumbnail not available")
            st.markdown(f'<p class="song-name">👉 {song["name"]}</p>', unsafe_allow_html=True)
            st.markdown('<'
                        '/div>', unsafe_allow_html=True)