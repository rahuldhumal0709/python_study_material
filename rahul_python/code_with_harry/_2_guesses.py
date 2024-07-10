num=18
nog=1 # No. of guesses
while nog<=9:
    guess=int(input("Please enter correct number : "))
    if guess >num:
        print("Please enter small no as you entered.",end=" ")
        print("No. of Guesses left",9-nog)
    elif guess < num :
        print("Please enter large no as you entered.",end=" ")
        print("No. of Guesses left",9-nog)
    elif num==guess:
        print("Congrates,Entered number is matched.",end=" ")
        print("No. of Guesses you attemped",nog)
        break
    nog+=1
print("Game over")