# GPT-Youtube-Summarizer-Starter
A quick-start Flask app for anyone looking to generate YouTube video summaries using OpenAI's GPT models.

## Usage
This project is meant to be bare-bones to assist anyone looking to create an application that uses OpenAI's GPT models to summarize YouTube videos. 

To run the application as is, you need to,

1. Clone the repository
`git clone https://github.com/peter-w-bryant/GPT-Youtube-Summarizer-Starter.git`

2. Create an OpenAI and YouTube API key and assign them in the `config.py` file.

3. Further modify the bottom of the `config.py` file with youir desired models settings. By default I am using, the `text-davinci-002` model for text generation with
the maximum generated tokens set to `50` and the temperature for sampling set to `0.5`, feel free to change these as you see fit!
