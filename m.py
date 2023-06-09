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

if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

def parting(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

#соси быстро
@app.on_message(filters.command("sosi", prefixes=".") & filters.me)
def past(_, message):
    message.delete()

    with open('соси.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            if line != "":
                time.sleep(0.6)
                app.send_message(message.chat.id, line)
                
#отозвись
@app.on_message(filters.command("отзовись", prefixes=".") & filters.me)
def past(_, message):
    message.delete()

    with open('ot.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            if line != "":
                time.sleep(0.2)
                app.send_message(message.chat.id, line)

#mq
@app.on_message(filters.command("mq1", prefixes=".") & filters.me)
def past(_, message):
    message.delete()

    with open('mq1.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            if line != "":
                time.sleep(0.8)
                app.send_message(message.chat.id, line)

#паста хуяста
@app.on_message(filters.command("пасты", prefixes=".") & filters.me)
def past(_, message):
    alreadyUse = []
    message.delete()

    with open('пасты.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        
    jokescouht = len(lines)

    try:
        count = int(message.text.split()[1])
    except:
        count = None


    if count:
        if not count > jokescouht:
            for number in range(count):
                while True:
                    word = random.choice(lines)
                    if not word in alreadyUse:
                        app.send_message(message.chat.id, f'{word}')
                        sleep(0.8)
                        alreadyUse.append(word)
                        break
        else:
            app.send_message(message.chat.id, f'ты че ебанутый? у меня есть только {jokescouht}')
    else:
        word = random.choice(lines)
        app.send_message(message.chat.id, word)

#паста хуяста
@app.on_message(filters.command("ср", prefixes=".") & filters.me)
def past(_, message):
    alreadyUse = []
    message.delete()

    with open('ср.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        
    jokescouht = len(lines)

    try:
        count = int(message.text.split()[1])
    except:
        count = None


    if count:
        if not count > jokescouht:
            for number in range(count):
                while True:
                    word = random.choice(lines)
                    if not word in alreadyUse:
                        app.send_message(message.chat.id, f'{word}')
                        sleep(0.6)
                        alreadyUse.append(word)
                        break
        else:
            app.send_message(message.chat.id, f'ты че ебанутый? у меня есть только {jokescouht}')
    else:
        word = random.choice(lines)
        app.send_message(message.chat.id, word)

#помощь нахуй
@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(_, message):
    message.delete()
    app.send_message(message.chat.id, HELP)

#нью паста
@app.on_message(filters.command("add", prefixes=".") & filters.me)
def add(_, message):
    message.delete()
    newJoke = message.text.split('.add ')[1]
    with open('пасты.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{newJoke}')
    message.edit('успешно!')
    time.sleep(1)
    message.delete()
	
#рандомайзер
@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(_, msg):
	random_number = str(random.randint(0, int(msg.command[1])))
	msg.edit(roi + random_number)



too = random.randint(0, 100)
roi = f'<b> случайное число: </b>'

	 # Шаблон текста в строчки
@app.on_message(filters.command("нсп", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	я
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	выебал
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	твою
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	маму
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	сын
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	свиноматки
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ебливой
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	терпишь мой нон-стоп
	''')
	
		 # Шаблон текста в строчки 1
@app.on_message(filters.command("нсп1", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	где
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	отпор
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	семихуюлинское
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	отребье
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	этой
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	конференции
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	в которую
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	сто
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	раз
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	нахаркали
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	в
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	твою
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	разбитую
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	на две части
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	черепушку
	''')
	
	 # Шаблон текста в строчки 2
@app.on_message(filters.command("соси", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	соси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	засоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	усоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	присоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	пососи
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	дососи
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	пересоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	насоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	подсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	надсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	всоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	обсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	изсоси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	не соси
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	разсоси
	''')
	
	 # Шаблон текста в строчки 3
@app.on_message(filters.command("нсп2", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	я тебя буду швырять телочку ебанную
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	окровавленный сынуля шлюхи 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	красную плесень
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	твоей шизофренированной матери 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	кинул как кость собаке
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	кошу твое осознание и даже не стесняюсь
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	взорванный зачуханный дряблый сынуля куртизанки 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ты
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	зачем
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	нашёл
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	себя
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	среди
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ярких
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	красок
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	спермы?
	''')
	
	 # Шаблон текста в строчки 4
@app.on_message(filters.command("нсп3", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	червям приказ отдали потанцевать в твоём кишечнике
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	как те закрутка бутылки пива в кишечник моим великолепным нон стопом? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	зачем путаешь бефидок с моей кончей и хуяришь его на завтрак? 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я сигарету об твоё глазное яблоко тушу, теперь оно отслаивается
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	ахихивхиххахип
	''') 
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я щас матери твоей кости распилю и дам тебе погрызть
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	скручивай ласты сынуля шлюхи 
	''')
	sleep(0.1)
	app.send_message(msg.chat.id, f'''
	я тебе твое сасалище зарыганное в мясище разхуярил уже
	''')
	
#1000-7
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
	global number
	i = 1000
	while i > 0:
		try:
			app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
		except FloodWait as e:
			sleep(e.x)

		i -= 7
		sleep(0)

	if(end_message != ''):
		app.send_message(message.chat.id, end_message)

#спамер
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, msg):
	spams = " ".join(msg.command[2:])

	global number

	if not spams:
		msg.edit(f'''
			**Error: Что-то пошло не так...\nИспользование: .spam <кол-во спама> <слово>**''')
		sleep(1.5)
		msg.delete()
	else:
		for _ in range(int(msg.command[1])):
			app.send_message(msg.chat.id, spams)

#правда/ложь
@app.on_message(filters.command("tf", prefixes=".") & filters.me)
def betaloves(_, msg):
	t = ["[правда]", "[ложь]"]

	try0 = random.choice(t)
	try1 = " ".join(msg.command[1:])

	if not try1:
		msg.edit(f'''
			**Error: Вы не ввели вопрос!\nИспользование: .tf <вопрос>**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{try1} {try0}''')

	sleep(5)
	global number
	number = number + 1		
	
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

@app.on_message(filters.command('id', prefixes='.') & filters.me)
def id(_, message):
    message.edit(f'ID = {message.reply_to_message.from_user.id}')

# @app.on_message(filters.sticker)
def reply(_, message):
    with open('userlist.txt', 'r+', encoding='utf-8') as file:
        usertoreply = file.read().splitlines()

    if str(message.from_user.id) in usertoreply:
        with open('стик.txt', 'r+', encoding='utf-8') as file:
            alljokes = file.read().splitlines()
            randomjoke = random.choice(alljokes)
            # message.reply(randomjoke)

#спам лестница
@app.on_message(filters.text & filters.me)
def send(_, message):
    message.delete()
    
    text = message.text.split(' ', 0)
    num = 1
    words = text[0].split()
    words_mass = parting(words, num)
    
    for words_to_send in words_mass:
        group_words = ""
        for word in words_to_send:
            try:
                group_words = (f"{word}")
            except FloodWait as e:
                sleep(e.x)
                
            app.send_message(message.chat.id, group_words)
          
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