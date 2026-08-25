import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer
    
mixer.init()
mx = mixer.music
os.chdir('music')

def play(song,lp):
    try:
        mx.load(song)
        mx.play(loops=lp)
    except:
        print('Песня не найдена')
    
def stop():
    mx.stop()
    
def pause():
    mx.pause()
    
def unpause():
    mx.unpause()
    
def lists():
    lst = os.listdir()
    print(f'Ваш плейлист:\n{'\n'.join(lst).replace('.mp3','')}')


def help():
    print("""
                        _             _                       
      ___ _ __ ___   __| |      _ __ | | __ _ _   _  ___ _ __ 
     / __| '_ ` _ \ / _` |_____| '_ \| |/ _` | | | |/ _ \ '__|
    | (__| | | | | | (_| |_____| |_) | | (_| | |_| |  __/ |   
     \___|_| |_| |_|\__,_|     | .__/|_|\__,_|\__, |\___|_|   
                               |_|            |___/
          """)
    print('🕹️ Команды:\n\nplay [name] — включить песню из плейлиста.\nplay [name] -loop — включить песню из плейлиста и повторять ее.\nstop — выключить песню.\npause — поставить на паузу.\nunpause — убрать паузу.\nlist — посмотреть плейлист.\nhelp — вызвать это меню.')
    print(f'\n{'-'*50}\n')
    
help()
        
while True:
    a = input()
    if a.split() and a.split()[0] == 'play' and len(a.split())==2:play(f'{a.split()[1]}.mp3',0)
    elif a.split() and a.split()[0] == 'play' and len(a.split())==3 and a.split()[2] == '-loop':play(f'{a.split()[1]}.mp3',-1)
    elif a == 'stop':stop()
    elif a == 'pause':pause()
    elif a == 'unpause':unpause()
    elif a == 'help':help()
    elif a == 'list':lists()
    else: print('Команда не найдена')