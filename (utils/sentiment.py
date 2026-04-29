from textblob import TextBlob

def sentiment_analysis(comments):
    pos, neg, neu = 0, 0, 0

    for c in comments:
        polarity = TextBlob(c).sentiment.polarity
        if polarity > 0:
            pos += 1
        elif polarity < 0:
            neg += 1
        else:
            neu += 1

    return {
        "positive": pos,
        "negative": neg,
        "neutral": neu
    }
