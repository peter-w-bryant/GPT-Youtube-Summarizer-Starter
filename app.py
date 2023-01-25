from flask import Flask, render_template, request
import json
import requests
import config
import openai
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
app.secret_key = config.secret_key

'''
Simple index page with a form to enter a YouTube video URL.
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

'''
Summarize a YouTube video using GPT-3, and return the summary as a JSON response.
'''
@app.route("/summarize", methods=["POST"])
def summarize():
    # Get YouTube API key
    youtube_api_key = config.youtube_API_key

    # Get video URL from request
    url = request.form["url"]

    # Extract video ID from URL
    video_id = url.split("v=")[1]

    # Make request to YouTube API to get video details
    api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={youtube_api_key}"
    r = requests.get(api_url)
    video_data = r.json()
    with open('search_cache.json', 'w') as json_file:
        json.dump(video_data, json_file)

    # Extract video title and description
    title = video_data["items"][0]["snippet"]["title"]
    # description = video_data["items"][0]["snippet"]["description"]
    
    # Extract video transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id) 

    # Full transcript string
    transcript_str = ""
    for line in transcript:
        # Break if transcript exceeds 2048 tokens (max context length for text-davinci-002)
        if (len(transcript_str.strip()) + len(line["text"] + " ") + config.max_tokens) <= config.model_max_tokens:
            transcript_str += line["text"] + " "
        else:
            break

    # Initialize OpenAI API key
    openai.api_key = config.openai_API_key

    # Create prompt for GPT-3
    gpt3_prompt = (
        f"Summarize the video {title} with the following transcript: {transcript_str}"
    )
    
    # Generate summary with GPT-3
    completions = openai.Completion.create(
        engine=config.model,
        prompt=gpt3_prompt,
        max_tokens=config.max_tokens,
        n=1,
        stop=None,
        temperature=config.temperature,
    )

    # Extract summary from completions
    summary = completions.choices[0].text

    # # Return summary as JSON response
    return {"summary": summary}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
