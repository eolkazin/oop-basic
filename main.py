class Animals:
    """Animals class

    This class contains the base information for Animals.
    """

    def __init__(self, name, age):
        """Initialize Animals class

        Args:
            name (str): Name of the animal
            age (int): Age of the animal
        """
        self.name = name
        self.age = age
        self.legs = 4

    def info(self):
        """Prints the attributes of the animal.

        This method prints the name, age, and number of legs of the animal.
        """
        print(self.name, self.age, self.legs)

class Dog(Animals):
    def __init__(self, name, age):
        """Initialize Dog class

        Args:
            name (str): Name of the dog
            age (int): Age of the dog
        """
        super().__init__(name, age)
        self.legs = 4

    def info(self):
        """Prints the attributes of the dog.

        This method prints the name, age, and number of legs of the dog.
        """
        print(self.name, self.age, self.legs)

class Cat(Animals):
    def __init__(self, name, age):
        """Initialize Cat class

        Args:
            name (str): Name of the cat
            age (int): Age of the cat
        """
        super().__init__(name, age)
        self.legs = 4

    def info(self):
        """Prints the attributes of the cat.

        This method prints the name, age, and number of legs of the cat.

        Prints:
            str: Name of the cat
            int: Age of the cat
            int: Number of legs of the cat
        """
        print(self.name, self.age, self.legs)


animals1 = Dog("Dog", 2)
animals1.info()
animals2 = Cat("Cat", 4)
animals2.info()
