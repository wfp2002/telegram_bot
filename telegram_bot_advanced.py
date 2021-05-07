import requests, re, time

targetAlta = 65.0
targetBaixa = 60.0

print('Target Alta: $ ' + str(targetAlta))
print('Target Baixa: $ ' + str(targetBaixa))

def sendMessage(botMessage):
    botToken = '1759413148:AAGZJRnU5qxu2ZPyOc17bs9sRyNYX6TYm3I'
    botChatID = '177744171'
    sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatID + '&text=' + botMessage 

    response = requests.get(sendText)
    return response.json()

while True:
    try:
        treeweb = requests.get("https://bscscan.com/token/0xf0fcd737fce18f95621cc7841ebe0ea6efccf77e")
        seedweb = requests.get("https://bscscan.com/token/0x40B34cC972908060D6d527276e17c105d224559d")
        p = re.compile("[$][0-9]{1,4}\.[0-9]{1,4}")
        result1 = p.search(treeweb.text)
        result2 = p.search(seedweb.text)

        tree = str(result1.group(0).replace('$',''))
        seed = str(result2.group(0).replace('$',''))

        result = tree + "," + seed
        print(result)

        print('Target Alta: $ ' + str(targetAlta))
        print('Target Baixa: $ ' + str(targetBaixa))

        if (float(seed) > targetAlta):
            print('Maior que $ ' + str(targetAlta))
            sendMessage('SEED em Alta: $' + str(seed))
        elif (float(seed) < targetBaixa):
            print('Menor que $ ' + str(targetBaixa))
            sendMessage('SEED em Baixa: $' + str(seed))

        time.sleep(300)

    except Exception:
        pass
