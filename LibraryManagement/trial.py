class Library:

    def __init__(self,listOfBooks):
        self.book = listOfBooks

    def dispAvailableBooks(self):
        print("Available Books are ")
        for book in self.book:
            print(" *" + book)

    def bookIssue(self,bookName):
        if bookName in self.book:
            print(f"You have been Issued {bookName} ")
            self.book.remove(bookName)
            return True
        else:
            print("Book is not available in Library")
            return False

    def bookReturn(self,bookName):
        self.book.append(bookName)
        print("Thanks for returning a book and choosing Central Library")

class Student:

    def IssueBook(self):
        self.book = input("Enter the name of book you want to be issued: ")
        return self.book

    def ReturnBook(self):
        self.book = input("Enter the name of book you want to return: ")
        return self.book

if __name__ == '__main__':
    centralLib = Library(["Algorithams","Django","Computer Networks","DataBase"])
    student = Student()

    while True:

        welcomeMsg = '''
        ===== Welcome To The Central Library =====
        1. List of Books
        2. Issue Book
        3. Add/Return Book
        4. Exit
        '''

        print(welcomeMsg)

        a = int(input("Enter the Choice : "))

        if a == 1:
            centralLib.dispAvailableBooks()
        if a == 2:
            centralLib.bookIssue(student.IssueBook())
        if a == 3:
            centralLib.bookReturn(student.ReturnBook())
        if a == 4:
            print("Thanks for Choosing Central Library")
            exit()

