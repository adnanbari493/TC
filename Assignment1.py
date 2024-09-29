pip install openai
import streamlit as st
import random
import openai  # For GPT-4 API integration
import pandas as pd

# OpenAI API key (replace with your actual API key)
openai.api_key = "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"

# Sample interview performance metrics data (replace with actual data)
user_metrics = {
    "Total Interviews Completed": 5,
    "Average Score": 85,
    "Best Performance": "Software Engineer",
    "Areas of Improvement": "System Design, Time Management"
}

# Home Page with SPJIMR Logo and Metrics
def home_page():
    # Display SPJIMR logo
    st.image("https://www.spjimr.org/sites/default/files/inline-images/spjimr-logo.png", width=300)

    # Display user performance metrics
    st.header(f"Welcome back, {user_name}!")
    st.subheader("Your Interview Performance Metrics:")
    
    # Display metrics in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Interviews", value=user_metrics["Total Interviews Completed"])
    with col2:
        st.metric(label="Average Score", value=f"{user_metrics['Average Score']}%")
    with col3:
        st.metric(label="Best Performance", value=user_metrics["Best Performance"])
    
    # Areas of Improvement
    st.subheader(f"Focus Areas: {user_metrics['Areas of Improvement']}")
    st.write("Keep practicing to improve in these areas!")
    
# GPT-4 Integration for Conversational Feedback
def gpt4_conversation(domain):
    st.subheader(f"Let's start an interview session for: **{domain}**")
    
    # Initialize conversation interface
    user_input = st.text_input("Ask your interview question or respond here:")
    
    if user_input:
        # Call GPT-4 API to generate a response
        response = openai.Completion.create(
            engine="gpt-4", 
            prompt=f"Interview prep for {domain}. User asked: {user_input}. Respond accordingly.",
            max_tokens=150
        )
        
        # Extract and display the response
        st.write("**GPT-4's Response:**")
        st.write(response.choices[0].text.strip())

# Main App Logic
st.title("SPJIMR Interview Preparation Platform")

# Sidebar for user information
st.sidebar.header("User Information")
user_name = st.sidebar.text_input("Enter your name")
selected_page = st.sidebar.selectbox("Navigate to:", ["Home", "Interview Session"])

# Homepage with metrics and logo
if selected_page == "Home":
    home_page()

# GPT-4 Interactive Interview Session
elif selected_page == "Interview Session":
    st.sidebar.header("Domain Selection")
    selected_domain = st.sidebar.selectbox("Choose your domain", [
        "Software Engineer", 
        "Product Manager", 
        "Consultant", 
        "Data Scientist", 
        "Marketing Manager", 
        "Operations Manager"
    ])
    
    # Start the conversation with GPT-4
    gpt4_conversation(selected_domain)

# Footer
st.write("---")
st.write("Developed by 4Sight Consulting Group | Powered by GPT-4 and EKOSH Data")
