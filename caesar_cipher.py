print("-----------------WELCOME TO CAESAR CIPHER------------------")

while True:
    str=input("Type 'encrypt' for encryption , type 'decrypt' for decryption:")

    if str=="encrypt":
        message=input("Type your message: ")
        n = int(input("Type the shift number: "))
        encrypted_message = ""
        print("Here's the encrypted result: ")
        for char in message:
            if char.isalpha():
                encrypted_message += chr((ord(char)-97+n)%26+97)

            else :
                encrypted_message += char
        print(encrypted_message)

    else :
        message=input("Type your message: ")
        n = int(input("Type the shift number: "))
        decrypted_message = ""
        print("Here's the decrypted result: ")
        for char in message:
            if char.isalpha():
                decrypted_message += chr((ord(char)-97-n)%26+97)
            else :
                decrypted_message += char
        print(decrypted_message)
    
    consent= input("Type 'yes' if you want to go again . Otherwise type no .")
    if consent == "no":
        print("---------------GOODBYE-----------------")
        break

            
