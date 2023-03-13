username= input ("whats your username:")
not_good_username =["fuck","","!","@","#","$","%"]
while username in not_good_username:
    print("sorry username is not good")
    username= input ("whats your username:")
password= input ("whats your password:")
not_good_password =["","!","#","$","%","&","*",]
while password in not_good_password:
    print("sorry password is not good")
    password= input ("whats your password:")
age = input ("enter your age:")
not_good_age =["","!","#","$","%","&","*","1","2","3","4","5","6","7"]
while age in not_good_age:
    print("sorry age is not good")
    age = input ("enter your age:")
print ("--------------------------------------------------")  

colors =["green","blue","white","gray","black","red","yellow","orange","pink","aque"]
cs =input("say a number from 0 to 9 and you will get a color:")
colors_num =["0","1","2","3","4","5","6","7","8","9"]
while cs not in colors_num:
    print ( "your number is wrong!" )
    cs =input("say a number from 0 to 9 and you will get a color:")
if cs == "0":
    print ( "your random color is " + colors[0] )
elif cs== "1":
    print ( "your random color is " + colors[1] )
elif cs== "2":
    print ( "your random color is " + colors[2] )
elif cs== "3":
    print ( "your random color is " + colors[3] )
elif cs== "4":
    print ( "your random color is " + colors[4] )
elif cs== "5":
    print ( "your random color is " + colors[5] )
elif cs== "6":
    print ( "your random color is " + colors[6] )
elif cs== "7":
    print ( "your random color is " + colors[7] )
elif cs== "8":
    print ( "your random color is " + colors[8] )
elif cs== "9":
    print ( "your random color is " + colors[9] )
print ("--------------------------------------------------")

num1= input ("please insert the first number " + username+":")
not_num1 =["","a"]
num2= input ("please insert the second number " + username+":")
operation= input ("please insert your desired operation among: +,-,*,/,**: ")
not_oan =["+","-","*","/","**"]
while operation not in not_oan:
    print ("oops its wrong, please try again :)")
    operation= input ("please insert your desired operation among: +,-,*,/,**: ")
if operation == "+":
    result = float(num1)+ float(num2)
elif operation == "-":
    result = float(num1)- float(num2)
elif operation == "*":
    result = float(num1)* float(num2)
elif operation == "/":
    result = float(num1)/ float(num2)
elif operation == "**":
    result = float(num1)** float(num2)
else:
    result=("oops its wrong, please try again :)")
    
print (result)
print ("--------------------------------------------------")

a = input("player1:please enter your number from (1-1000)")
a =int(a)
while a > 1000 or a < 1 :
    print ("is big or smal")
    a = input("player1:please enter your number from (1-1000)")
    a =int(a)
is_correct = False
trycount = 0
while trycount < 10 and  is_correct == False:
    b =int(input("player2:please enter your number from (1-1000)"))
    if b == a:
        print ("player2:you won")
        is_correct = True
    
    elif b > a :
        print("it should be smaller")
        trycount += 1
    else:
        print ("it should be bigger")
        trycount += 1
if  is_correct == False:
    print ("player2:you lost")
