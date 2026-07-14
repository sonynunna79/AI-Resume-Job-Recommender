import streamlit as st
from recommender import recommend
from pypdf import PdfReader
from skills import find_missing_skills


st.title("AI Resume Job Recommender 🤖")


uploaded_file = st.file_uploader(
    resume_text = extract_text(uploaded_file)
    st.subheader("📄 Resume Extracted Text")

st.text_area(
    "Resume Text",
    resume_text,
    height=300
)
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


   recommendations = recommend(resume_text)

st.subheader("🏆 Top 5 Job Recommendations")

for job in recommendations:

    st.markdown(f"### 💼 {job['Job Title']}")

    st.progress(job["Match Score"] / 100)

    st.success(f"Match Score: {job['Match Score']}%")

    missing = find_missing_skills(resume_text, job["Job Title"])

    st.write("**Skills To Improve:**")

    if missing:
        for skill in missing:
            st.write("🔹", skill)
    else:
        st.write("🎉 Great! Your skills match this job.")

    st.markdown("---")
