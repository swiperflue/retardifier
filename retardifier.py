import requests
import json
import time
import random
import os
import re


class Retardifier:
    def __init__(self, token, gif_dir, retards_ids, retardations, retardation_salt):
        self.token = token
        self.gif_dir = gif_dir
        self.retards_ids = retards_ids
        self.retardations = retardations
        self.retardation_misc = retardation_salt
        self.url = 'https://api.telegram.org/bot'

    def get_updates(self, offset=None):
        url=f'{self.url}{self.token}/getUpdates'
        if offset:
            url+=f'?offset={offset}'
        response = requests.get(url)
        if not response.ok:
            print(f"Failed getting updates: {response.content}")
            return None
        return json.loads(response.content)

    def send_reply(self, gif, text, message_id, chat_id):
        url=f'{self.url}{self.token}/sendAnimation'
        files = {'animation': open(gif, 'rb')}
        data = {'chat_id': chat_id, 'caption': text, 'reply_to_message_id': message_id}
        response = requests.post(url, files=files, data=data)
        if not response.ok:
            print(f"Failed to send reply: {response.content}")
        
    def handle_retardation(self, retardation):
        for item in self.retardations:
            if re.search(item, retardation['text'], re.IGNORECASE):
                reply = self.retardify(retardation['text'])
                gif = os.path.join(self.gif_dir, random.choice(os.listdir(self.gif_dir)))
                self.send_reply(gif, reply, retardation['message_id'], retardation['chat']['id'])
                return
            
    def retardify(self, text):
        retardified_text = ">"
        for char in text:
            cap = random.randint(0, 1)
            if cap:
                retardified_text += char.upper()
            else:
                retardified_text += char.lower()
        retardation_suffix = ' '
        retardation_suffix += ' '.join(random.sample(self.retardation_misc, 7))
        retardified_text += retardation_suffix
        return retardified_text

    def run(self):
        offset = None
        while True:
            updates = self.get_updates(offset)
            for update in updates['result']:
                offset=update['update_id']+1
                if 'message' in update and 'text' in update['message'] and update['message']['from']['id'] in self.retards_ids:
                    self.handle_retardation(update['message'])
            time.sleep(1)
        
    
if __name__ == '__main__':
    config = {}
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    daniel = Retardifier(
        config['token'],
        config['gif_dir'],
        config['retards_ids'],
        config['retardations'],
        config['retardation_salt']
    )
    daniel.run()
