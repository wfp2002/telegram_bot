import requests, re, time

targetAlta = 60.0
targetBaixa = 40.0

def sendMessage(botMessage):
    botToken = '234987234:JKmhjkMNHyxu2ZPyOc17bs9sYUjmnhGSWr'
    #Para pegar o botToken, e na hora da criacao do bot entrar no @botFather e dar um /New, assim que informar os nomes solicitados sera gerado pelo @botFather
    botChatID = '475745179' 
    #Para pegar o botChatID acessar o endereco abaixo e ver o message_id->from->id: Algo como "475745179" 
    #https://api.telegram.org/bot234987234:JKmhjkMNHyxu2ZPyOc17bs9sYUjmnhGSWr/getUPdates
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

        if (float(seed) > targetAlta):
            print('Maior que $ ' + str(targetAlta))
            sendMessage('SEED em Alta: $' + str(seed))
        elif (float(seed) < targetBaixa):
            print('Menor que $ ' + str(targetBaixa))
            sendMessage('SEED em Baixa: $' + str(seed))

        time.sleep(1200)

    except Exception:
        pass
