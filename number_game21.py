import random 

count=1
list=[]
print("Player 2 is Computer.")
str=input("Do you want to start the game? (Yes/No)")
if(str=="Yes"):
    print("Enter 'F' to take the first chance.")
    print("Enter 'S' to take the second chance.")
    str=input();
    if(str=="F"):
        while(True):
            list1=[]
            n=int(input("How many numbers do you wish to enter?"))
            flag1=True
            for i in range(0 , n):
                num=int(input(">"))
                if(num==21):
                    print("Game Over! Computer wins!")
                    print("-------------------------------------THANK YOU FOR PLAYING-----------------------------------")
                    flag1=False
                    break;
                list1.append(num)
            if(flag1==False):
                break
            if(len(list)>0):
                flag=True
                if(list1[0]-list[len(list)-1]==1):
                    for i in range(1 , n):
                        if(list1[i]-list1[i-1]!=1):
                            print("Wrong input. You are disqualified from the game.")
                            print("-------------------------------------THANK YOU FOR PLAYING-----------------------------------")
                            flag=False
                            break;
                if(flag==False):
                    break
                else:
                    list.append(list1)
                
            else:
                flag=True
                for i in range(1 , n):
                        if(list1[i]-list1[i-1]!=1):
                            print("Wrong input. You are disqualified from the game.")
                            print("-------------------------------------THANK YOU FOR PLAYING-----------------------------------")
                            flag=False
                            break;
                if(flag==True):
                    list.append(list1)
                else:
                    break
            count = count +n;
            r=random.randint(1 , 21-count+1)
            flag1=True
            for num in range(count , count+r):
                if(num==21):
                    print("You win!")
                    print("-------------------------------------THANK YOU FOR PLAYING-----------------------------------")

                    flag1=False
                    break
                list.append(num)
            if(flag1==False):
                break
            else:
                print("Order of inputs after computer's turn is:")
                print(list)
            count = count +r
                
                    
        
    else:
        while True:
            r=random.randint(1 , 21-count+1)
            flag1=True
            for num in range(count , count+r):
                if(num==21):
                    print("You win!")
                    print("-------------------------------------THANK YOU FOR PLAYING-----------------------------------")

                    flag1=False
                    break
                list.append(num)
            if(flag1==False):
                break
            else:
                print("Order of inputs after computer's turn is:")
                print(list)
            count = count +r
            list1=[]
            n=int(input("How many numbers do you wish to enter?"))
            flag1=True
            for i in range(0 , n):
                num=int(input(">"))
                if(num==21):
                    print("Game Over! Computer wins!")
                    print("-------------------------------------THANK YOU FOR PLAYING-----------------------------------")
                    flag1=False
                    break;
                list1.append(num)
            if(flag1==False):
                break
            if(len(list)>0):
                flag=True
                if(list1[0]-list[len(list)-1]==1):
                    for i in range(1 , n):
                        if(list1[i]-list1[i-1]!=1):
                            print("Wrong input. You are disqualified from the game.")
                            print("-------------------------------------THANK YOU FOR PLAYING-----------------------------------")
                            flag=False
                            break;
                if(flag==False):
                    break
                else:
                    list.append(list1)
                
            else:
                flag=True
                for i in range(1 , n):
                        if(list1[i]-list1[i-1]!=1):
                            print("Wrong input. You are disqualified from the game.")
                            print("-------------------------------------THANK YOU FOR PLAYING-----------------------------------")
                            flag=False
                            break;
                if(flag==True):
                    list.append(list1)
                else:
                    break
            count = count +n;
else:
    print("---------------------THANK YOU FOR YOUR SUGGESTION-------------------")



        
