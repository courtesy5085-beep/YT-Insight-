import streamlit as st
from utils.youtube_api import get_video_data
from utils.comments import get_comments
from utils.sentiment import sentiment_analysis
from utils.nlp import extract_keywords
from utils.openai_utils import summarize
from utils.pdf_generator import generate_pdf
import re

st.set_page_config(page_title="YT Insight Pro", layout="wide")

st.title("🎥 YT Insight Pro")

url = st.text_input("Paste YouTube URL")

def extract_video_id(url):
    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    return match.group(1) if match else None

if st.button("Analyze"):
    video_id = extract_video_id(url)

    if not video_id:
        st.error("Invalid URL")
    else:
        with st.spinner("Analyzing video..."):
            meta = get_video_data(video_id)
            comments = get_comments(video_id)

            sentiment = sentiment_analysis(comments)
            keywords = extract_keywords(comments)
            summary = summarize(comments)

            engagement = (meta["likes"] + len(comments)) / meta["views"]

        st.subheader(meta["title"])
        st.image(meta["thumbnail"])

        col1, col2, col3 = st.columns(3)
        col1.metric("Views", meta["views"])
        col2.metric("Likes", meta["likes"])
        col3.metric("Engagement", round(engagement, 4))

        st.subheader("Sentiment")
        st.write(sentiment)

        st.subheader("Top Keywords")
        st.write(list(keywords))

        st.subheader("AI Summary")
        st.write(summary)

        if st.button("Export PDF"):
            filename = f"report_{video_id}.pdf"
            generate_pdf({**meta, "summary": summary}, filename)
            with open(filename, "rb") as f:
                st.download_button("Download PDF", f, file_name=filename)
