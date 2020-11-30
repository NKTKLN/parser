import requests, time
# # #
parsertokens = ['0123456789:ABC10DEFGhIJKlmnO1P1QrS-tuvw1XYZaB1',
                '0123456789:ABC10DEFGhIJKlmnO1P1QrS-tuvw1XYZaB1',
                '0123456789:ABC10DEFGhIJKlmnO1P1QrS-tuvw1XYZaB1',
                '0123456789:ABC10DEFGhIJKlmnO1P1QrS-tuvw1XYZaB1',
                '0123456789:ABC10DEFGhIJKlmnO1P1QrS-tuvw1XYZaB1']
token = '0123456789:ABC10DEFGhIJKlmnO1P1QrS-tuvw1XYZaB1'
chat_id = '@chanal_name'
chanals = ['chanal_name', 'chanal_name', 'chanal_name', '...']
# #
url = ''
num = 0
urllast = []
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
                            if len(respons.json()['response']['items'][00]['attachments']) == 1:
                                try:
                                    url = respons.json()['response']['items'][00]['attachments'][0]['photo']['sizes'][7]['url']
                                except:
                                    url = respons.json()['response']['items'][00]['attachments'][0]['photo']['sizes'][6]['url']
            else:
                if respons.json()['response']['items'][1]['marked_as_ads'] == 0:
                    if len(respons.json()['response']['items'][1]['text']) < 50:
                        if 'copyright' not in respons.json()['response']['items'][00]:
                            if len(respons.json()['response']['items'][1]['attachments']) == 1:
                                try:
                                    url = respons.json()['response']['items'][1]['attachments'][0]['photo']['sizes'][7]['url']
                                except:
                                    url = respons.json()['response']['items'][1]['attachments'][0]['photo']['sizes'][6]['url']
            if url.split("/")[3] + url.split("/")[4] not in urllast and url != '':
                url2 = f'https://api.telegram.org/bot{token}/sendPhoto'
                requests.post(url=url2, data={'chat_id': chat_id, 'photo': url})
                urllast.append(url.split("/")[3] + url.split("/")[4])
            num += 1
            if num == len(parsertokens) - 1:
                num = 0
            time.sleep(30)
        except:
            pass
