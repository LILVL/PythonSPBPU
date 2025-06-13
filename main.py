from task_1 import Book, Car, BankAccount

if __name__ == "__main__":
    book = Book("1984", "George Orwell", 328)
    car = Car("Toyota", "Corolla", 2020)
    account = BankAccount("John Doe", 1000.0)

    try:
     Book.read(-10)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     Car.drive(-50)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     BankAccount.withdraw(2000.0)
    except TypeError:
        print('Ошибка: неправильные данные')
