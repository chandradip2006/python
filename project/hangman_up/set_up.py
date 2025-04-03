import random
from database import words
print("Let's play Hangman!!")

# words=words.split(" ")
# print(words)

# print(f"list of words: {words}")
random.shuffle(words)
word = random.choice(words)
word1=word
# count=len(word) 
count=len(word)
l=count
# print("You have total 6 chances")
print(f"Word length: {count}")
list2=['_']*count
chance= int(input("no of chances you want to play with: "))
# chance=6
print(f"You have only {chance} lives so try to guess the word within {chance} attempts! Good luck")
print("-----------------------------------------------------------------------")
list1=list(word)
list3=[]
while True:
    print(list2)
    count1=0;
    print(f"life remaining: {chance}")
    char = input("guess a letter: ")
    if char in list3:
        print("You already guessed this letter, try another one!")
        print("-----------------------------------------------------------------------")
        continue
    else:
        list3.append(char)
    if char in list1:
        print("good guess")
        # list[word.find(char)]=char
        # word=word.replace(char,"-" , 1)
        for i in range(l):
            if list1[i]==char:
                list2[i]=char
                list1[i]="-"
                count1 +=1;
        count=count-count1
        if count==0:
            word=word.replace(char,"-" , 1)
            print(list2)
            print("congratulations you won!!!")
            break
    else :
        # print("wrong guess , try again")
        print(f"You guessed {char} that is not present in the word  . So you lose a life")
        chance=chance-1
        if chance==0:
            print(f"game over  , you die , the word was {word1}")
            break
    print("-----------------------------------------------------------------------")
