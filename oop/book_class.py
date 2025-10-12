class Book:
    def __init__(self, title, author,year):
        self.title = title
        self.author = author
         self.year = year
        

    def __str__(self):
        return f"'{self.title}' by {self.author} in {self.year} "

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}, year={self.year}')"

book = Book("1984", "George Orwell" , "2004")

print(book)          
print(repr(book))
