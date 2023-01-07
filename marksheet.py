math = int(input("Enter maths number: "))
phy = int(input("Enter physicss number: "))
chem = int(input("Enter chemistry number: "))

total=math + phy + chem
print(total, 'out of 300')
per = int(total/300*100)
print()
if per < 33:
    print("fail")
elif per >= 33 and per <= 45:
    print("third division")
elif per >= 46 and per <= 60:
    print("second division ")
else:
    print("first divison***")
print()
print("with ",per ,"precent ")


    