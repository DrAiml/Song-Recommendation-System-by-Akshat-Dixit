Song Recommendation System
A modern, music-inspired web application built with Streamlit that recommends songs based on user input. Powered by a precomputed similarity matrix and a dataset of songs, this app delivers personalized song recommendations with a sleek, dark-themed UI reminiscent of Spotify and YouTube Music.
Features

Song Recommendations: Select a song from a dropdown and get five similar song recommendations, displayed with thumbnails in a visually appealing horizontal layout.
Modern UI: Features a dark theme with vibrant cyan-green gradients, glowing buttons, and hover effects for an engaging user experience.
Custom Styling: Includes custom CSS for a polished look with smooth animations, glowing selectbox and button, and elegant recommendation cards.
Placeholder Support: Prevents invalid inputs with a placeholder in the selectbox and a disabled recommendation button until a valid song is selected.
Designed by Akshat Dixit: A subtle credit displayed below the title in an italicized, glowing style to maintain the app's aesthetic.

Tech Stack

Streamlit: For building the interactive web app.
Python: Core programming language for data processing and recommendation logic.
Pandas: For handling the song dataset.
Joblib: For loading the precomputed dataset and similarity matrix.
Custom CSS: For a modern, music-inspired UI with glow effects and animations.

Installation

Clone the repository:git clone https://github.com/DrAiml/Song-Recommendation-System-by-Akshat-Dixit.git


Install dependencies:pip install streamlit pandas joblib


Ensure dataset.pkl and similarity.pkl are in the project directory (containing song data and similarity matrix, respectively).
Run the app:streamlit run app.py



Usage

Select a song from the dropdown menu.
Click the "Recommend Songs" button to view five recommended songs displayed as cards with thumbnails.
Hover over the button, selectbox, or cards for glowing effects and animations.

Dataset
The app uses a precomputed dataset (dataset.pkl) with song metadata (music_name, thumbnail) and a similarity matrix (similarity.pkl) for recommendations. Ensure these files are correctly formatted and available.

Credits
Designed and developed by Akshat Dixit.

License
MIT License