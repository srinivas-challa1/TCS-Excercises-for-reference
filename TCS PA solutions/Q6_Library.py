class Book:
    def __init__(self, book_id, book_name):
        self.book_id = book_id
        self.book_name = book_name


class Library:
    def __init__(self, library_id, address, book_list):
        self.library_id = library_id
        self.address = address
        self.book_list = book_list

    def count_books(self, character):
        count = 0
        for book in self.book_list:
            if(book.book_name.startswith(character)):
                count += 1
        return(count)

    def remove_books(self, blist):
        for book in blist:
            for b in self.book_list:
                if(b.book_name == book):
                    self.book_list.remove(b)


if __name__ == "__main__":
    books = []
    count = int(input())
    for _ in range(count):
        bid = int(input())
        bname = input()
        b = Book(bid, bname)
        books.append(b)
    L = Library(135, 'Guntur', books)
    char = input()
    count = int(input())
    names = []
    for _ in range(count):
        names.append(input())
    print(L.count_books(char))
    L.remove_books(names)
    for i in L.book_list:
        print(i.book_name)
