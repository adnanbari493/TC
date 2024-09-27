import streamlit as st
import random
import pandas as pd
import altair as alt

# Define job roles and their corresponding mock interview questions and case studies
job_roles = {
    "Software Engineer": {
        "questions": [
            "What is the difference between an array and a linked list?",
            "Explain the concept of Object-Oriented Programming (OOP).",
            "How does a binary search algorithm work?",
            "What is a RESTful API?",
            "Explain the CAP theorem."
        ],
        "case_study": "Design a scalable messaging system like WhatsApp."
    },
    "Product Manager": {
        "questions": [
            "How would you define a product roadmap?",
            "Describe a time when you had to make a critical decision based on limited data.",
            "How do you prioritize product features?",
            "What metrics would you use to track the success of a product?",
            "How do you handle conflicting stakeholder requirements?"
        ],
        "case_study": "Develop a go-to-market strategy for a new fintech app."
    },
    "Consultant": {
        "questions": [
            "What is a SWOT analysis?",
            "How would you approach a client with a declining market share?",
            "Describe your problem-solving process in consulting.",
            "What frameworks do you use for business analysis?",
            "How do you handle tight deadlines in consulting projects?"
        ],
        "case_study": "Help a client reduce operational costs by 15% within 12 months."
    },
    "Data Scientist": {
        "questions": [
            "Explain the bias-variance tradeoff in machine learning.",
            "What is the difference between supervised and unsupervised learning?",
            "How do you handle missing data in a dataset?",
            "What is cross-validation and why is it important?",
            "Describe a time when you used data to solve a business problem."
        ],
        "case_study": "Analyze customer churn data to identify key factors driving churn."
    },
    "Marketing Manager": {
        "questions": [
            "How would you design a marketing campaign for a new product launch?",
            "Explain the difference between inbound and outbound marketing.",
            "How do you measure the effectiveness of a marketing campaign?",
            "What is a customer persona and why is it important?",
            "Describe a time when you had to handle a PR crisis."
        ],
        "case_study": "Develop a marketing strategy to increase brand awareness for a new product."
    },
    "Operations Manager": {
        "questions": [
            "How do you manage supply chain disruptions?",
            "Explain the concept of lean manufacturing.",
            "How do you handle resource allocation in a large project?",
            "Describe a time when you implemented a process improvement.",
            "What KPIs do you use to measure operational efficiency?"
        ],
        "case_study": "Optimize the supply chain for a manufacturing company to reduce lead times."
    }
}

# Track user progress (mock-up example using pandas)
progress_data = pd.DataFrame({
    "Job Role": ["Software Engineer", "Product Manager", "Consultant", "Data Scientist", "Marketing Manager", "Operations Manager"],
    "Completed Questions": [3, 2, 4, 3, 1, 0],
    "Total Questions": [5, 5, 5, 5, 5, 5]
})

# Streamlit App Interface
st.title("SPJIMR Comprehensive Interview Preparation Platform")

# Sidebar for user input
st.sidebar.header("User Information")
name = st.sidebar.text_input("Enter your name")
role = st.sidebar.selectbox("Select your desired role", list(job_roles.keys()))

# Feedback Section
st.sidebar.header("Feedback Section")
user_feedback = st.sidebar.text_area("Any suggestions for improving the platform?")
if st.sidebar.button("Submit Feedback"):
    st.sidebar.success("Thank you for your feedback!")

# Main Content
if name and role:
    st.header(f"Welcome, {name}! You're preparing for a {role} interview.")
    
    # Mock Interview Questions
    st.subheader("Mock Interview Questions")
    st.write("Here are some sample interview questions:")
    selected_role = job_roles[role]["questions"]
    random.shuffle(selected_role)
    for i, question in enumerate(selected_role[:3]):  # Show 3 random questions at a time
        st.write(f"Question {i+1}: {question}")
    
    # Case Study
    st.subheader("AI-Generated Case Study")
    case_study = job_roles[role]["case_study"]
    st.write(f"Case Study: {case_study}")
    
    # Progress Tracking
    st.subheader("Your Progress")
    st.write("Track your interview preparation progress here:")
    
    # Show progress for selected role
    role_progress = progress_data[progress_data["Job Role"] == role]
    completed_questions = int(role_progress["Completed Questions"])
    total_questions = int(role_progress["Total Questions"])
    
    st.write(f"Completed Questions: {completed_questions}/{total_questions}")
    
    # Visualization of progress
    progress_chart = alt.Chart(progress_data).mark_bar().encode(
        x="Job Role",
        y="Completed Questions",
        color="Job Role"
    ).properties(
        width=600,
        height=400
    )
    
    st.altair_chart(progress_chart)
    
    # Allow user to mark progress
    if st.button("Mark as Completed"):
        st.success("Progress saved!")
    
    # Progress summary
    if completed_questions == total_questions:
        st.write(f"Congratulations, {name}! You have completed all the questions for {role}.")
    else:
        st.write(f"You have completed {completed_questions}/{total_questions} questions. Keep practicing!")

# Footer
st.write("---")
st.write("Developed by 4Sight Consulting Group | Powered by EKOSH Data")
