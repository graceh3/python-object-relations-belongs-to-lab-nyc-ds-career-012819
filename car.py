class Car:

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)
        
    @classmethod
    def add_car(cls, car_instance):
        cls._all.append(car_instance)
        return cls._all
        
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year
    
    @property
    def owner(self):
        return self._owner
    
    @make.setter
    def make(self, new_make):
        self._make = new_make
        
    @model.setter
    def model(self, new_model):
        self._model = new_model
    
    @year.setter
    def year(self, new_year):
        self._year = new_year
        
    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner
    
    @classmethod
    def all(cls):
        return cls._all
    
    @classmethod
    def cars_driven_by(cls, occupation):
        result = []
        for car in Car._all:
            if car.owner.occupation == occupation:
                result.append(car.owner.name.split()[0].lower())
        return result
   
