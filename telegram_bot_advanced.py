import json
import requests
from time import sleep
from threading import Thread, Lock

global config
config = {'url': 'https://api.telegram.org/bot1785291467:AAFo6L_CpajZW_lLbCYaOcjxUWbIeKnM8-8/', 'lock': Lock()}

def del_update(data):
    global config

    config['lock'].acquire()
    requests.post(config['url'] + 'getUpdates', {'offset': data['update_id']+1})
    config['lock'].release()


def send_message(data, msg):
    global config

    config['lock'].acquire()
    requests.post(config['url'] + 'sendMessage', {'chat_id': data['message']['chat']['id'], 'text': str(msg)})
    config['lock'].release()




while True:
    x=''
    while 'result' not in x:
        try:
            x = json.loads(requests.get(config['url'] + 'getUpdates').text)
        except Exception as e:
            x=''
            if 'Failed to estabilish a new connection' in str(e):
                print('Perda de conexao')
            else:
                print('Erro desconhecido: ' + str(e))

    if len(x['result']) > 0:
        for data in x['result']:
            Thread(target=del_update, args=(data, )).start()

            print(json.dumps(data, indent=1))
            if data['message']['text'] == 'oi':
                Thread(target=send_message, args=(data, 'oi pra vc tbem!')).start()

        sleep(1.5)
