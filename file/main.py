class Book:
    def __init__(self, name, page_count, price):
        self.name = name
        self.page_count = page_count
        self.price = price

    def increase_pages(self):
        self.page_count += 10

    def decrease_price(self):
        if self.page_count > 100:
            self.price /= 2

    def __str__(self):
        return f"Book: {self.name}, Pages: {self.page_count}, Price: ${self.price}"

books = []
for i in range(5):
    print(f"\n{i+1}-kitob ma'lumotlarini kiriting:")
    name = input("Kitob nomi: ")
    page_count = int(input("Kitobning sahifalar soni: "))
    price = float(input("Kitobning narxi: $"))

    book = Book(name, page_count, price)
    books.append(book)

for book in books:
    book.increase_pages()

for book in books:
    if book.page_count > 100:
        book.decrease_price()

print("\nKitoblar haqida ma'lumotlar:")
for book in books:
    print(book)
