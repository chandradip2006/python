import random
from database import words
print("Let's play Hangman!!")
chance=6
print(f"You have only {chance} lives so try to guess the word within {chance} attempts! Good luck")


# words=words.split(" ")
# print(words)


# print(f"list of words: {words}")
random.shuffle(words)
word = random.choice(words)
word1=word
# count=len(word) 
count=5
# print("You have total 6 chances")
print(f"Word length: {count}")
list=['_' , '_' , '_' , '_' , '_']
while True:
    print(list)
    char = input("guess a letter: ")
    if char in word:
        print("good guess")
        list[word.find(char)]=char
        word=word.replace(char,"-" , 1)
        count=count-1
        if count==0:
            word=word.replace(char,"-" , 1)
            print(list)
            print(f"congratulations you won!!!")
            break
        print(f"life remaining: {chance}")
    else :
        # print("wrong guess , try again")
        print(f"You guessed {char} that is not present in the word  . So you lose a life")
        chance=chance-1
        if chance==0:
            print(f"game over  , you die , the word was {word1}")
            break
        print(f"life remaining: {chance}")
