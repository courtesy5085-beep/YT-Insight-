from googleapiclient.discovery import build
import os

def get_video_data(video_id):
    youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))

    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=video_id
    )
    response = request.execute()

    item = response["items"][0]

    return {
        "title": item["snippet"]["title"],
        "channel": item["snippet"]["channelTitle"],
        "published": item["snippet"]["publishedAt"],
        "description": item["snippet"]["description"],
        "tags": item["snippet"].get("tags", []),
        "views": int(item["statistics"]["viewCount"]),
        "likes": int(item["statistics"].get("likeCount", 0)),
        "comments": int(item["statistics"].get("commentCount", 0)),
        "thumbnail": item["snippet"]["thumbnails"]["high"]["url"]
    }
