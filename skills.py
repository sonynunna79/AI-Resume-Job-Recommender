def find_missing_skills(resume_text, job):

    resume_text = resume_text.lower()

    job_skills = {

        "AI Engineer": [
            "python",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch"
        ],

        "Data Scientist": [
            "python",
            "statistics",
            "machine learning",
            "pandas",
            "sql"
        ],

        "Data Analyst": [
            "excel",
            "sql",
            "python",
            "data analysis",
            "pandas"
        ],

        "Machine Learning Engineer": [
            "python",
            "algorithms",
            "machine learning",
            "neural networks"
        ]
    }


    required = job_skills.get(job, [])

    missing = []


    for skill in required:

        if skill not in resume_text:

            missing.append(skill)


    return missing