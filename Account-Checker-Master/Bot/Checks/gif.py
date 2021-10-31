import requests
import time
import json
from datetime import date
from message import Editmessage, Sendmessage, logger

bot_token = '2081531833:AAE5VzRAHOx-bjNll2xV6z_P4Gy-yBs73ow'
def gif_helper(chat_id, combo):

        url = 'https://api.giphy.com/v1/gifs/random?api_key=yCwQZFtE7k1VnI057XFTHN3sHG65cFky&tag='+combo
        get = requests.get(url).json()
        gif = get["data"]["image_original_url"]
        url2 = "https://api.telegram.org/bot{bot_token}/SendVideo?chat_id={chat_id}&video={gif}".format(bot_token=bot_token, chat_id=chat_id,gif=gif)
        send = requests.get(url2)
        