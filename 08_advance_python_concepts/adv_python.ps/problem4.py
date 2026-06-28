class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        return(f"{self.title} by {self.author}")

    def __len__(self):
        return len(self.title)
    
b1=Book("lala hi bhagwan","lord lala")
print(b1)
print(len(b1))

b2=Book("chacha hi shaitan","lord lala")
print(b2)
print(len(b2))