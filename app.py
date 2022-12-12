import os
import re
import datetime
from time import sleep
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from config import Envs, Credential
from duckduckgo_search import ddg
from dotenv import load_dotenv
load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
app_level_token = os.getenv("APP_LEVEL_TOKEN")
leetcode_channel_id = "C041BS3U4GY"

app = App(token=bot_token)

@app.message(re.compile(".*"))
def message_hello(message, say):
    # if message['user'] == "U03S846QDUM":
    #     say(f"<@{message['user']}>, tui nayok! Ay mair kha.")
    #     return

    text = message['text'].lower()
    if re.compile(r"^hi").match(text):
        say(f"Hey, <@{message['user']}>! What can I do for you?")
        return
    
    if re.compile(r"^how are you").match(text):
        say(f"I'm fine. Thank you.")
        return
    
    if re.compile(r"^help:").match(text):
        res = ''
        for x in ddg(text, max_results=3):
            res += f"{x['href']}\n"
        say(res)
        return
    
    if re.compile(r"^env:").match(text):
        if "ranks" in text.split():
            say(f"<@{message['user']}>! Acca Bhaiya, ekhon e diye dicci.\n")
            sleep(5)
            say("```" + Envs().get_ranks_env() + "```")
            return
        
        if "wegro" in text.split():
            say(f"<@{message['user']}>! Acca Bhaiya, ekhon e diye dicci.\n")
            sleep(5)
            say("```" + Envs().get_wegro_env() + "```")
            return
        
        say(f"<@{message['user']}>! Valo bujhi Nai Bhaiya, Abar bolen.\n")
        return
    
    if re.compile(r"^credential:").match(text):
        words = text.split()
        if "dev" in words and ("db" in words or "database" in words) and "sheba" in words:
            say(f"<@{message['user']}>! Acca Bhaiya, ekhon e diye dicci.\n")
            sleep(5)
            say("```" + Credential().get_sheba_dev() + "```")
            return
        
        say(f"<@{message['user']}>! Valo bujhi Nai Bhaiya, Abar bolen.\n")
        return

    say(f"Please, kindly elaborate your need.")
    

@app.command("/next")
def handle_next_command(ack, say, command):
    ack()
    if (command['channel_id'] != leetcode_channel_id):
        say(f"Wrong Channel!")
        return

    weekday = datetime.datetime.today().weekday() 
    if weekday == 0 or weekday == 6: # sunday, monday
        next_day = "Tuesday"
    elif weekday < 3: # tuesday, wednesday
        next_day = "Thursday"
    else:
        next_day = "Sunday"

    say(f"We will discuss the following problem next {next_day} at 3.00 PM. <!channel>\n\n{command['text']}")

@app.command("/discuss")
def handle_next_command(ack, say, command):
    ack()
    if (command['channel_id'] != leetcode_channel_id):
        say(f"Wrong Channel!")
        return

    say(f"We will discuss the last problem in 5 mins. Interested people, please come to room no. 3. <!channel>")

if __name__ == "__main__":
    SocketModeHandler(app, app_level_token).start()
