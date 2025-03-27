import random

alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


num=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# str="0 1 2 3 4 5 6 7 8 9"
# str=list(str.split(" "))
# print(str)

# str="~ ` ! @ # $ % ^ & * ( ) _ - + = / . , < > : ; [ ] { } ? | \ "
# str=list(str.split(" "))
# print(str)

char1 =['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '/', '.', ',', '<', '>', ':', ';', '[', ']', '{', '}', '?', '|', '\\']

password=""
length=int(input("Enter the no of alphabets in your password:"))
length1=int(input("Enter the no of numbers in your password:"))
length2=int(input("Enter the no of special characters in your password:"))

for char in alpha:
    password+=random.choice(char)
    length-=1
    if(length==0):
        break

for char in num:
    password+=random.choice(char)
    length1-=1
    if(length1==0):
        break

for c in char1:
    password+=random.choice(char1)
    length2-=1
    if(length2==0):
        break

list=list(password);
random.shuffle(list)
password="".join(list)
print(password)
