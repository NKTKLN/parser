import requests
import time
import telebot
from telebot.types import InputMediaPhoto
# # #
parsertokens = ['01234567890a1b1c121d3f1gh4151617181920i212j2k2l3m2425n26o2p7q2r8s2t930',
                '01234567890a1b1c121d3f1gh4151617181920i212j2k2l3m2425n26o2p7q2r8s2t930',
                '01234567890a1b1c121d3f1gh4151617181920i212j2k2l3m2425n26o2p7q2r8s2t930',
                '01234567890a1b1c121d3f1gh4151617181920i212j2k2l3m2425n26o2p7q2r8s2t930',
                '01234567890a1b1c121d3f1gh4151617181920i212j2k2l3m2425n26o2p7q2r8s2t930']
token = '0123456789:ABC10DEFGhIJKlmnO1P1QrS-tuvw1XYZaB1'
chat_id = '@chanal_name'
 cap = 'caption'
chanals = ['chanal_name', 'chanal_name', 'chanal_name', '...']
# # #
bot = telebot.TeleBot(token)
# # 
num = 0
urllast = []
timer = 0 
#
while True:
    for chanal in chanals:
        parsertoken = parsertokens[num]
        respons = requests.get('https://api.vk.com/method/wall.get', params={"access_token": parsertoken, "v": 5.124, "domain": chanal})
        try:
            type1 = respons.json()['response']['items'][00]['attachments'][0]['type']
            type2 = respons.json()['response']['items'][1]['attachments'][0]['type'] 
            if respons.json()['response']['items'][00]['attachments'][0][type1]['date'] > respons.json()['response']['items'][1]['attachments'][0][type2]['date']:
                if respons.json()['response']['items'][00]['marked_as_ads'] == 0:
                    if len(respons.json()['response']['items'][00]['text']) < 50:
                        if 'copyright' not in respons.json()['response']['items'][00]:
                            urs = respons.json()['response']['items'][00]['attachments']
            else:
                if respons.json()['response']['items'][1]['marked_as_ads'] == 0:
                    if len(respons.json()['response']['items'][1]['text']) < 50:
                        if 'copyright' not in respons.json()['response']['items'][1]:
                            urs = respons.json()['response']['items'][1]['attachments']
            try:
                url = [InputMediaPhoto(urs[0]['photo']['sizes'][7]['url'], caption=cap)] + [InputMediaPhoto(urs[i + 1]['photo']['sizes'][6]['url']) for i in range(len(urs) - 1)]
            except:
                url = [InputMediaPhoto(urs[0]['photo']['sizes'][6]['url'], caption=cap)] + [InputMediaPhoto(urs[i + 1]['photo']['sizes'][6]['url']) for i in range(len(urs) - 1)]
                                        
            if urs[0]['photo']['sizes'][6]['url'] not in urllast:
                bot.send_media_group(chat_id, url)
                urllast.append(urs[0]['photo']['sizes'][6]['url'])
            num += 1
            if num == len(parsertokens) - 1:
                num = 0
                time.sleep(65)
        except:
            pass
    timer += 1
    if timer == "100000000":
        urllast.clear()
