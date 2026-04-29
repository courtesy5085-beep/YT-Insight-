from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(comments):
    text = "\n".join(comments[:50])

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize audience opinion:\n{text}"}
        ]
    )

    return res.choices[0].message.content
