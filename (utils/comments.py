from googleapiclient.discovery import build
import os

def get_comments(video_id, max_results=200):
    youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))

    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )

    response = request.execute()

    for item in response["items"]:
        text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(text)

    return comments[:max_results]
