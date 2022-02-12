from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os
import sys
import csv
import traceback
import time
import random

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

print (re+" █░░█ █▀▀▄ █▀▀▄ █▀▄▀█")
print (gr+" █▀▀█ █▀▀▄ █▀▀▄ █░▀░█┘")
print (re+" ▀░░▀ ▀▀▀░ ▀▀▀░ ▀░░░▀")

print (cy+"https://https://t.me/hababamsohbet")
print (cy+"yapım @gladbey")

print (re+"NOTE :")
print ("1. 200 den fazla almaya çalışmayın hesabınız kapana bilir.")
print ("2. daha fazla hesap ekleyip daha fazla üye çekebilirsiniz.")
print ("3. 15-30 dk da bir çekin hesabınız kapana bilir.")
print ("4. hesabınız flood yememesi için yetkiniz oldugundan emin olun.")

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(re+"[!] ilk python3 setup.py yazınız\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] gelen kodu giriniz: '+re))

users = []
with open(r"members.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print(gr+'bir grup seçin:'+cy)
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input(gr+"gurubun yanındaki numarayı giriniz: "+re)
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

mode = int(input(gr+"kullanıcı adı ile çekmek için 1 id ile çekmek için 2 yazın: "+cy))

n = 0

for user in users:
    n += 1
    if n % 80 == 0:
        sleep(60)
    try:
        print("ekleniyor {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("yanlış mod seçtiniz.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("60-180 saniye arası hazırlanıyor")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print("hesabınız flood yemiş olabilir")
        print("{} saniye bekleniyor".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("hesabın gruba alımları kapalı olabilir.")
        print("5 saniye bekleniyor")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("Unexpected Error")
        continue
