import numpy as np
import pandas as pd
import ast

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# 1. Load Data
# ============================================================
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge datasets on title
movies = movies.merge(credits, on="title")

# Keep only required columns
movies = movies[
    ["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]
]

# Drop missing values
movies.dropna(inplace=True)


# ============================================================
# 2. Helper Functions
# ============================================================
def convert(obj):
    """
    Extract 'name' from list of dictionaries
    """
    return [i["name"] for i in ast.literal_eval(obj)]


def convert_cast(obj):
    """
    Extract top 3 cast members
    """
    cast_list = []
    for i, val in enumerate(ast.literal_eval(obj)):
        if i < 3:
            cast_list.append(val["name"])
    return cast_list


def fetch_director(obj):
    """
    Extract director name from crew
    """
    for i in ast.literal_eval(obj):
        if i["job"] == "Director":
            return [i["name"]]
    return []


# ============================================================
# 3. Apply Data Processing
# ============================================================
movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"] = movies["cast"].apply(convert_cast)
movies["crew"] = movies["crew"].apply(fetch_director)

# Split overview into words
movies["overview"] = movies["overview"].apply(lambda x: x.split())

# Remove spaces inside words
movies["genres"] = movies["genres"].apply(lambda x: [i.replace(" ", "") for i in x])
movies["keywords"] = movies["keywords"].apply(lambda x: [i.replace(" ", "") for i in x])
movies["cast"] = movies["cast"].apply(lambda x: [i.replace(" ", "") for i in x])
movies["crew"] = movies["crew"].apply(lambda x: [i.replace(" ", "") for i in x])


# ============================================================
# 4. Create Tags Column
# ============================================================
movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)

new_df = movies[["movie_id", "title", "tags"]].copy()
new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x).lower())



# ============================================================
# 5. Vectorization
# ============================================================
cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(new_df["tags"]).toarray()


# ============================================================
# 6. Cosine Similarity
# ============================================================
similarity = cosine_similarity(vectors)


# ============================================================
# 7. Recommendation Function
# ============================================================
def recommend(movie_name):
    if movie_name not in new_df["title"].values:
        print("❌ Movie not found!")
        return

    movie_index = new_df[new_df["title"] == movie_name].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    print(f"\n🎬 Recommended movies for '{movie_name}':\n")
    for i in movies_list:
        print(new_df.iloc[i[0]].title)


# ============================================================
# 8. Run Model
# ============================================================
if __name__ == "__main__":
    recommend("Avatar")

import pickle
pickle.dump(new_df.to_dict(),open("movies_dict.pkl", "wb"))

print(new_df['title'].values)

new_df.to_dict()

pickle.dump(similarity,open('similarity.pkl','wb'))