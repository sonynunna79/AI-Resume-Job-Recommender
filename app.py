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
resume_text = st.text_area("Paste your resume text")
job, score = recommend(resume_text)

st.success("Recommended Job: " + job)

st.info(f"Match Score: {score}%")