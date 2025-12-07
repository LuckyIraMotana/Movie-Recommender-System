# 🎬 Movie Recommender System

A content-based movie recommendation system that suggests movies based on similarity analysis using machine learning algorithms.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [API Keys](#api-keys)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This project implements a movie recommendation system that analyzes movie content (genres, cast, crew, keywords, and overview) to suggest similar movies to users. It uses cosine similarity algorithm to find the most similar movies based on content features.

## ✨ Features

- **Content-Based Recommendations**: Suggests movies based on content similarity
- **Real Movie Posters**: Fetches actual movie poster images from APIs
- **Interactive Web Interface**: User-friendly Streamlit web application
- **Fast Performance**: Pre-calculated similarity matrix for instant recommendations
- **Caching System**: Optimized image loading with caching
- **Multiple API Support**: Fallback systems for reliable poster fetching

## 🔧 Prerequisites

Before running this project, make sure you have:

- **Python 3.8+** installed on your system
- **pip** (Python package installer)
- **Internet connection** (for fetching movie posters)
- **Git** (optional, for cloning the repository)

## 📦 Installation

### Step 1: Clone or Download the Project
```bash
# If using Git
git clone https://github.com/Akash252004/Movie-Recommended-System.git
cd Movie-Recommended-System

# Or download and extract the ZIP file
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

### Step 3: Install Required Packages
```bash
pip install numpy pandas scikit-learn streamlit requests
```

## 📁 Project Structure

```
movie-recommender-system-tmdb-dataset/
├── app.py                 # Main Streamlit application
├── aa.py                  # Data processing and model training script
├── model/                 # Directory containing trained models
│   ├── movie_list.pkl    # Processed movie dataset
│   └── similarity.pkl    # Pre-calculated similarity matrix
├── env/                   # Virtual environment (created during setup)
├── README.md             # This file
└── notebook86c26b4f17.ipynb  # Original Jupyter notebook (optional)
```

## 🚀 How to Run

### Method 1: Using Pre-trained Models (Recommended)

If you already have the model files in the `model/` directory:

1. **Activate Virtual Environment**
   ```bash
   # On Windows:
   env\Scripts\activate
   
   # On macOS/Linux:
   source env/bin/activate
   ```

2. **Run the Application**
   ```bash
   streamlit run app.py
   ```

3. **Open in Browser**
   - The app will automatically open in your browser
   - Or manually go to: `http://localhost:8501` or `http://localhost:8502`

### Method 2: Train Models from Scratch

If you need to generate the model files:

1. **Activate Virtual Environment**
   ```bash
   env\Scripts\activate
   ```

2. **Run Data Processing Script**
   ```bash
   python aa.py
   ```

3. **Create Model Directory and Move Files**
   ```bash
   # On Windows:
   mkdir model
   move movie_list.pkl model\
   move similarity.pkl model\
   
   # On macOS/Linux:
   mkdir model
   mv movie_list.pkl model/
   mv similarity.pkl model/
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 🔍 How It Works

### 1. Data Processing (`aa.py`)
- Creates sample movie dataset with 10 popular movies
- Processes movie features: genres, keywords, cast, crew, overview
- Combines all features into a single "tags" column
- Uses CountVectorizer to convert text to numerical vectors
- Calculates cosine similarity between all movie pairs
- Saves processed data and similarity matrix as pickle files

### 2. Recommendation Engine (`app.py`)
- Loads pre-trained models from pickle files
- Provides interactive web interface using Streamlit
- When user selects a movie:
  - Finds the movie's index in the dataset
  - Retrieves similarity scores for that movie
  - Sorts movies by similarity (highest first)
  - Returns top 5 most similar movies
- Fetches real movie poster images from APIs
- Displays recommendations with movie titles and posters

### 3. Image Fetching System
- Tries multiple APIs for movie posters (OMDB, TMDB)
- Implements caching for faster loading
- Provides fallback placeholder images if APIs fail
- Handles network errors gracefully

## 🛠 Technologies Used

- **Python 3.8+**: Programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
  - CountVectorizer: Text vectorization
  - cosine_similarity: Similarity calculation
- **Streamlit**: Web application framework
- **Requests**: HTTP library for API calls
- **Pickle**: Model serialization and storage

## 🔑 API Keys

The project uses the following APIs for movie poster fetching:

- **TMDB API**: `a5b85f5cad8ef94d307fdc40786fa9db` (included in code)
- **OMDB API**: Uses free tier (no key required for basic usage)

**Note**: These are demo API keys. For production use, you should:
1. Get your own API keys from the respective services
2. Store them securely (environment variables, config files)
3. Never commit API keys to version control

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. "ModuleNotFoundError" when running
```bash
# Solution: Make sure virtual environment is activated and packages are installed
env\Scripts\activate
pip install -r requirements.txt
```

#### 2. "FileNotFoundError" for model files
```bash
# Solution: Run the data processing script first
python aa.py
mkdir model
move movie_list.pkl model\
move similarity.pkl model\
```

#### 3. Images not loading
- Check internet connection
- The app will show placeholder images if APIs are unavailable
- This is normal behavior and doesn't affect recommendations

#### 4. Port already in use
```bash
# Solution: Kill existing processes or use different port
streamlit run app.py --server.port 8503
```

#### 5. Streamlit not found
```bash
# Solution: Install Streamlit
pip install streamlit
```

### Performance Tips

- **First load**: May take a few seconds to fetch movie posters
- **Subsequent loads**: Much faster due to caching
- **Large datasets**: Consider using more powerful hardware for processing

## 📊 Sample Movies Included

The current dataset includes these popular movies:
1. The Dark Knight
2. Inception
3. Interstellar
4. The Matrix
5. Avatar
6. Titanic
7. Forrest Gump
8. The Godfather
9. Pulp Fiction
10. Fight Club

## 🔮 Future Enhancements

- Add more movies to the dataset
- Implement user rating system
- Add movie filtering options
- Improve recommendation algorithms
- Add movie details and reviews
- Implement user authentication
- Add recommendation history

## 📝 License

This project is for educational purposes. Please respect the terms of service of the APIs used (TMDB, OMDB).

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding more movies to the dataset
- Improving the recommendation algorithm
- Enhancing the user interface
- Adding new features
- Fixing bugs

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Ensure all prerequisites are met
3. Verify that all required packages are installed
4. Check your internet connection for image loading

---

**Happy Movie Recommending! 🎬✨**