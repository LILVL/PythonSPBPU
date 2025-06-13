BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
class Book:
    id_ = 0
    name = None
    pages = 0

    def __init__(self, id_: int = 0, name: str = None, pages: int = 0):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return (f'Книга "{self.name}"')

    def __repr__(self):
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"

class Library:
    books = []

    def __init__(self, books=None):
        self.books = books
        if books == None: self.books = []

    def get_next_book_id(self) -> int:
        return len(self.books) + 1

    def get_index_by_book_id(self, Id):
        for a in enumerate(self.books):
            if (Id == a[0]):
                return a[0]
        raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
