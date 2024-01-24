from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "RESUME.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Bryton Kilonzo"
PAGE_ICON = ":wave:"
NAME = "Bryton Kilonzo"
DESCRIPTION = """
Junior Back-end developer with 4+ years of experience designing and building scalable, high-performance applications.
"""
EMAIL = "brytonkilonzo@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/bryton-kilonzo-983171170/",
    "GitHub": "https://github.com/bryton90",
}
PROJECTS = {
    "🏆 ChatGPT Bot - The simplest telegram bot for dialogue with ChatGPT.": "https://railway.app/new/template/-S3lVz",
    "🏆 Open Pilot - openpilot is an open source driver assistance system.": "https://comma.ai/",
    "🏆 Random Dad Jokes - A simple project that generates dad jokes ": "https://icanhazdadjoke.com",
    "🏆 Apache Airflow - A platform to programmatically author, schedule, and monitor workflows": "https://airflow.apache.org/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, JavaScript and C++
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), C++, JavaScript, Typescript
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📈 Supplier relationship
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Junior Back-end Developer | Freelance**")
st.write("11/2023 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Agile and Project Management: Familiarity with agile development methodologies (e.g., Scrum or Kanban) and project management tools (e.g., JIRA) helped streamline development processes.
- ► Setting up CI/ CD pipelines to automate the testing, integration, and deployment of code changes to production environments.
"""
)

# --- JOB 2
st.write("\n")
st.write("🚧", "**Lead Generation | Lemontree**")
st.write("04/2023 - 09/2023")
st.write(
    """
- ► Conducted research on industry trends, competitors, and market analysis, providing valuable insights to support decision-making.
- ► Actively sought and incorporated feedback from clients to continuously improve virtual assistance services and adept to evolving needs.
- ► Successfully balanced multiple tasks and priorities, optimising time management and productivity.
"""
)

# --- JOB 3
st.write("\n")
st.write("🚧", "**Systems Admin | Emrill LLC**")
st.write("08/2017 - 01/2020")
st.write(
    """
- ► Implemented security best practices to protect against common vulnerabilities such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
