class Animal:
    def __init__(self, name: str, age: int, species: str):
        """
        Инициализация объекта класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        :param species: Вид животного.
        """
        self.name = name
        self.age = age
        self.species = species
        self._health = 100  # Приватный атрибут, представляющий здоровье животного

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта класса Animal.

        :return: Строковое представление объекта.
        """
        return f"Animal(name={self.name}, age={self.age}, species={self.species})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта класса Animal.

        :return: Официальное строковое представление объекта.
        """
        return f"Animal(name='{self.name}', age={self.age}, species='{self.species}')"

    def make_sound(self) -> str:
        """
        Возвращает звук, издаваемый животным.

        :return: Звук, издаваемый животным.
        """
        return "Some generic animal sound"

    def _check_health(self) -> int:
        """
        Возвращает текущее состояние здоровья животного.

        :return: Текущее состояние здоровья.
        """
        return self._health

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация объекта класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age, species="Dog")
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта класса Dog.

        :return: Строковое представление объекта.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта класса Dog.

        :return: Официальное строковое представление объекта.
        """
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"

    def make_sound(self) -> str:
        """
        Возвращает звук, издаваемый собакой.

        :return: Звук, издаваемый собакой.

        Причина перегрузки: Собаки издают специфический звук "Woof", который отличается от общего звука животного.
        """
        return "Woof"

    def fetch(self, item: str) -> str:
        """
        Возвращает действие собаки, приносящей предмет.

        :param item: Предмет, который собака приносит.
        :return: Действие собаки, приносящей предмет.
        """
        return f"{self.name} fetches the {item}"

# Пример использования
animal = Animal(name="Generic Animal", age=5, species="Unknown")
print(animal)
print(repr(animal))
print(animal.make_sound())

dog = Dog(name="Buddy", age=3, breed="Golden Retriever")
print(dog)
print(repr(dog))
print(dog.make_sound())
print(dog.fetch("ball"))