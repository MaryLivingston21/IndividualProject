class ANIMAL:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def to_string(self):
        return self.name + ": a " + str(self.age) + " year old " + self.breed + '\n'

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_age(self):
        return self.age

    def __eq__(self, other):
        return self.name == other.name and self.breed == other.breed and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.breed, self.age))
