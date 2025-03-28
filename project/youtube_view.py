import webbrowser as web
import time

url = input("enter your url: ")
time1 = int(input("enter the time you want to watch: "))
n = int(input("enter the no of times you want to view: "))

for i in range(n):
    web.open_new_tab(url)
    time.sleep(time1)