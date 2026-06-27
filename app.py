import streamlit as st

from resume_parser import extract_text

from recommender import recommend



st.title("AI Resume Analyzer & Job Recommendation System")


st.write("Upload your resume PDF and get suitable job recommendations")


file = st.file_uploader(
    "Upload Resume PDF",
    type="pdf"
)



if file:

    resume_text = extract_text(file)


    st.subheader("Resume Extracted Successfully")


    st.write(resume_text)


    job = recommend(resume_text)


    st.success(
        "Recommended Job: " + job
    )