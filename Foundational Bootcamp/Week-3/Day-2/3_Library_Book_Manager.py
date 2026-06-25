class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn=isbn          
        self._title=title        
        self._author=author       
        self.__copies=copies   

    @property
    def available(self):
        return self.__copies

    def checkout(self, n):
        if n<=0:
            print("Invalid number of copies")

        if n>self.__copies:
            print("Not enough copies available")
        self.__copies-=n

    def return_book(self, n):
        if n<=0:
            print("Invalid number of copies")
        else:
            self.__copies+=n

b1=Book("978123456", "Python Basics", "Farhan", 10)
print("Title  :  ", b1._title)
print("Available  :  ", b1.available)
print()
b1.checkout(3)
print("After checkout  : ", b1.available)
print()
b1.return_book(2)
print("After return :  ", b1.available)
