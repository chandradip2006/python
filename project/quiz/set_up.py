from database import qa_dict
import random

consent=input("Do you want to start the quiz?(yes/no)")
if(consent=="yes"):
    print("---------------------Welcome to the quiz----------------------------")
    n=int(input("no of questions you want to be asked: "))
    print(f"the quiz consists of {n} questions . All questions must be answered .GOOD LUCK!!")
    print("if you want to quit , type 'Q'")
    score=0
    print("--------------------------------------------------")
    for i in range(n):
        question = random.choice(list(qa_dict.keys()))
        print(f"{i+1}." , question)
        print()
        answer = input("Enter your answer: ")
        print()
        if answer.lower() == qa_dict[question].lower():
            print("Correct answer!!")
            score += 1
        
        elif (answer=="Q"):
            break
        else :
            print("Incorrect answer!!")
            print("The correct answer is: ", qa_dict[question])
        print(f"your score: {score}/{n}")
        print("--------------------------------------------------")

    print("Quiz ended!!")
    print(f"your final score: {(score/n)*100}%")




print("---------------------------Goodbye-----------------------------")
