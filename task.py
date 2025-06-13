# TODO: Подробно описать три произвольных класса


class Book:
    def __init__(self, title: str, author: str, pages: int):
        if not title or not author:
            raise ValueError("Title and author must be non-empty strings.")
        if pages <= 0:
            raise ValueError("Number of pages must be a positive integer.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> str:
        """
        Simulates reading a certain number of pages.

        Args:
            pages_read (int): The number of pages read.

        Returns:
            str: A message indicating the number of pages read.

        Raises:
            ValueError: If pages_read is not a positive integer.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(50)
        'You have read 50 pages of 1984 by George Orwell.'
        """
        if pages_read <= 0:
            raise ValueError("Number of pages read must be a positive integer.")
        return f"You have read {pages_read} pages of {self.title} by {self.author}."

    def get_summary(self) -> str:
        """
        Returns a summary of the book.

        Returns:
            str: A summary of the book.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_summary()
        '1984 by George Orwell has 328 pages.'
        """
        return f"{self.title} by {self.author} has {self.pages} pages."

    def is_long_book(self, threshold: int = 300) -> bool:
        """
        Checks if the book is considered long based on a page threshold.

        Args:
            threshold (int): The page count threshold to consider a book long.

        Returns:
            bool: True if the book is long, False otherwise.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.is_long_book()
        True
        """
        return self.pages > threshold

class Car:
    def __init__(self, make: str, model: str, year: int):
        if not make or not model:
            raise ValueError("Make and model must be non-empty strings.")
        if year < 1886:  # The first car was invented in 1886
            raise ValueError("Year must be 1886 or later.")
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Simulates starting the car's engine.

        Returns:
            str: A message indicating the engine has started.

        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.start_engine()
        'The engine of Toyota Corolla (2020) has started.'
        """
        return f"The engine of {self.make} {self.model} ({self.year}) has started."

    def drive(self, distance: float) -> str:
        """
        Simulates driving the car for a certain distance.

        Args:
            distance (float): The distance to drive in kilometers.

        Returns:
            str: A message indicating the distance driven.

        Raises:
            ValueError: If distance is not a positive number.

        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.drive(100.5)
        'You have driven 100.5 km in your Toyota Corolla (2020).'
        """
        if distance <= 0:
            raise ValueError("Distance must be a positive number.")
        return f"You have driven {distance} km in your {self.make} {self.model} ({self.year})."

    def get_age(self, current_year: int = 2023) -> int:
        """
        Calculates the age of the car.

        Args:
            current_year (int): The current year.

        Returns:
            int: The age of the car.

        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.get_age()
        3
        """
        return current_year - self.year

class BankAccount:
    def __init__(self, owner: str, balance: float):
        if not owner:
            raise ValueError("Owner must be a non-empty string.")
        if balance < 0:
            raise ValueError("Balance must be a non-negative number.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """
        Deposits a certain amount into the bank account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            float: The new balance after the deposit.

        Raises:
            ValueError: If amount is not a positive number.

        >>> account = BankAccount("John Doe", 1000.0)
        >>> account.deposit(500.0)
        1500.0
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws a certain amount from the bank account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            float: The new balance after the withdrawal.

        Raises:
            ValueError: If amount is not a positive number or exceeds the balance.

        >>> account = BankAccount("John Doe", 1000.0)
        >>> account.withdraw(200.0)
        800.0
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        """
        Returns the current balance of the bank account.

        Returns:
            float: The current balance.

        >>> account = BankAccount("John Doe", 1000.0)
        >>> account.get_balance()
        1000.0
        """
        return self.balance