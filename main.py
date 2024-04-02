class User:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age
    @age.getter
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age_value):
        if new_age_value < 0 or new_age_value > 120:
            raise ValueError('incorrect age value')
        else: self._age = new_age_value
