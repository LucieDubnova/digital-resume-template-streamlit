import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Lucie Dubnová"
PAGE_ICON = ":wave:"
NAME = "Ing. Lucie Dubnová"
DESCRIPTION = """
Specialist in data analytics with a focus on continuous improvement and energy management.
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load profile picture
profile_pic = Image.open("foto CV.jpg")

# Sidebar
with st.sidebar:
    st.image(profile_pic, width=150)
    st.title(NAME)
    st.write(DESCRIPTION)
    my_radio = st.radio("Choose a section", {
        "About Me": "Learn more about Lucie",
        "Experience & Qualifications": "Lucie's professional background",
        "Skills": "Lucie's skill set",
        "Education & Training": "Lucie's educational background and trainings"
    })

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("Pod Strání 880, 252 66 Libčice nad Vltavou")
    st.write("Tel.: +420 608 946 482")
    st.write("Email: lucie.dubnova@seznam.cz")

if my_radio == "About Me":
    st.subheader("About Me")
    st.write("""
    I am constantly thinking about what can be done better and more efficiently. 
    I enjoy working with data, focusing not only on analysis but also on proper data collection. 
    Effective communication is often the key to the success of a project, and I embrace this challenge by utilizing both my technical and communication skills. 
    I have proven my ability to complete even complex projects successfully.
    """)

if my_radio == "Experience & Qualifications":
    st.subheader("Experience & Qualifications")
    st.write("""
    - **CI Engineer at Adient s.r.o., Kvasiny (2016 – 2023)**:
        - Led projects focused on savings and continuous improvement.
        - Implemented and maintained corporate standards.
        - Managed energy management systems.
        - Achievements:
            - Implemented an energy management system per ISO 50001:2018 in a new production hall.
            - Reduced the energy intensity of the production hall operation by 30%.
            - Reduced manufacturing scrap costs by 70% over three years.
    - **Trainee at Johnson Controls, Mladá Boleslav (2015 – 2016)**:
        - One-year trainee program, familiarization with the operations of various departments.
    """)

if my_radio == "Skills":
    st.subheader("Skills")
    st.write("**Languages**")
    st.progress(75)  # English (B2)

    st.write("**MS Office**")
    st.progress(90)  # Advanced knowledge

    st.write("**Programming**")
    st.progress(70)  # Python (Object-oriented programming), SQL

    st.write("**Data Analytics**")
    st.progress(85)  # Data collection and analysis, energy management systems

if my_radio == "Education & Training":
    st.subheader("Education & Training")
    with st.expander("Education"):
        st.write("""
        - M.Sc. in Analytical Chemistry, University of Pardubice (2013 – 2015)
        - B.Sc. in Clinical Biology and Chemistry, University of Pardubice (2010 – 2013)
        - Gymnázium Dobruška (2002 – 2010)
        """)
    with st.expander("Certifications"):
        st.write("""
        - European Energy Manager (2020)
        - Six Sigma Black Belt (2020)
        - Lean Implementer (2019)
        """)
    with st.expander("Courses"):
        st.write("""
        - Various courses in data analytics, programming (Python, SQL), and Excel VBA.
        - Generative AI and AI for all courses by IBM.
        """)

# Footer
st.write("---")
st.write("Made with ❤️ by Lucie Dubnová")