import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend(resume):

    data = pd.read_csv("dataset/jobs.csv")

    vectorizer = TfidfVectorizer()

    job_vectors = vectorizer.fit_transform(data["Skills"])

    resume_vector = vectorizer.transform([resume])

    similarity = cosine_similarity(
        resume_vector,
        job_vectors
    )

    data["score"] = similarity[0]


    result = data.sort_values(
        by="score",
        ascending=False
    )


    job = result.iloc[0]["Job"]

    score = result.iloc[0]["score"] * 100


    return job, round(score,2)