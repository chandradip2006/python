import random

num = random.randint(1 , 100);
# print(num)

guess=int(input("guess a number between 1 to 100: "))

count=0
while True:
    if(guess>num):
        guess=int(input("guess a lower number: "))
        count+=1
    elif (guess<num):
        guess=int(input("guess a higher number: "))
        count+=1
    else:
        count += 1
        print(f"you guessed it in {count} tries")
        break


