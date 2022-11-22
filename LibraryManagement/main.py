class Library:

    def __init__(self,listOfBooks):
        self.book = listOfBooks

    def displayAvailableBooks(self):
        print("Books Available are: ")
        for book in self.book:
            print(" *" + book)

    def borrowBook(self,bookName):
        if bookName in self.book:
            print(f"{bookName} is Issued to you ")
            self.book.remove(bookName)
            return True
        else:
            print("This Book is not availabe in Library")
            return False

    def returnBook(self,bookName):
        self.book.append(bookName)
        print(f"Thanks for returning the book {bookName} and choosing Central Library")

class Student:

    def requestBook(self):
        self.book = input("Enter the name of book you want to be issued : ")
        return self.book

    def retnBook(self):
        self.book = input("Enter the name of book you want to return : ")
        return self.book

if __name__ == '__main__':
    centralLibrary = Library(["algorithams","django","DataBase","Networks"])
    student = Student()
    while(True):

        welcomeMsg = ''' 
        ====== Welcome To the Central Library =======
        Please Choose an option
        1. Listing all the Books
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print(welcomeMsg)

        a = int(input("Enter the Choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.retnBook())
        elif a == 4:
            print("Thanks for choosing Central Library! Have a great day ahead")
            exit()
        else:
            print("Invalid Choice!")

