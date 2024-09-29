import streamlit as st
import pandas as pd
import altair as alt

# Sample data for performance graph and feedbacks
performance_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    "Score": [60, 75, 80, 85, 90, 88, 95]
}

feedbacks = [
    "Improve your problem-solving skills.",
    "Work on time management during interviews.",
    "Focus more on system design.",
    "Good job on explaining your thought process!",
    "Work on communication skills in technical discussions."
]

areas_to_improve = [
    "System Design", "Communication", "Problem-Solving", "Time Management", "Technical Knowledge"
]

# Streamlit app starts here
st.title("Interactive Interview Preparation Dashboard")

# Sidebar for selecting Job Role
st.sidebar.header("Job Role Selection")
job_roles = ["Software Engineer", "Product Manager", "Consultant", "Data Scientist", "Marketing Manager", "Operations Manager"]
selected_role = st.sidebar.selectbox("Select your interview role:", job_roles)

# Dropdown to select Case Study Practice
st.sidebar.header("Case Study Practice")
case_study_practice = {
    "Software Engineer": "Design a scalable file storage system like Google Drive.",
    "Product Manager": "Develop a product roadmap for a new e-commerce platform.",
    "Consultant": "Help a retail client reduce operational costs by 20%.",
    "Data Scientist": "Analyze customer churn data and create a predictive model.",
    "Marketing Manager": "Plan a marketing strategy to increase brand awareness for a new product.",
    "Operations Manager": "Optimize the supply chain process for a manufacturing company."
}
selected_case_study = st.sidebar.selectbox("Choose a case study:", list(case_study_practice.values()))

# Main Dashboard Sections
st.header(f"Welcome to your Interview Dashboard, focused on {selected_role}")

# 1. Earlier Feedback Section
st.subheader("Earlier Feedback")
for feedback in feedbacks:
    st.write(f"- {feedback}")

# 2. Performance Graph
st.subheader("Performance Overview")
performance_df = pd.DataFrame(performance_data)
chart = alt.Chart(performance_df).mark_line(point=True).encode(
    x="Month",
    y="Score",
    tooltip=["Month", "Score"]
).interactive()

st.altair_chart(chart, use_container_width=True)

# 3. Areas to Improve
st.subheader("Areas to Improve")
st.write(", ".join(areas_to_improve))

# 4. Interactive Chatbot (dummy implementation for now)
st.subheader("Interactive Chat Bot")
user_input = st.text_input("Ask a question or type your interview response here:")
if user_input:
    st.write(f"**Chatbot Response**: I received your input '{user_input}'. More sophisticated responses will be available when connected to an AI model.")

# Additional Feature: Resource Links for Interview Prep
st.subheader("Additional Resources")
st.markdown("""
- [LeetCode](https://leetcode.com) - Practice coding problems
- [Glassdoor](https://www.glassdoor.com) - Look up interview questions for various companies
- [System Design Primer](https://github.com/donnemartin/system-design-primer) - Learn about system design
""")

# Display selected Case Study for Practice
st.subheader("Selected Case Study for Practice")
st.write(f"**{selected_case_study}**")

# 5. Progress Overview (Optional)
st.subheader("Progress Overview")
st.write("Your progress over the months:")
progress_data = {
    "Total Interviews Completed": 15,
    "Average Score": 88,
    "Best Performance": "Software Engineer",
    "Focus Areas": "System Design and Communication"
}

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Interviews", progress_data["Total Interviews Completed"])
col2.metric("Average Score", f"{progress_data['Average Score']}%")
col3.metric("Best Performance", progress_data["Best Performance"])
col4.metric("Focus Areas", progress_data["Focus Areas"])
