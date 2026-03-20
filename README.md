# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python, Pandas, and Scikit-learn.  
This project suggests movies similar to the one a user selects, based on metadata and similarity scores.

---

## 📖 Overview
This system uses the **TMDB 5000 dataset** to recommend movies.  
It calculates similarity between movies using features like cast, crew, genres, and keywords, then suggests the most relevant titles.

---

## 🗂️ Project Structure
- `Movie_Recom_System.ipynb` → Jupyter notebook with data preprocessing and model building.  
- `app.py` → Python script to run the recommendation app.  
- `movie_list.pkl` → Preprocessed movie list data.  
- `similarity.pkl` → Precomputed similarity matrix.  
- `tmdb_5000_movies.csv` → Dataset containing movie metadata.  
- `tmdb_5000_credits.zip` → Dataset containing cast and crew information.  

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/Movie_Recom_System.git
cd Movie_Recom_System
pip install -r requirements.txt
