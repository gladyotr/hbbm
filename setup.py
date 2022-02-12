

"""



"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}█░░█ █▀▀▄ █▀▀▄ █▀▄▀█
	{re}█▀▀█ █▀▀▄ █▀▀▄ █░▀░█
	{re}▀░░▀ ▀▀▀░ ▀▀▀░ ▀░░░▀
	
	           
	{re}https://https://t.me/hababamsohbet
	{cy}yapım @gladbey
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] api ID giriniz : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+]  hash ID giriniz : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] telefon numarası giriniz : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] kurulum tamamlandı !!!")
print(gr+"[+] python3 scraper.py yazıp devam edebilirsiniz")
print(gr+"[+] yapım @gladbey")
