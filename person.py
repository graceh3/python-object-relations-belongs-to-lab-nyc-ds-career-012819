# import car class here
from car import Car

class Person:

    _allp=[]
    
    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        Person.add_person(self)
        
    @classmethod
    def add_person(cls, person_instance):
        cls._allp.append(person_instance)
    
    @property
    def name(self):
        return self._name
    
    @property
    def occupation(self):
        return self._occupation
    
    @classmethod
    def has_oldest_car(cls):
        car_years = {}
        for car in Car._all:
            car_years.update({car.year:car.owner.name})
        keys = sorted([key for key in car_years.keys()])
        return car_years[keys[0]]

    @classmethod
    def drives_a(cls, make):
        return[(car.owner.name).split()[0].lower() for car in Car._all if car.make == make]
    
    def drives_same_make_as_me(self):
        make1 = ""
        name1 = ""
        result = []
        for car in Car._all:
            if car.owner.name == self._name: 
                make1 = car.make
        result.extend(self.drives_a(make1))
        result.remove(self._name.split()[0].lower())
        return result
        
    @classmethod
    def all_persons(cls):
        return cls._allp
        
        
        
        
        
        
        
            