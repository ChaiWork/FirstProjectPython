#Magic method = dunder method (double underscore) __init__,__str__,__eq__
# they are automatically called by many python build in operation
# they allow developers to define or customize the behavoir of objects


class Book:
    
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author =author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key '{key}' was not found"
        
book1 = Book("The Hobbit","J.R.R Tolkien",310)
book2 = Book("The Hobbit","Rahman",100)
book3 = Book("Princess","Luis",123)

print(book1)
print(book1 == book2)
print(book2 < book3)
print(book2 + book3)
print("Princess" in book3)

print(book1['title'])
print(book1["author"])
print(book1["num_pages"])
print(book1["audio"])