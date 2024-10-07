import streamlit as st
import pandas as pd

# Insert SPJIMR logo
st.image("https://upload.wikimedia.org/wikipedia/en/thumb/0/03/S._P._Jain_Institute_of_Management_and_Research_logo.svg/1920px-S._P._Jain_Institute_of_Management_and_Research_logo.svg.png", width=300)

# Sample data for pre-reads
pre_reads_data = {
    "Class Date": ["12th October 2024", "15th October 2024", "18th October 2024"],
    "Topic": ["AI in Business", "Design Thinking", "Blockchain Technology"],
    "Pre-read Link": [
        "https://www.example.com/ai-pre-read",
        "https://www.example.com/design-thinking-pre-read",
        "https://www.example.com/blockchain-pre-read"
    ]
}

# Store student queries to display to the faculty
student_queries = []

# Streamlit app starts here
st.title("SPJIMR Pre Class Work Preparation Platform")

# Insert SPJIMR logo
st.image("https://upload.wikimedia.org/wikipedia/commons/3/37/SPJIMR_Mumbai_Logo.png", width=300)

# Sidebar for selecting the class topic
st.sidebar.header("Upcoming Class Topics")
class_topics = ["AI in Business", "Design Thinking", "Blockchain Technology"]
selected_topic = st.sidebar.selectbox("Select the topic for pre-class preparation:", class_topics)

# Display the selected pre-read information
st.header(f"Pre-Read Material for {selected_topic}")
pre_reads_df = pd.DataFrame(pre_reads_data)
selected_pre_read = pre_reads_df[pre_reads_df['Topic'] == selected_topic]

# Show the pre-read link
if not selected_pre_read.empty:
    pre_read_link = selected_pre_read["Pre-read Link"].values[0]
    st.write(f"Please read the material before the next class: [Pre-Read for {selected_topic}]({pre_read_link})")

# Interactive Chatbot Section
st.subheader("Have questions on the Pre-Read?")
user_input = st.text_input("Ask a question about the pre-read:")
if user_input:
    st.write(f"**Chatbot Response**: I received your question: '{user_input}'. A detailed response will be available when connected to an AI model.")
    student_queries.append({"Topic": selected_topic, "Question": user_input})

# Display student queries to the faculty
if st.sidebar.checkbox("Show student queries (for faculty only)", False):
    st.sidebar.subheader("Questions asked by students:")
    if student_queries:
        for idx, query in enumerate(student_queries):
            st.sidebar.write(f"{idx + 1}. [{query['Topic']}] - {query['Question']}")
    else:
        st.sidebar.write("No queries yet.")

# Faculty Upload Section (for faculty to upload pre-reads)
st.sidebar.subheader("Faculty: Upload Pre-Reads")
uploaded_file = st.sidebar.file_uploader("Upload Pre-Read (PDF/DOCX)", type=["pdf", "docx"])
if uploaded_file is not None:
    st.sidebar.success(f"Successfully uploaded: {uploaded_file.name}")

# Additional Feature: Resource Links for Class Preparation
st.subheader("Additional Resources")
st.markdown("""
- [Harvard Business Review](https://hbr.org) - Articles on management practices
- [MIT Technology Review](https://www.technologyreview.com) - Stay updated with emerging technologies
- [Coursera](https://www.coursera.org) - Explore courses related to class topics
""")

# Progress Overview (Optional)
st.subheader("Student Progress Overview")
progress_data = {
    "Total Pre-Reads Completed": 8,
    "Average Quiz Score": 92,
    "Most Engaged Topic": "Design Thinking",
    "Focus Areas": "AI and Blockchain"
}

col1, col2, col3, col4 = st.columns(4)
col1.metric("Pre-Reads Completed", progress_data["Total Pre-Reads Completed"])
col2.metric("Average Quiz Score", f"{progress_data['Average Quiz Score']}%")
col3.metric("Most Engaged Topic", progress_data["Most Engaged Topic"])
col4.metric("Focus Areas", progress_data["Focus Areas"])
