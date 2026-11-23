print("WELCOME TO NUMBER GUESSING GAME!!"
      "you gonna have 10 chances and you need to guess the number")
print("the number is between 50 to 100")
a=10
print(f"you have {a}attempts")
real=85
print("press 0 and enter to quit the game")
while 0<a<=10:
    guess=int(input("enter your guessed number:"))
    if guess>real:
        print("TRY AGAIN!!try for lower")
        a=a-1
        print(f"you have {a} attempts more ")
    elif guess < real:
        print("ITS WRONG!! try for higher")
        a=a-1
        print(f"you have{a}attempts")
    elif guess==0:
        print("THANKYOU FOR QUITTING THE GAME")
        break
    else:
        print("congratulations!! YOU GUESSED THE NUMBER CORRECTLY!")
        break
print("OOPS!! THE CHANCES ARE OVER. RESTART THE GAME...")

