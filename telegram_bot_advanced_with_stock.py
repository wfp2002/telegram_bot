import json
import requests
import re
from time import sleep
from threading import Thread, Lock

global config
config = {'url': 'https://api.telegram.org/bot12876218736:jdshfkshfd_ASJjhsdCYaOcjxUWbIeKnM8-8/', 'lock': Lock()}

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


def valor_acao(acao):
    
    if acao == 'seed':
        seedweb = requests.get("https://bscscan.com/token/0x40B34cC972908060D6d527276e17c105d224559d")
        p = re.compile("[$][0-9]{1,4}\.[0-9]{1,4}")
        resultado = p.search(seedweb.text)
        seed = str(resultado.group(0))
        return str(seed)

    elif acao == 'tree':
        treeweb = requests.get("https://bscscan.com/token/0xf0fcd737fce18f95621cc7841ebe0ea6efccf77e")
        p = re.compile("[$][0-9]{1,4}\.[0-9]{1,4}")
        resultado = p.search(treeweb.text)
        tree = str(resultado.group(0))
        return str(tree)
        

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
            elif data['message']['text'] == 'seed':
                Thread(target=send_message, args=(data, valor_acao('seed'))).start()
            elif data['message']['text'] == 'tree':
                Thread(target=send_message, args=(data, valor_acao('tree'))).start()

        sleep(1.5)
