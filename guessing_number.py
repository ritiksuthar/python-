import random 

rannum = random.randrange(1,30)
while True:
    print("*****************************start*****************************************")
    print("enter the number between 1 to 30")
    for i in range(0,5):
        
        num = int(input("Enter your number: "))
        if num == rannum:
            print(" hurrry...you are win ")
            break
        elif num > rannum:
            print("your number is big..")
        elif num < rannum:
            print("you are number is small..")

        print("oops..you are lost try again next time i hope you will be win... thankyou   ")
    print()
    print("*******************************end***************************************")