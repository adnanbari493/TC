import streamlit as st
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import googleapiclient.discovery

streamlit
selenium
webdriver-manager
requests
beautifulsoup4
pandas
google-auth
google-auth-oauthlib
google-auth-httplib2
googleapiclient

# --- STREAMLIT UI ---
st.title("📊 Real-Time YouTube Views Tracker")
st.write("Track live YouTube views from Datamuni or YouTube API.")

# --- USER INPUT ---
video_id = st.text_input("Enter YouTube Video ID", "dQw4w9WgXcQ")  # Example Video ID
data_source = st.radio("Select Data Source", ("Datamuni (Scraping)", "YouTube API (Recommended)"))

# --- FUNCTION TO SCRAPE DATAMUNI ---
def scrape_datamuni():
    url = "https://www.datamuni.com/youtube/"  # Change to actual Datamuni link
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without opening a browser
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service("chromedriver.exe")  # Change path to chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(5)  # Wait for JavaScript to load

    try:
        views_element = driver.find_element(By.CLASS_NAME, "real-time-views")  # Modify this if needed
        real_time_views = views_element.text.strip()
    except:
        real_time_views = "Not Found"

    driver.quit()
    return real_time_views

# --- FUNCTION TO FETCH VIEWS FROM YOUTUBE API ---
def fetch_youtube_api(video_id):
    api_key = "YOUR_YOUTUBE_API_KEY"  # Replace with your API key
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    try:
        response = youtube.videos().list(part="liveStreamingDetails", id=video_id).execute()
        views = response["items"][0]["liveStreamingDetails"]["concurrentViewers"]
        return f"{views} views/min"
    except Exception as e:
        return "Error fetching data"

# --- SHOW REAL-TIME VIEWS ---
if st.button("Get Real-Time Views"):
    if data_source == "Datamuni (Scraping)":
        views = scrape_datamuni()
    else:
        views = fetch_youtube_api(video_id)

    st.metric(label="📈 Real-Time Views", value=views)

# --- AUTO UPDATE EVERY 60 SECONDS ---
st.write("Auto-refresh enabled: Updates every 60 seconds")
placeholder = st.empty()

while True:
    if data_source == "Datamuni (Scraping)":
        views = scrape_datamuni()
    else:
        views = fetch_youtube_api(video_id)

    placeholder.metric(label="📈 Real-Time Views", value=views)
    time.sleep(60)  # Refresh every 60 seconds
