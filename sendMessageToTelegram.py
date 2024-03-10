import requests
import json

def sendMessage(bot_token: str) -> bool:
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(url)
    data = response.json()
    chat_id = data['result'][0]['message']['chat']['id']
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    payload = {
        "chat_id": f'{chat_id}',
        "text": "Hello world! from Suvarna"
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    #with open("output.json", "w") as file:
         #json.dump(response.json(), file)
    if(response.status_code == 200):
        return True
    else:
        return False

if __name__ == '__main__':
    #Replace Bot token
    bot_token = "6726725343:AAGTlVHimoc31J4LK6my8zuTadHjIJjL9as" 
    if(sendMessage(bot_token)):
        print("Message sent to Telegram")
    else:
        print("Error! Couldn't send the message to Telegram")
