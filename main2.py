from typing import Final 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import telegram
import requests
import schedule
import time
import threading
import re
from datetime import datetime
from dataclasses import dataclass

ma=''
TOKEN: Final = '7663753275:AAFeMC5sGWk00mWgQHPTx-waGh64i3MLGR8'
BOT_USERNAME: Final = '@thuvien123bot'
bot = telegram.Bot(TOKEN)
chat_id = ''
class checkincode:
    def __init__(self, code, time):
        self.code = code
        self.time = time

    
pending=[]
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hello')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('xin code')

url = 'https://libcalendar.ntu.edu.sg/r/checkin'

async def checkin(text: str):
    payload = {
    "code": str,  
    }

    headers = {
        'Referer': 'https://libcalendar.ntu.edu.sg/r/checkin',
    }
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)

def extract_booking_time(message):
    # Regular expression to match the date and time format
    match = re.search(r'until (\d{1,2}:\d{2}\w{2} [A-Za-z]+, [A-Za-z]+ \d{1,2}, \d{4})', message)
    if match:
        time_str = match.group(1)
        # Convert the extracted string into a datetime object
        print(time_str)
        booking_time = datetime.strptime(time_str, "%I:%M%p %A, %B %d, %Y")
        return booking_time
    return None

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('đã nhận code, đợi tí để check code')
    ma = update.message.text
    current_timestamp = time.time()
    payload = {
    "code": update.message.text,  
    }

    headers = {
        'Referer': 'https://libcalendar.ntu.edu.sg/r/checkin',
    }
    response = requests.post(url, data=payload, headers=headers)
    
    await update.message.reply_text('oke')
    await update.message.reply_text(response.text)
    timestamp = extract_booking_time(response.text).timestamp()
    p1=checkincode(update.message.text,timestamp)
    pending.append(p1)
    delay = timestamp - current_timestamp
    if delay > 0:
        await update.message.reply_text(f"Checkin will be done in {delay//3600} hours")
        time.sleep(delay)
        response = requests.post(url, data=payload, headers=headers)
        await update.message.reply_text("Your checkin has been done")
    else:
        await update.message.reply_text("The booking time has already passed!")

async def pending_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cnt = 0
    for code in pending:
        cnt = cnt+1
        await update.message.reply_text(f"code number {cnt}:")
        await update.message.reply_text(f"Code: {code.code}") 
        await update.message.reply_text(f"Remain time:{code.time/3600} hour(s)")

def prcocess_code():
    while True:
        
        for code in pending:
            current_timestamp = time.time()
            if(current_timestamp>code.time):
                checkin(code.code)
        time.sleep(300)


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('pending',pending_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.run_polling(poll_interval=3)
