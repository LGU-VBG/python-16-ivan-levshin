class Person: 
    def __init__(self,surname,name):
        self._name = name
        self._surname = surname
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self.name = value

    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self,value):
        self._surname = value

    @property
    def fullname(self):
        return f"{self._name}{self._surname}"
    
    @fullname.setter
    def fullname(self,value):
        name_parts = value.split(' ', 1)
        self._name = name_parts[0]
        self.surname = name_parts[1] if len(name_parts) > 1 else ""

person = Person('Mike', 'Pondsmith')
person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)