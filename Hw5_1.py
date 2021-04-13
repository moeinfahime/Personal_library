class Bookshelf:
    def __init__(self, title, author, publish_year, pages, language, price):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.left_pages = pages
        self.update_pages = pages

    def read(self, page):
        self.left_pages = self.pages - page
        self.update_pages = self.pages - self.left_pages
        return f"you have read {self.update_pages} "f"more pages from {self.title}. " \
               f"There are {self.left_pages} pages left."

    def get_status(self, page):
        self.left_pages = self.pages - page
        if self.left_pages == self.pages:
            return "no pages has been read yet"
        elif 0 < self.left_pages < self.pages:
            return "reading the book"
        elif self.left_pages == 0:
            return "all pages has been read"

    def __str__(self):
        return f"Title:{self.title} \nauthor(s):{self.author} \nPublish_year:{self.publish_year} " \
               f"\nPages(number of pages):{self.pages} \nLanguage:{self.language} \nPrice:{self.price}"


Nomber_Books = int(input('please input number of books:'))
List_books = []

for i in range(1, Nomber_Books + 1):
    title_book = input("Please enter a book title: ")
    author_book = input("Please enter author(s): ")
    publish_year_book = input("Please enter year of publish: ")
    pages_book = int(input("Please enter pages of book: "))
    language_book = input("Please enter language of book: ")
    price_book = input("Please enter a price book: ")
    page_ = int(input("Please enter pages read: "))
    book = Bookshelf(title_book, author_book, publish_year_book, pages_book, language_book, price_book)
    List_books.append(book)

for j in range(len(List_books)):
    print(j + 1, ')')
    print(List_books[j])
    print(book.read(page_))
    print(book.get_status(page_))
