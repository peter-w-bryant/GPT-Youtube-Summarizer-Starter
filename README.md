# GPT-Youtube-Summarizer-Starter
A quick-start Flask app for anyone looking to generate YouTube video summaries using OpenAI's GPT models.

## Usage
This project is meant to be bare-bones to assist anyone looking to create an application that uses OpenAI's GPT models to summarize YouTube videos. 

To run the application as is, you need to,

1. Clone the repository

```{bash}
git clone https://github.com/peter-w-bryant/GPT-Youtube-Summarizer-Starter.git
```

2. Create an OpenAI and YouTube API key and assign them in the `config.py` file.

3. Further modify the bottom of the `config.py` file with your desired models settings. By default I am using, the `text-davinci-002` model for text generation with
the maximum generated tokens set to `50` and the temperature for sampling set to `0.5`, feel free to change these as you see fit!

4. If you have properly taken care of #2 and #4, you can install all dependencies and run the Flask application with,

```{bash}
pip install -r requirements.txt
python3 app.py
```

This should start a development server, at which point you can go to `http://127.0.0.1:8000` in your browser where you will see a very simple HTML page for submitting a YouTube URL. 

![index](https://user-images.githubusercontent.com/72423203/214469179-5ff483d1-593f-4c6b-9eca-d90e707844e2.png)

If you submit a full URL to a YouTube video of your choice and hit summarize, you will return a JSON response at the `http://127.0.0.1:8000/summarize` route that looks like,

```
{
  "summary": "Summary text of length max tokens."
}
```

Please feel free to modify this application to your own project needs!

## Example Output
As an example, when passed the URL of [Key & Peele's infamous Substitute Teacher skit](https://www.youtube.com/watch?v=Dd7FixvoKBw), the following JSON was returned,

```
{
  "summary": "The video is about a substitute teacher who is taking attendance and gets frustrated when the students don't say their names correctly. He threatens to send one student, Aaron, to the principal's office for not pronouncing his name correctly."
}
```
