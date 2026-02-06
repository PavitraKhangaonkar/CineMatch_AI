🎬 CineMatch_AI
 
Intelligent Movie Recommendation System 

CineMatch_AI is an AI-powered movie recommendation system that applies classical Machine Learning and Natural Language Processing (NLP) techniques to recommend movies similar to a user’s choice.
The application is deployed live on Render and provides an interactive experience using Streamlit.
• ML • NLP • Streamlit • Render


🔗 Live Demo: https://your-app-name.onrender.com


🚀 Project Overview

• Finding movies that match user preferences can be challenging due to the large volume of content available.
• CineMatch_AI solves this by:
• Learning patterns from movie metadata
• Computing similarity between movies
• Automatically recommending relevant movies
• This is a content-based recommendation system, built end-to-end and deployed to the cloud.

🤖 Why This Is an AI Project

• CineMatch_AI applies Artificial Intelligence through Machine Learning, where the system:
• Learns from data instead of hardcoded rules
• Uses NLP to process textual information
• Makes automated recommendations based on learned similarity patterns

Top 5 similar movies for a selected title


🏗️ System Architecture
User Movie Selection
        ↓
Text Feature Engineering
        ↓
Vectorization (CountVectorizer)
        ↓
Cosine Similarity Matrix
        ↓
Top-N Movie Recommendations
        ↓
Streamlit UI + TMDB Posters



🌐 Deployment (Render)

-Deployed as a Render Web Service
-Publicly accessible URL
-Environment variables used for secure API handling
-Render Commands

Build Command:

pip install -r requirements.txt


Start Command:

streamlit run app.py --server.port $PORT --server.address 0.0.0.0


🔐 API & Security

->Movie posters fetched using TMDB API
->API key stored securely as a Render environment variable

import os
API_KEY = os.getenv("TMDB_API_KEY")


✔ No hardcoded secrets
✔ Follows deployment best practices

🛠️ Tech Stack

Python
Pandas, NumPy
Scikit-learn
Natural Language Processing (NLP)
Streamlit
TMDB API
Render (Cloud Deployment)


📁 Project Structure
CineMatch_AI/
│
├── app.py                  # Streamlit application
├── movies.pkl              # Preprocessed movie data
├── similarity.pkl          # Cosine similarity matrix
├── requirements.txt        # Dependencies
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── README.md

📊 Limitations

Content-based filtering only (no user behavior data)
Cold-start problem for new movies
Recommendations depend on metadata quality
These trade-offs were intentionally chosen for simplicity and clarity.

🔮 Future Enhancements

Collaborative filtering
Hybrid recommendation system
User personalization
Performance optimization with caching
Model evaluation metrics


🎯 Skills Demonstrated

Artificial Intelligence (Classical ML)
Recommendation systems
NLP-based feature engineering
Similarity-based modeling
Streamlit app development
Cloud deployment (Render)
Secure API management


🙌 Acknowledgements

TMDB for movie data
Streamlit for UI framework
Scikit-learn for ML utilities

⭐ CineMatch_AI demonstrates my ability to design, explain, and deploy an AI-powered system end-to-end.