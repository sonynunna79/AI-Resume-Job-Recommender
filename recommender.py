import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity



def recommend(resume):

    data = pd.read_csv("dataset/jobs.csv")


    vectorizer = TfidfVectorizer()


    vectors = vectorizer.fit_transform(
        data["Skills"].tolist() + [resume]
    )


    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )


    index = similarity.argmax()


    return data.iloc[index]["Job"]