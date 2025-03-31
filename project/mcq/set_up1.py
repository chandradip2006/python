from database1 import mcq_dict
import random

consent=input("Do you want to start quiz?(yes/no)")
l = len(mcq_dict)


if consent.lower()=='yes':
    print("----------------Welcome to the quiz , Quiz is of MCQ format----------------")
    n = int(input("no of MCQs you want to be asked: "))
    if n<=l:
        score=0
        print(f"You have {n} MCQs. Each MCQ has 4 options. Out the 4 options only ONE option is correct , You have to answer all the questions. GOOD LUCK!!")
        print("if you want to QUIT , type 'Q'")
        print("-----------------------------------------------------")


        for i in range(n):
            question=random.choice(list(mcq_dict.keys()))
            print(f"Question {i+1}: {question}")
            options = mcq_dict[question]
            list1=list(options.keys());
            random.shuffle(list1)
            opt=[]


            for k in range(5):
                if(list1[k]!="answer"):
                    opt.append(options[list1[k]])
            for j in range(4):
                print(f"{j+1}. {opt[j]}")
            print()

            flag =True
            while flag:
                answer = input("Enter the number of your answer: ")
                z=0
                for r in range(4):
                    if(opt[r]==options["answer"]):
                        z=r+1
                        break
                if answer=="Q":
                    break
                else:
                    if(answer=="1" or  answer=="4" or answer=="3" or answer=="2"):
                        if int(answer) == z:
                            print("Correct answer")
                            score += 1
                        else:
                            print("Incorrect answer")
                            print(f"the correct is: {options["answer"]}")
                        
                        print(f"Your current score: {score}/{n}")
                        print("-----------------------------------------------------")
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 4.")
        print("Quiz is over!!!")
        print(f"Your final score is: {(score/n)*100}%")
    else:
        print(f"You have entered more than the available questions , Please enter a number between 1 and {l}")

print("--------------------GOOD BYE-----------------------")

        

