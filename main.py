import configparser
import json
import time

from parse_message import parse_message

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, int(api_id), api_hash)

client.start()
url = "https://t.me/python_cool"
# url = "https://t.me/shaman_channel"


async def get_last_message(channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0    # номер записи, с которой начинается считывание
    limit_msg = 1   # максимальное число записей, передаваемых за один раз

    all_messages = []   # список всех сообщений
    total_messages = 0
    total_count_limit = 0  # поменяйте это значение, если вам нужны не все сообщения

    messages = ''

    while True:
        history = await client(GetHistoryRequest(
            peer=channel,
            offset_id=offset_msg,
            offset_date=None, add_offset=0,
            limit=limit_msg, max_id=0, min_id=0,
            hash=0))
        messages = history.messages
        for i in messages:
            with open('last_post.txt', 'r') as f:
                lp = int(f.read())
            if i.id > lp:
                await parse_message(i, url)
        time.sleep(60)



async def main():
    channel = await client.get_entity(url)
    #print(channel)
    #await dump_all_participants(channel)
    await get_last_message(channel)


with client:
    client.loop.run_until_complete(main())
