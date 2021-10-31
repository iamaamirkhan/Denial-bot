import logging
from telegram import Bot
import os

from telegram.files.video import Video

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

bot_token = os.environ.get('2081531833:AAE5VzRAHOx-bjNll2xV6z_P4Gy-yBs73ow')
bot = Bot('2081531833:AAE5VzRAHOx-bjNll2xV6z_P4Gy-yBs73ow')

def Sendmessage(chat_id, text,reply_markup=None):
    try:
        message = bot.send_message(chat_id=chat_id, text=text, reply_to_message_id=None,parse_mode="HTML", reply_markup=reply_markup)
        msg_id = message.message_id
        return msg_id
    except Exception as e:
        logger.info(e)
        raise UserWarning


def Editmessage(chat_id, text, msg_id, reply_markup=None):
    try:
        bot.edit_message_text(chat_id=chat_id, text=text, message_id=msg_id,parse_mode="HTML", reply_markup=reply_markup)
    except Exception as e:
        logger.info(e)
