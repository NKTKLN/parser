# -*- coding: utf-8 -*-

import telebot, requests, time

parsertokens = [' ']
token = ' '
chat_id = '@ '
bot = telebot.TeleBot(token)
url = '////'
num = 0
urllast = []

while True:
    chanals = [' ']
    for chanal in chanals:
        parsertoken = parsertokens[num]
        respons = requests.get('https://api.vk.com/method/wall.get', params={"access_token": parsertoken, "v": 5.124, "domain": chanal})
        try:
            if chanal in [' ']:
                if respons.json()['response']['items'][00]['marked_as_ads'] == 0:
                    if len(respons.json()['response']['items'][00]['text']) < 70:
                        if len(respons.json()['response']['items'][00]['attachments']) == 1:
                            try:
                                url = respons.json()['response']['items'][00]['attachments'][0]['photo']['sizes'][7]['url']
                            except:
                                url = respons.json()['response']['items'][00]['attachments'][0]['photo']['sizes'][6]['url']
            elif chanal in [' ']:
                if respons.json()['response']['items'][1]['marked_as_ads'] == 0:
                    if len(respons.json()['response']['items'][1]['text']) < 70:
                        if len(respons.json()['response']['items'][1]['attachments']) == 1:
                            try:
                                url = respons.json()['response']['items'][1]['attachments'][0]['photo']['sizes'][7]['url']
                            except:
                                url = respons.json()['response']['items'][1]['attachments'][0]['photo']['sizes'][6]['url']
            if url.split("/")[3] + url.split("/")[4] not in urllast and url != '////':
                bot.send_photo(chat_id, url)
                urllast.append(url.split("/")[3] + url.split("/")[4])
            num += 1
            if num == len(parsertokens) - 1:
                num = 0
            time.sleep(30)
        except:
            pass
