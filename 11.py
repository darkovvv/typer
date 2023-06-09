import random
import pickle
import asyncio
from pyrogram import Client, filters
from time import sleep
from random import shuffle
from pyrogram.types import ChatPermissions
from pyrogram.errors import FloodWait
import textwrap
import os
import json
import pickle
import time
from math import ceil

if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
	
app = Client('admin', api_id=18413850, api_hash='598aac24b5cf0a1b4632485f5f33c4c7')
	
def parting(xs, parts):
    part_len = ceil(len(xs)/parts)
    return [xs[part_len*k:part_len*(k+1)] for k in range(parts)]

def parting(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

@app.on_message(filters.command('adduser', prefixes='.') & filters.me)
def adduser(_, message):
    id = message.text.split('.adduser ')[1]
    if '@' in id:
        id = app.get_users(id).id

        with open('userlist.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{id}\n')

        message.edit(f'{id} добавлен!')

    else:
        try:
            with open('userlist.txt', 'a+', encoding='utf-8') as file:
                file.write(f'{int(id)}')

            message.edit(f'{id} добавлен!')
        except:
            message.edit('ID может быть числом или пингом!')

@app.on_message(filters.command('deluser', prefixes='.') & filters.me)
def deluser(_, message):
    id = message.text.split('.deluser ')[1]

    if '@' in id:
        id = app.get_users(id).id

    with open('userlist.txt', 'r', encoding='utf-8') as file:
        allids = file.read().splitlines()
        if str(id) in allids:
            allids.remove(str(id))

            open('userlist.txt', 'w').close()
            with open('userlist.txt', 'a', encoding='utf-8') as file:
                for idtowrite in allids:
                    file.write(f'{int(idtowrite)}\n')

            message.edit(f'{id} удалён!')
        else:
            message.edit(f'{id} не существует!')

@app.on_message(filters.command('id', prefixes='.') & filters.me)
def id(_, message):
    message.edit(f'ID = {message.reply_to_message.from_user.id}')

@app.on_message(filters.text)
def reply(_, message):
    with open('userlist.txt', 'r+', encoding='utf-8') as file:
        usertoreply = file.read().splitlines()
        kew = ["1"]
        kew1 = random.choice(kew)
        
    if str(message.from_user.id) in usertoreply:
        with open('нон-стоп.txt', 'r+', encoding='utf-8') as file:
            if kew1 in "1":
                alljokes = file.read().splitlines()
                randomjoke = random.choice(alljokes)
                message.reply(randomjoke)
                
        
print('хуй залупа')
app.run()