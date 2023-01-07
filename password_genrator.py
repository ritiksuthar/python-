import random 
import array
while True:
    
        max_lan = 12
        digit = ['0','1','2','3','4','5','6','7','8','9',]
        lo_charcters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
        up_charcters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
        symbols = ['!','@','$','%','^','&','*','(',')','-','+','~','<','>','?','/',':',';','|',]

        combaind_list = digit + lo_charcters + up_charcters + symbols

        random_digit = random.choice(digit)
        #print(random_digit)
        random_loChar = random.choice(lo_charcters)
        #print(random_loChar)
        random_upChar = random.choice(up_charcters)
        #print(random_upChar)
        random_symbol = random.choice(symbols)
        #print(random_symbol)

        temp_pass = random_digit + random_loChar + random_upChar + random_symbol 
        #print(temp_pass)

        for x in range (4):
            temp_pass = temp_pass + random.choice(combaind_list)
        # print (x)
        #print( temp_pass)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
        password = ""
        #print(temp_pass_list)
        for x in temp_pass_list:
                password = password + x

        print("your password is :", password)