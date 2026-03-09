# Movie Recommender System

A simple movie recommendation system built using **content-based filtering** to suggest similar movies based on user selection.

## About This Project

This is a **learning project** I built to understand basic Machine Learning concepts like:
- **K-Nearest Neighbors (KNN)** for finding similar items
- **Cosine Similarity** for measuring movie similarity
- **Feature Engineering** and text vectorization
- Working with real-world datasets

> **Note:** This is a basic implementation created for educational purposes while learning ML fundamentals during my B.Tech.

## Dataset

- **TMDB 5000 Movie Dataset** (from Kaggle)
- Contains movie metadata like genres, cast, crew, keywords, overview, etc.

## Tech Stack

- **Python** - Core programming language
- **Streamlit** - Web interface
- **Pandas** - Data manipulation
- **Scikit-learn** - ML algorithms (CountVectorizer, Cosine Similarity)
- **Pickle** - Model serialization
- **TMDB API** - Fetching movie posters

## How It Works

1. **Data Preprocessing:** Combined multiple features (genres, keywords, cast, crew) into a single text field
2. **Vectorization:** Converted text data into numerical vectors using CountVectorizer
3. **Similarity Calculation:** Used cosine similarity to find movies with similar feature vectors
4. **Recommendation:** Returns top 5 most similar movies based on the selected movie

## Installation & Setup

```bash
# Clone the repository
git clone https://github.com/SD1920/Movie_Recommender.git
cd Movie_Recommender

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Project Structure

```
Movie_Recommender/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            
└── README.md
```

> **Note:** The `.pkl` files (movies2.pkl, similarity2.pkl) are automatically downloaded from Google Drive when you run the app for the first time.

## Features

- Search and select from 5000+ movies
- Get 5 similar movie recommendations
- View movie posters fetched from TMDB API
- Clean and simple UI

## Learning Outcomes

Through this project, I learned:
- How recommendation systems work
- Text preprocessing and feature extraction
- Similarity metrics in ML
- Building web apps with Streamlit
- Working with APIs

## Future Improvements

- Add collaborative filtering
- Implement hybrid recommendation (content + collaborative)
- Add movie ratings and reviews
- Improve UI/UX

---

**Disclaimer:** This is a basic learning project and not production-ready code. Feel free to fork and improve!