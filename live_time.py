import time
import os
import winsound
timestamp=time.strftime('%H:%M:%S')
print(timestamp)

timestamp1=time.strftime('%H')
print(timestamp1)

timestamp=time.strftime('%M')
print(timestamp)

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

while True:
    timestamp = time.strftime('%H:%M:%S')
    print(timestamp)
    time.sleep(1)
    if(timestamp=='02:29:50'):
        # os.system('echo "\a"')
        frequency = 200
        duration = 1000*10
        winsound.Beep(frequency, duration)