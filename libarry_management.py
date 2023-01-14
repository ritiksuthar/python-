class Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict={}

    def displayBook(self):
        print(f"We have following books in our libraary:{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-book Database has been update you can take thee book now")
        else:
            print(f"Book is allready in use by {self.lendDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to your list")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__=="__main__":
    dnyanesh=Library(["python","c++","java","php","ruby","R"],"THRITIKSUTHAR")
    while 1:
        print("###########################THERITIKSUTHAR LIBRARY###########################")
        print(f"welcome to the {dnyanesh.name} libray.Enter your choice to continue")
        print("1.Display Books")
        print("2 lend books")
        print("3 Add book")
        print("4 Return book")
        print("############################################################################")
        
        user_choice=input()
        if user_choice not in ["1","2","3","4"]:
            print("not a valid option")
            print("press q to quit and c to contiou")
            user_choice=input()
            if user_choice=="q":
                exit()
            if user_choice=="c":
                continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            dnyanesh.displayBook()
        elif user_choice==2:
            book = input("Enter the name  of the book u want to  lend")
            user=input("Enter you name")
            dnyanesh.lendBook(user,book)
        elif user_choice==3:
            book=input("Enter the name  of the book u want to  add ")
            dnyanesh.addBook(book)
        elif user_choice==4:
            book=input("Enter the name  of the book u want to  return ")
            dnyanesh.returnBook(book)

        