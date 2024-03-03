version = open('verid', 'r')
ver = version.readline()
ver = ver.strip()
verlist = ver.split('.')
version.close()
print('-' * 10, f'RblxChatter v{ver}', '-' * 10)
from bs4 import BeautifulSoup
import requests
import debugger


debugger.info('Checking for update...')
url = 'https://raw.githubusercontent.com/sc1l/RblxChatter/main/verid'

response = requests.get(url)
if response.status_code == 200:
    rep = response.text
    soup = BeautifulSoup(rep, 'html.parser')
    clean_text = str(soup).strip()
    onlist = str(clean_text).split('.')
    debugger.debug(f'local = {ver, verlist}, online = {clean_text, onlist}')
    debugger.info(f'Checked online version: {clean_text}')
    debugger.info(f'Checked local version: {ver}')
    if verlist == onlist:
        debugger.info(f'this version is lastest version.')
    elif verlist[0] < onlist[0]:
        debugger.warn(f'outdated version! please update to {clean_text}')
    elif verlist[0] == onlist[0] and verlist[1] < onlist[1]:
        debugger.warn(f'outdated version! please update to {clean_text}')
    elif verlist[0] == onlist[0] and verlist[1] == onlist[1] and verlist[2] < onlist[2]:
        debugger.warn(f'outdated version! please update to {clean_text}')
else : 
    debugger.warn('failed to check for update!')



try:
    
    import random
    debugger.debug('Imported random')
    import pyautogui
    debugger.debug('Imported pyautogui')
    import time
    debugger.debug('Imported time')
    from pywinauto.keyboard import send_keys
    debugger.debug('Imported pywinauto...')
    debugger.sinput('Please select your .tpl file(Full name)')
    tpl = open(input('>>> '), "r")
    text = tpl.read()
    message = text.split("\n")
    tpl.close()
    min = debugger.input('Please select your min second(default 9)')
    max = debugger.input('Please select your max second(default 15)')
    debugger.info('Waiting for 5 seconds')
    time.sleep(5)
    while True:
        pyautogui.press('/')
        debugger.info('opened chat')
        time.sleep(0.5)
        msg = random.choice(message)
        pyautogui.write(msg)
        debugger.info(f'chatted {msg}')
        time.sleep(1)
        send_keys('{ENTER}')
        send_keys('{ENTER}')
        debugger.info('pressed Enter')
        wait = random.randint(min, max)
        debugger.info(f'Waiting for {wait} seconds...')
        time.sleep(wait)

except KeyboardInterrupt as KeyMsg:
    debugger.error(f'Keyboard Exception. Message = {KeyMsg}')
except BaseException as Msg:
    debugger.error(f'[Error]: {Msg}')
