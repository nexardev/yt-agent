from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)
        full_text = " ".join([t.text for t in transcript])
        return {"video_id": video_id, "transcript": full_text}
    except Exception as e:
        return {"error": str(e)}
