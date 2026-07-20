# MAGIC METHOD:
#              Dunder methods (double underscore) __init__, __str__, __eq__.
#              They are automatically called by many of python's built in operations.
#              They allow developers to define or customise the behaviour of objects.

class Book:
    def __init__(self, title, author, num_pages):  # for memory location save
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):  # for string 
        return f" {self.title} by {self.author}"
    
    def __eq__(self, other):   # for comparison
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):  # for less than
        return self.num_pages < other.num_pages 
    
    def __add__(self, other):  # for addition
        return self.num_pages + other.num_pages 
    
    def __contains__(self, keyword):  # searching any word in the function
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author 
        elif key == "num_pages":
            return self.num_pages
        else:
            return "Not Found"



book1 = Book("Harry potter","J.K Rowling", 418)
book2 = Book("Harry potter 1","J.K Rowling", 418)
book3 = Book("Harry potter 2","J.K Rowling", 418)

print(book1)
print(book1 == book2)
print(book2 < book3)
print(book2 + book3)
print("Harry" in book1)
print(book1['num_pages'])

