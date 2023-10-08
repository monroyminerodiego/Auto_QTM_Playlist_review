import time, random, smtplib, platform, MySQLdb, sys, pyautogui as py, pyperclip as pc, os
from win32api import GetKeyState
from win32con import VK_CAPITAL
from bs4 import BeautifulSoup
from email.message import EmailMessage
from datetime import date, timedelta
from dotenv import load_dotenv
from getpass import getuser
load_dotenv()


os.system('cls')

def double_check_screen(name1,name2):
	counter = 0
	status = True
	path1 = '../Images/'+name1+'.png'
	path2 = '../Images/'+name2+'.png'
	localization = py.locateOnScreen(path1,confidence=0.9)
	while localization == None:
		py.sleep(1)
		counter = counter + 1
		localization = py.locateOnScreen(path1,confidence=0.9)
		if localization:
			status = name1
		localization = py.locateOnScreen(path2,confidence=0.9)
		if localization:
			status = name2
		if counter == 90:
			status = False
			break
	return status
def click_screen(name):
    state = True
    counter = 0
    path = '../Images/'+name+'.png'
    localization = py.locateCenterOnScreen(path,confidence=0.9)
    while localization == None:
        py.sleep(1)
        counter = counter + 1
        localization = py.locateCenterOnScreen(path,confidence=0.9)
        if counter == 90:
            state = False
            break
    if state:
        py.click(localization)
    return state
def check_screen(name):
    state = True
    counter = 0
    path = '../Images/'+name+'.png'
    localization = py.locateOnScreen(path,confidence=0.9)
    while localization == None:
        py.sleep(1)
        counter = counter + 1
        localization = py.locateOnScreen(path,confidence=0.9)
        if counter == 90:
            state = False
            break
    return state
def change_mayusc():
    status = GetKeyState(VK_CAPITAL)
    if status:
        py.press('capslock')

def open_notepad():
    os.system(f'start "pendientes" "{paths["pendientes"]}"'); py.sleep(0.1)
    os.system(f'start "bitacora" "{paths["bitacora"]}"'); py.sleep(0.1)
    os.system(f'start "tickets" "{paths["tickets"]}"'); py.sleep(0.1)
    os.system(f'start "notas" "{paths["notas"]}"'); py.sleep(0.1)
    os.system(f'start "playcounts" "{paths["playcounts"]}"'); py.sleep(0.1)

    py.hotkey('ctrl','2'); py.sleep(0.1)
    py.hotkey('ctrl','e'); py.sleep(0.1)
    py.press('backspace'); py.sleep(0.1)
    py.hotkey('win','left'); py.sleep(0.1)
    py.hotkey('win','up'); py.sleep(0.1)
    for i in range(2):
        py.hotkey('ctrl','win','alt','down',); py.sleep(0.1)
    py.hotkey('ctrl','win','alt','right',); py.sleep(0.1)
def open_chrome():
    def open_KeePass():
        os.system(f'start "KeePass" "{paths["KeePass"]}"')
        screen_status = double_check_screen('header_keepass','login_keepass')
        if screen_status == 'login_keepass':
            click_screen('login_keepass'); py.sleep(0.3)
            change_mayusc()
            py.write(os.getenv('KEEPASS'), interval=0.03); py.sleep(0.3)
            py.press('enter'); py.sleep(0.3)
        elif screen_status == False:
            os.system(f'taskkill /im KeePass.exe /t'); py.sleep(0.3)
            os.system(f'start "KeePass" "{paths["KeePass"]}"'); py.sleep(0.3)
            open_KeePass()
    
    os.system(f'start "chrome" "{paths["chrome"]}"'); py.sleep(0.3)
    while not(check_screen('loading_chrome')):
        os.system(f'taskkill /im chrome.exe /t'); py.sleep(0.3)
        os.system(f'start "chrome" "{paths["chrome"]}"'); py.sleep(0.3)
    py.hotkey('ctrl','w'); py.sleep(0.3)
    py.hotkey('ctrl','5'); py.sleep(0.3)
    while not(click_screen('psswrd_login_qtm_prod')):
        py.press('f5'); py.sleep(0.3)
    py.hotkey('shift','tab'); py.sleep(0.3)

    open_KeePass(); py.sleep(2)
    
    py.press('tab',presses=2,interval=0.02); py.sleep(0.3)
    py.press('home'); py.sleep(0.3)
    py.hotkey('ctrl','b'); py.sleep(0.3)
    py.hotkey('win','1'); py.sleep(0.3)
    py.hotkey('ctrl','v'); py.sleep(0.3)
    py.hotkey('win','3'); py.sleep(0.3)
    py.hotkey('ctrl','c'); py.sleep(0.3)
    py.hotkey('win','1'); py.sleep(0.3)
    py.press('tab'); py.sleep(0.3)
    py.hotkey('ctrl','v'); py.sleep(0.3)
    py.press('enter'); py.sleep(0.3)
    check_screen('loading_chrome'); py.sleep(2)

def moni_digital_face():
    while True:
        py.hotkey('ctrl','f'); py.sleep(0.3)
        py.write('Support Dashboard', interval=0.03); py.sleep(0.3)
        py.press('enter', presses=2,interval=0.03); py.sleep(0.3)
        py.press('esc'); py.sleep(0.3)
        py.press('enter'); py.sleep(2)
        py.hotkey('ctrl','f'); py.sleep(0.3)
        py.write('Quantum Players Monitor',interval=0.03); py.sleep(0.3)
        py.press('enter', presses=2,interval=0.03); py.sleep(0.3)
        py.press('esc'); py.sleep(0.3)
        if click_screen('Quantum_Players_Monitor'):
            break
        else:
            py.hotkey('ctrl','r')

    py.sleep(2); click_screen('search_criteria'); py.sleep(1)
    py.hotkey('ctrl','f');py.sleep(0.3)
    py.write('page',interval=0.03); py.sleep(0.3)
    py.press('enter',presses=2,interval=0.03)
    py.press('esc'); py.sleep(0.3)
    py.hotkey('shift','tab'); py.sleep(0.3)
    py.press('down'); py.sleep(2)
    py.press('f12'); py.sleep(3)
    click_screen('body'); py.sleep(0.3)
    py.hotkey('ctrl','c'); py.sleep(0.3)
    py.press('f12'); py.sleep(3)

    read_info(pc.paste())

def read_info(html):
    soup = BeautifulSoup(html,'html.parser')
    rows = soup.find_all('tr',role='row')
    x = 1
    text = f'{x}.- '
    for row in rows:
        print(f'')




paths = {
    "bitacora":"C:/Users/Diego Monroy/Projects/BBP/Notes/bitacora.txt",
    "playcounts":"C:/Users/Diego Monroy/Projects/BBP/Notes/playcounts.txt",
    "notas":"C:/Users/Diego Monroy/Projects/BBP/Notes/notas.txt",
    "pendientes":"C:/Users/Diego Monroy/Projects/BBP/Notes/pendientes.txt",
    "tickets":"C:/Users/Diego Monroy/Projects/BBP/Notes/tickets.txt",
    "chrome":"C:/Program Files/Google/Chrome/Application/chrome.exe",
    "KeePass":"C:/Program Files/KeePass Password Safe 2/KeePass.exe"
    }
files = [
    'pendientes',
    'bitacora',
    'tickets',
    'notas',
    'playcounts',
    'chrome',
    'KeePass'
    ]

if 'chrome' in files: open_chrome()
if (('pendientes' in files) or ('bitacora' in files) or ('tickets' in files) or ('notas' in files) or ('playcounts' in files)): open_notepad()
