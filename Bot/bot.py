from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
from Checks.Altbalaji import altbalaji_helper
from Checks.hoichoi import hoichoi_helper
from Checks.voot import Voot_helper
from Checks.zee5 import zee_helper
from Checks.ass import bin_helper
from Checks.gif import gif_helper
from Miscellaneous.Scraper import pastebin, text_scraper, throwbin
import os


bot_token = '2081531833:AAE5VzRAHOx-bjNll2xV6z_P4Gy-yBs73ow'
startmessage = [
    
    [
        InlineKeyboardButton(text="Developer 👨‍💻", url="t.me/GravityZR"),
        InlineKeyboardButton(text="Channel 📢", url="t.me/Makepossiblex"

        ),
    ],
]


def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    userid= info['username']
    text = f'<i>Welcome @{userid}, I am Denial Python Base Check Bot - I can help you to check accounts, cc, For Commands Use /help</i>\n<b>Made By @GravityZR</b>'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return

    
def combos_spilt(combos):
    split = combos.split('\n')
    return split


def help(update, context):
    chat_id = update.message.chat_id
    text = "<b>Commands\n \n«——»Accounts«——»\n\nFor Albalaji  Use- !alt - your combo\nFor Voot Use- !vot - your combo\nFor Zee5 Use- !zee - your combo\nFor Hoichoi Use- !hoi - your combo\n«——»Accounts«——»\nFor Bin Check Use- !bin - your bin\nFor Gifs Use- !gif - text\n\nMore Tools Coming Soon!</b>"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))

def duty(update, context):
    chat_id = update.message.chat_id
    text =  update.message.text.split(' ', 1)
    if text[0] == '!alt':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                altbalaji_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            altbalaji_helper(chat_id, text[1])
    elif text[0] == '!vot':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                Voot_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            Voot_helper(chat_id, text[1])
    elif text[0] == '!hoi':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                hoichoi_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            hoichoi_helper(chat_id, text[1])
    elif text[0] == '!zee':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                zee_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            zee_helper(chat_id, text[1])
    elif text[0] == '!bin':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                bin_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            bin_helper(chat_id, text[1])
    elif text[0] == '!gif':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                gif_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            gif_helper(chat_id, text[1])
    elif text[0] == '!pst':
            try:
                throwbin(chat_id, text[1])
            except IndexError:
                Sendmessage(chat_id, "<i>Somethings wrong with your format!</i>")
    else:
        logger.info('Unknown Command')


def scraperdfnc(update, context):
    msg = update.message.text
    status_msg = update.message
    chat_id = status_msg.chat_id
    try:
        if 'pastebin' in msg:
            link = msg.split(' ')[1]
            pastebin(chat_id,link)
        elif 'ghostbin' in msg:
            link = msg.split(' ')[1]
            ghostbin(chat_id,link)
        else:
            scrape_text = status_msg['reply_to_message']['text']
            text_scraper(chat_id, scrape_text)
    except:
        Sendmessage(chat_id, 'Only Supports pastebin, please check if you send paste bin link')

def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("scrape", scraperdfnc))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
