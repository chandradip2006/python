a="!!!!!!harry!!!!!!    !!!!!!!!harry"  #strings are immutable
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("harry" ,"john"))
print(a.split("    "))
blogHeading ="introduction tO Js"
print(blogHeading.capitalize())
str1="welcome to the console"
print(len(str1))
print(str1.center(50))
str1="welcome to the console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to" , 4 ,10))

str1="He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ishh"))
# print(str1.index("ishh"))
str1="welcometotheconsole"
print(str1.isalnum())
str1="welcome"
print(str1.isalpha())

str1="hello world"
print(str1.islower())

str1="we wish you a merry christmas"
print(str1.isprintable())
print(str1.isspace())

str1="World Health Organisation"
print(str1.istitle())

str1="To Kill a Mocking bird"
print(str1.istitle())

str1="Python is a Interpreted Language"
print(str1.swapcase())

str1="His name is Dan. He is an honest man."
print(str1.title())