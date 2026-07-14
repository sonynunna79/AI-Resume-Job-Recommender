import streamlit as st
from recommender import recommend
from pypdf import PdfReader
from skills import find_missing_skills


st.title("AI Resume Job Recommender 🤖")


uploaded_file = st.file_uploader(
    resume_text = extract_text(uploaded_file)
    "Upload Your Resume PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            resume_text += text


    st.success("Resume uploaded successfully ✅")


    job, score = recommend(resume_text)


    st.subheader("Recommended Job")

    st.info(job)


    st.subheader("Resume Match Score")

    st.progress(score / 100)

    st.success(f"Match Score: {score}%")


    missing = find_missing_skills(resume_text, job)


    st.subheader("Skills To Improve")


    if missing:

        for skill in missing:

            st.write("🔹", skill)


    else:

        st.write("Great! Your skills match the job 🎉")
