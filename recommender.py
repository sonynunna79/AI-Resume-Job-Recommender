import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend(resume):

    data = pd.read_csv("dataset/jobs.csv")

    # convert to lowercase
    skills = data["Skills"].astype(str).str.lower()

    resume = resume.lower()

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    job_vectors = vectorizer.fit_transform(skills)

    resume_vector = vectorizer.transform([resume])

    similarity = cosine_similarity(
        resume_vector,
        job_vectors
    )

    index = similarity.argmax()

    job = data.iloc[index]["Job"]

    score = similarity[0][index] * 100

    return job, round(score,2)