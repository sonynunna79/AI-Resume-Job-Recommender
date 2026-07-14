import streamlit as st
import matplotlib.pyplot as plt
from recommender import recommend
from pypdf import PdfReader
from skills import find_missing_skills
from fpdf import FPDF

course_map = {
    "python": "Python for Everybody",
    "machine learning": "Machine Learning by Andrew Ng",
    "deep learning": "Deep Learning Specialization",
    "tensorflow": "TensorFlow Developer Certificate",
    "sql": "SQL for Data Science",
    "excel": "Microsoft Excel Essentials",
    "pandas": "Pandas for Data Analysis",
    "statistics": "Statistics for Data Science",
    "data analysis": "Google Data Analytics",
    "neural networks": "Neural Networks and Deep Learning"
}

st.set_page_config(
    page_title="AI Resume Job Recommender",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Job Recommender")

uploaded_file = st.file_uploader(
    "📄 Upload Your Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    st.success("✅ Resume uploaded successfully!")

    st.subheader("📄 Resume Extracted Text")

    st.text_area(
        "Resume Text",
        resume_text,
        height=250
    )

    recommendations = recommend(resume_text)
    st.subheader("🏆 Top 5 Job Recommendations")

for job in recommendations:

    st.markdown(f"## 💼 {job['Job Title']}")

    st.progress(job["Match Score"] / 100)

    st.success(f"Match Score: {job['Match Score']}%")

    missing = find_missing_skills(
        resume_text,
        job["Job Title"]
    )

    st.write("### Skills To Improve")

    if missing:

        for skill in missing:

            st.write(f"🔹 {skill}")

            if skill.lower() in course_map:

                st.info(
                    f"📚 Recommended Course: {course_map[skill.lower()]}"
                )

    else:

        st.success("🎉 Great! Your skills match this job.")

    st.markdown("---")
    st.subheader("📊 Skill Match Chart")

job_names = []
scores = []

for job in recommendations:

    job_names.append(job["Job Title"])
    scores.append(job["Match Score"])

fig, ax = plt.subplots()

ax.bar(job_names, scores)

plt.xticks(rotation=20)

plt.ylabel("Match Score (%)")

st.pyplot(fig)
pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=14)

pdf.cell(0, 10, "AI Resume Recommendation Report", new_x="LMARGIN", new_y="NEXT")

pdf.ln(5)

for job in recommendations:

    pdf.cell(
        0,
        10,
        f"{job['Job Title']} - {job['Match Score']}%",
        new_x="LMARGIN",
        new_y="NEXT"
    )

pdf.output("Recommendation_Report.pdf")

with open("Recommendation_Report.pdf", "rb") as pdf_file:

    st.download_button(
        label="📥 Download Recommendation Report",
        data=pdf_file,
        file_name="Recommendation_Report.pdf",
        mime="application/pdf"
    )
