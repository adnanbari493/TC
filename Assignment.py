
import streamlit as st
import random

# Sample interview questions (Replace with AI-generated questions later)
mock_questions = {
    "Software Engineer": [
        "What is the difference between an array and a linked list?",
        "Explain the concept of OOP.",
        "How does a binary search work?"
    ],
    "Product Manager": [
        "How would you define a product roadmap?",
        "Describe a time when you had to make a critical decision based on limited data.",
        "How do you prioritize product features?"
    ],
    "Consultant": [
        "What is a SWOT analysis?",
        "How would you approach a client with a declining market share?",
        "Describe your problem-solving process in consulting."
    ]
}

# Personalized feedback mockup
def generate_feedback(role):
    feedback_options = {
        "Software Engineer": [
            "Improve your understanding of data structures.",
            "Work on optimizing algorithms for better performance."
        ],
        "Product Manager": [
            "Focus on improving market analysis.",
            "Enhance your decision-making framework."
        ],
        "Consultant": [
            "Refine your consulting frameworks.",
            "Improve your problem-solving approach."
        ]
    }
    return random.choice(feedback_options.get(role, ["Keep practicing!"]))

# Sample case study generator
def generate_case_study(role):
    case_studies = {
        "Software Engineer": "Design a scalable messaging system like WhatsApp.",
        "Product Manager": "Develop a go-to-market strategy for a new fintech app.",
        "Consultant": "Help a client reduce operational costs by 15% within 12 months."
    }
    return case_studies.get(role, "No case study available.")

# Streamlit App Interface
st.title("SPJIMR Interview Preparation Platform MVP")

st.sidebar.header("User Information")
name = st.sidebar.text_input("Enter your name")
role = st.sidebar.selectbox("Select your desired role", ["Software Engineer", "Product Manager", "Consultant"])

st.sidebar.header("Feedback Section")
st.sidebar.text_area("Any suggestions for improving the platform?")

if name and role:
    st.header(f"Welcome, {name}!")
    
    # Step 1: Interview Practice
    st.subheader("Mock Interview Questions")
    question = random.choice(mock_questions.get(role, []))
    st.write(f"Question: {question}")
    
    # Step 2: Case Study
    st.subheader("AI-Generated Case Study")
    case_study = generate_case_study(role)
    st.write(f"Case Study: {case_study}")
    
    # Step 3: Feedback
    st.subheader("Personalized Feedback")
    feedback = generate_feedback(role)
    st.write(f"Feedback: {feedback}")

# Progress Dashboard Placeholder
st.subheader("Your Progress")
st.write("Track your interview practice and case studies here. (Feature in development)")

# Footer
st.write("---")
st.write("Developed by 4Sight Consulting Group | Powered by EKOSH Data")


