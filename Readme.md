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



🌐 Deployment

## Prerequisites
1. **TMDB API Key**: Get your free API key from [TMDB](https://www.themoviedb.org/settings/api)
2. **GitHub Repository**: Your code should be pushed to GitHub

## Deployment Options

### 1. Streamlit Cloud (Recommended - Free & Easy)
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub account
3. Select the `Cinematch_AI` repository
4. Set main file path to `app.py`
5. Add secret: `TMDB_API_KEY` = your_api_key
6. Click Deploy

### 2. Render (Free tier available)
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repo
4. Configure:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port $PORT --server.headless true --server.runOnSave false`
5. Add environment variable: `TMDB_API_KEY` = your_api_key
6. Click Create Web Service

### 3. Heroku
1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Set environment variable: `heroku config:set TMDB_API_KEY=your_api_key`
5. Deploy: `git push heroku main`

### 4. Docker (For any cloud provider)
1. Build image: `docker build -t cinematch-ai .`
2. Run locally: `docker run -p 8501:8501 -e TMDB_API_KEY=your_key cinematch-ai`
3. Deploy to Docker Hub, then to your preferred cloud platform

## Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export TMDB_API_KEY=your_api_key

# Run the app
streamlit run app.py
```

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