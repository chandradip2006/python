import os
# os.system("cls")

name=""
bid=0
while True:
    str=input("What is your name?: ")
    price=int(input("What is your bid?: "))
    if price>bid:
        name=str
        bid=price
    print("Are there any other bidders? Type 'yes' or 'no'")
    consent=input(">")
    if consent.lower()=='no':
        break
    else :
        os.system("cls")

print(f"The winner is {name} with a bid of ${bid}")