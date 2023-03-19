import pyttsx3  #here we can import the pyttsx3 module and this module can 
                # convert the text into a speech

audio=pyttsx3.init() # here we can initillize the pyttsx3 in your program

audio.setProperty("rate",130)# Here  we can set the speed of words/minit
voice=audio.getProperty("voices") # Here we can explore the property of voice 
audio.setProperty("voice",voice[1].id)# Here we can ste the femal voice id is 1//male voice id is 0
audio.say("Welcome to SBI ATM")#The say method can contains the text // we can provide the string name 
audio.say("Please Enter your ATM pin")# where the string is decelared in your program
audio.runAndWait() # This function can make the speech audiable in your program
pin=int(input("::Enter your ATM pin::\n"))
pin1=9696 # And from here we start our ATM meachine code
def pin3():
    
    audio.setProperty("rate",120)
    voice=audio.getProperty("voices")
    audio.setProperty("voice",voice[1].id)
    audio.say("Your pin is incorrect, Please reenter your pin")
    audio.runAndWait()
    audio.stop()
   # pin=int(input("::Enter your ATM pin::\n"))
if(pin!=pin1):
    pin3()    
    pin=int(input("::Enter your ATM pin::\n"))
   
if(pin==pin1):
    print("::::::::MENU::::::::")
    print("::1::Check Balance::")
    print("::2::Cash Withdraw::")
    print("::3::Change Pin::")
    print("::4::Cash Deposit::")
    audio.setProperty("rate",120)
    voice=audio.getProperty("voices")
    audio.setProperty("voice",voice[1].id)
    audio.say("Select option form menu")
    audio.runAndWait()
    audio.stop()
    
    print("Select option form menu")
    n=(int(input()))
    Balance=20000
    check_vab=1
    Cash_w=2
    Change_p=3
    Cash_de=4

    if(n==1):
        print("The Balance=",Balance)
    elif(n==2):
        audio.setProperty("rate",120)
        voice=audio.getProperty("voices")
        audio.setProperty("voice",voice[1].id)
        audio.say("Enter your amount")
        audio.runAndWait()
        audio.stop()
        amount=int(input("Enter your amount"))
        if(amount<Balance):
            audio.setProperty("rate",120)
            voice=audio.getProperty("voices")
            audio.setProperty("voice",voice[1].id)
            audio.say("Please take your cash")
            audio.runAndWait()
            audio.stop()
        else:
            audio.setProperty("rate",120)
            voice=audio.getProperty("voices")
            audio.setProperty("voice",voice[1].id)
            audio.say("Sorry your balance is insufficiant")
            audio.runAndWait()
            audio.stop()
    elif(n==3):
        audio.setProperty("rate",120)
        voice=audio.getProperty("voices")
        audio.setProperty("voice",voice[1].id)
        audio.say("Please Enter your old pin")
        audio.runAndWait()
        print("Enter your old pin")
        num=int(input())
        audio.setProperty("rate",120)
        voice=audio.getProperty("voices")
        audio.setProperty("voice",voice[1].id)
        audio.say("Please Enter your new pin")
        audio.runAndWait()
        print("Enter the new pin")
        num1=int(input())
        pin=num1
        audio.setProperty("rate",120)
        voice=audio.getProperty("voices")
        audio.setProperty("voice",voice[1].id)
        audio.say("Your pin has been changed successfully")
        audio.runAndWait()
        print("Your pin has been change successfully")
    elif(n==4):
        audio.setProperty("rate",120)
        voice=audio.getProperty("voices")
        audio.setProperty("voice",voice[1].id)
        audio.say("Enter your amount to deposit")
        audio.runAndWait()
        print("Enter your amount to deposit")
        A=int(input())
        print("Total Balance=",Balance+A)
else:
    pass
print("")
audio.setProperty("rate",120)
voice=audio.getProperty("voices")
audio.setProperty("voice",voice[1].id)
audio.say("Thank You for Visiting")
audio.runAndWait()
print("Thank you")
