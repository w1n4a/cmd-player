import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer
    
mixer.init()
mx = mixer.music
os.chdir('music')

def play(song,lp):
    try:
        mx.load(song,lp)
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
    os.chdir(os.path.dirname(os.path.abspath(__file__))
)
    with open('README.md',"r",encoding="utf-8") as f:
        print(f.read())
    print(f'\n{'-'*50}\n')
    os.chdir('music')
    
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