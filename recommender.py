import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend(resume_text):

    jobs = [
        {
            "title": "AI Engineer",
            "skills": "python machine learning deep learning tensorflow ai"
        },
        {
            "title": "Data Analyst",
            "skills": "python sql excel pandas data analysis"
        },
        {
            "title": "Machine Learning Engineer",
            "skills": "python machine learning algorithms neural networks"
        },
        {
            "title": "Data Scientist",
            "skills": "python statistics machine learning data science"
        }
    ]

    job_titles = []
    job_skills = []

    for job in jobs:
        job_titles.append(job["title"])
        job_skills.append(job["skills"])


    documents = [resume_text] + job_skills


    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)


    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:]
    )


    scores = similarity[0]


    best_index = scores.argmax()


    best_job = job_titles[best_index]


    score = round(scores[best_index] * 100, 2)


    return best_job, score