
class Person:
    def __init__(self, name, age, email):
        self._name = None
        self._age = None
        self._email = None

        self.name = name
        self.age = age
        self.email = email

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value:str) -> None:
        if not isinstance(value, (str)):
            raise TypeError(
                f"Name must be string not {type(value)}")
        self._name = value
    @property
    def age(self) -> float:
        return self._age
    
    @age.setter
    def age(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Age must be either int or float not {type(value)}")
        if not (0 < value < 125):
            raise ValueError("Your age muct be between 1 and 124")
        self._age = value
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value:str) -> None:
        if not "@" in value:
            raise ValueError("Your email adress must contain a \"@\"")
        self._email = value

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age}, email={self.email})"
    
    def say_hello(self):
        print(f"Hi, my name is{self.name}, I am {self.age} years old, my email adress is {self.email}")

p = Person("Pernilla", 32, "pernilla@gmail.com")
print(p)
