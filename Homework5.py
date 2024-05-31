


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class AttributeMixin:
    @property
    def attributes(self):
         return f"name: {self.name}, surname: {self.surname}, age: {self.age}, university: {self.university}"

class Student(Person, AttributeMixin):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university



student = Student("Bilbo", "Baggins", 20, "technical university")
print(student.attributes)  
