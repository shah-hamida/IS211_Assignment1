class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        pass


    def display(self):
        print((self.title), "written by", (self.author))
        pass



if __name__ == "__main__":
    a = Book (title = "Harry Potter and the Goblet of Fire" , author = "J.K Rowling")
    b = Book (title = "Ivanhoe: A Romance" , author = "Walter Scott")


    a.display()
    b.display()
