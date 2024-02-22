version = open('verid', 'r')
ver = version.readline()
ver = ver.strip()
verlist = ver.split('.')
version.close()
print('-' * 5, f'RblxChatter v{ver}', '-' * 5)
from bs4 import BeautifulSoup
import requests


print('[info]: Checking for update...')
url = 'https://raw.githubusercontent.com/sc1l/RblxChatter/main/verid'

response = requests.get(url)
if response.status_code == 200:
    rep = response.text
    soup = BeautifulSoup(rep, 'html.parser')
    clean_text = str(soup).strip()
    onlist = str(clean_text).split('.')
    print('\033[33m'+f'[debug]: local = {ver, verlist}, online = {clean_text, onlist}'+'\033[0m')
    print(f'[info]: Checked online version: {clean_text}')
    print(f'[info]: Checked local version: {ver}')
    if verlist == onlist:
        print(f'[info]: this version is lastest version.')
    elif verlist[0] < onlist[0]:
        print('\033[91m'+f'[warn]: outdated version! please update to {clean_text}'+'\033[0m')
    elif verlist[0] == onlist[0] and verlist[1] < onlist[1]:
        print('\033[91m'+f'[warn]: outdated version! please update to {clean_text}'+'\033[0m')
    elif verlist[0] == onlist[0] and verlist[1] == onlist[1] and verlist[2] < onlist[2]:
        print('\033[91m'+f'[warn]: outdated version! please update to {clean_text}'+'\033[0m')
else : 
    print('\033[91m'+'[warn]: failed to check for update!'+'\033[0m')



try:
    
    import random
    print('\033[33m'+'[debug]: Imported random'+'\033[0m')
    import pyautogui
    print('\033[33m'+'[debug]: Imported pyautogui'+'\033[0m')
    import time
    print('\033[33m'+'[debug]: Imported time'+'\033[0m')
    from pywinauto.keyboard import send_keys
    print('\033[33m'+'[debug]: Imported pywinauto...'+'\033[0m')
    print('[input]: Please select your .tpl file(Full name)')
    tpl = open(input('>>> '), "r")
    text = tpl.read()
    message = text.split("\n")
    tpl.close()
    print('[input]: Please select your min second(default 9)')
    min = int(input('>>> '))
    print('[input]: Please select your max second(default 15)')
    max = int(input('>>> '))
    print('[info]: Waiting for 5 seconds')
    time.sleep(5)
    while True:
        pyautogui.press('/')
        print('[info]: opened chat')
        time.sleep(0.5)
        msg = random.choice(message)
        pyautogui.write(msg)
        print(f'[info]: chatted {msg}')
        time.sleep(1)
        send_keys('{ENTER}')
        send_keys('{ENTER}')
        send_keys('{ENTER}')
        print('[info]: Typed chat')
        wait = random.randint(min, max)
        print(f'[info]: Waiting for {wait} seconds...')
        time.sleep(wait)
except KeyboardInterrupt as KeyMsg:
    print('\033[31m'+f'[Error]: Keyboard Exception. Message = {KeyMsg}'+'\033[0m')
except BaseException as Msg:
    print('\033[31m'+f'[Error]: {Msg}'+'\033[0m')
