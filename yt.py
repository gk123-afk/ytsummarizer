import google.generativeai as genai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

st.title('YouTube Video Summarization')


genai.configure(api_key=st.secrets["google_api_key"])
model = genai.GenerativeModel('gemini-2.0-flash')

video = st.text_input("Enter Video Link")
word=st.selectbox("How many words?",(100, 200,500),)
languages = ['hi', 'en']
option = st.selectbox(
    "Please choose summary language",
    ("English", "Hindi"),
)


def vid(video):
    video1 = video[17:28]
    return video1

def getts(video):
    transcript_text = YouTubeTranscriptApi.get_transcript(vid(video),languages)
    ts = ""
    for i in transcript_text:
        ts += " " + i["text"]
    return ts

try:
    
    if st.button('Summary'):
       
       transcript = getts(video)
       prompt = f"""
       You are an expert linguist, who is good at summarizing the content.
       Help me summarize the content into: {word}words in {option}.

       ``` 
       {transcript}
       ```
       """
       response = model.generate_content(prompt)
       st.success(f"{response.text}.")
except Exception as e:
    print(f"An error occurred: {e}")
st.write("**How to share the link???**")
st.image("image copy.png",caption="click on the share button",width=500)
st.image("image.png",caption="copy the link and paste it",width=600)    