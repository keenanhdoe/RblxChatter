with open('verid', 'r') as version:
    ver = version.readline().strip()
    verlist = ver.split('.')

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
        debugger.info('This version is the latest version.')
    elif verlist < onlist:
        debugger.warn(f'Outdated version! Please update to {clean_text}')

else:
    debugger.warn('Failed to check for an update!')

try:
    import random, pyautogui, time
    from pywinauto.keyboard import send_keys
    debugger.debug('Imported random, pyautogui, time, pywinauto...')
    debugger.sinput('Please select your .tpl file(Full name)')
    
    with open(input('>>> '), "r") as tpl:
        message = tpl.read().split("\n")

    min_sec = debugger.input('Please select your min second(default 9)')
    max_sec = debugger.input('Please select your max second(default 15)')
    
    debugger.info('Waiting for 5 seconds')
    time.sleep(5)

    while True:
        pyautogui.press('/')
        debugger.info('Opened chat')
        time.sleep(0.5)
        msg = random.choice(message)
        pyautogui.write(msg)
        debugger.info(f'Chatted {msg}')
        time.sleep(1)
        send_keys('{ENTER}')
        send_keys('{ENTER}')
        debugger.info('Pressed Enter')
        wait = random.randint(int(min_sec), int(max_sec))
        debugger.info(f'Waiting for {wait} seconds...')
        time.sleep(wait)

except KeyboardInterrupt as KeyMsg:
    debugger.error(f'Keyboard Exception. Message = {KeyMsg}')
except BaseException as Msg:
    debugger.error(f'[Error]: {Msg}')
