import random

name = input("What's your name:")
print("Good Luck!", name )
words =['python', 'c', 'c++', 'java', 'visualBasic', 'javascript', 'ruby', 'swift', 'dotnet','php', 'kotlin'  ]
word = random.choice(words)
#print(word)
print("Guss the charcters..! hint-> programing language:")
gusses = ''
turns =12

while turns > 0:
    failed = 0
    for char in word :
        if char in gusses:
            print(char, end= " ")
        else:
            print("_", end = " ")
            failed = failed+1
    if failed==0:
        print("  your Win..")
        print("The word is:", word)
        break
        
    print()
    guss = input("\n guss the charcter :")
    gusses += guss
    

    if  guss not in word :
        turns-=1
        print("Wrong")
        print("you have ",+ turns ,'more gusses ')
        if  turns ==0:
            print("you loose")
    print(word)
    
    
    
    
    