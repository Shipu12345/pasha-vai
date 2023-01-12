import os
import openai
import wandb
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("CHAT_GPT_KEY")

def get_chatGPT_result(gpt_prompt="Write a basic bfs in python"):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    answer_text = gpt_prompt + ':\n' + response['choices'][0]['text']
    return answer_text
