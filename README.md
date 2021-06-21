# retardifier

A simple bot for retardifiying retards on Telegram.

To put it simply when some retard on Telegram say something completely retarded, it takes his message and retardifies it even more, and reply to it.

![image](https://user-images.githubusercontent.com/81438111/122693829-553a9600-d233-11eb-9e6a-0c55c10ac192.png)

## Installation and usage

1. clone the repo and cd to it
```
git clone https://github.com/swiperflue/retardifier.git
cd retardifier
```
2. create a python virtual environment and activate it
```
python -m venv venv
source venv/bin/activate
```
3. install the requirements
```
pip install -r requirements.txt
```
4. configure the bot by editing the config.json file
- token: is your [Telegram API token](https://core.telegram.org/bots/).
- gif_dir: is the derectory that contains the gifs, default is fine.
- retards_ids: is a list of ids for the retarded users you want the bot to reply to (you can use another bot to get that).
- retardations: a list of regular expressions for the retardations you want the bot to reply to.
- retardation_salt: a list of silly retarded words you want the bot to add to the end of the reply.

5. run the bot
```
python retardifier.py
```

PS: And yeah, don't forget to have fun :P, don't take this too seriously.
