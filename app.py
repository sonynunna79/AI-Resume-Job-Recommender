import pandas as pd


def recommend(resume):

    data = pd.read_csv("dataset/jobs.csv")

    resume = resume.lower()

    best_job = data.iloc[0]["Job"]
    best_score = 0

    for index, row in data.iterrows():

        skills = str(row["Skills"]).lower()

        skill_list = skills.replace(",", " ").split()

        match = 0

        for skill in skill_list:
            if skill in resume:
                match += 1

        score = (match / len(skill_list)) * 100

if "machine learning" in resume or "artificial intelligence" in resume or "ai" in resume:
    if row["Job"] in ["AI Engineer", "ML Engineer"]:
        score += 20

        if score >= best_score:
            best_score = score
            best_job = row["Job"]

    return best_job, round(best_score,2)