import time
import os
import winsound
import pygame
timestamp=time.strftime('%H:%M:%S')
print(timestamp)

timestamp1=time.strftime('%H')
print(timestamp1)

timestamp2=time.strftime('%M')
print(timestamp2)

timestamp=time.strftime('%S')
print(timestamp)

if(timestamp1>='00' and timestamp1<'12'):
    print("Good Morning")
elif(timestamp1>='12' and timestamp1<'16'):
    print("Good Afternoon")
elif(timestamp1>='16' and timestamp1<'20'):
    print("Good Evening")
else:
    print("Good Night")
z=52
while True:
    timestamp = time.strftime('%H:%M:%S')
    print(timestamp)
    time.sleep(1)
    k=int(time.strftime('%M'))
    # if(timestamp=='13:32:00'):
    if(k==z):
        
        # os.system('echo "\a"')
        # frequency = 800
        # duration = 1000*10
        # winsound.Beep(frequency, duration)
        pygame.mixer.init()
        pygame.mixer.music.load("PalPalDilKePas..mp3")
        pygame.mixer.music.play()
        ch=input("enter S to stop: ")
        if(ch=='S'):
            pygame.mixer.music.stop()
            z=z+1;