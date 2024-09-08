from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2

# Load environment variables
load_dotenv()

# Configure Google API key for Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Define a function to get the response from the Gemini model
def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

# Define a function to read the content of a PDF file
def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

# Example input prompt for the Gemini model
input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing 
Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App 
Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, 
Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX 
Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess 
resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial 
in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD 
(Job Description) and meticulously identify any missing keywords with utmost accuracy.

resume:{text}
description:{jd}

I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the title for all the three sections.
While generating the response put some space to separate all the three sections.
"""

# Streamlit UI
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .hero {
            position: relative;
            background: url('https://images.pexels.com/photos/3183197/pexels-photo-3183197.jpeg') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
            padding: 100px 0;
        }
        .hero::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1;
        }
        .hero h1, .hero p {
            z-index: 2;
            position: relative;
            color: white;
        }
        .hero h1 {
            font-size: 3em;
            font-weight: bold;
            margin-top: 0;
        }
        .hero p {
            font-size: 1.5em;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <h1>CareerCraft</h1>
        <p>Navigate the Job Market with Confidence!</p>
    </div>
""", unsafe_allow_html=True)

avs.add_vertical_space(10)

# Features Section
col1, col2 = st.columns([3, 2])
with col2:
    st.header("Wide Range of Offerings")
    st.write('ATS-Optimized Resume Analysis')
    st.write('Resume Optimization')
    st.write('Skill Enhancement')
    st.write('Career Progression Guidance')
    st.write('Tailored Profile Summaries')
    st.write('Streamlined Application Process')
    st.write('Personalized Recommendations')
    st.write('Efficient Career Navigation')

with col1:
    st.image('https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg', use_column_width=True)

avs.add_vertical_space(10)

# Career Adventure Section
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_response(input_prompt)
            st.subheader(response)

with col2:
    st.image('https://images.pexels.com/photos/3184306/pexels-photo-3184306.jpeg', use_column_width=True)

avs.add_vertical_space(10)

# FAQ Section
st.markdown("""
    <style>
        .faq {
            background-color: #f8f9fa;
            padding: 50px 0;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .faq h1 {
            font-size: 2.5em;
            text-align: center;
            color: #007BFF;
            margin-bottom: 30px;
        }
        .faq-item {
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin: 10px auto;
            max-width: 800px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .faq-item .question {
            font-weight: bold;
            font-size: 1.2em;
            color: #333;
            margin-bottom: 10px;
        }
        .faq-item .answer {
            font-size: 1em;
            color: #555;
        }
    </style>
    <div class="faq">
        <h1>FAQ</h1>
        <div class="faq-item">
            <div class="question">How does CareerCraft analyze resumes and job descriptions?</div>
            <div class="answer">CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.</div>
        </div>
        <div class="faq-item">
            <div class="question">Can CareerCraft suggest improvements for my resume?</div>
            <div class="answer">Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.</div>
        </div>
        <div class="faq-item">
            <div class="question">Is CareerCraft suitable for both entry-level and experienced professionals?</div>
            <div class="answer">Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

avs.add_vertical_space(10)