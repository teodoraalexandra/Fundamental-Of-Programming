from domain.Car import Car

class CarValidator:
    def validate(self, car):
        if type(car) != Car:
            raise TypeError("Can only validate cars")

        errors = []

        if type(car.id) != int or car.id <= 0:
            errors.append("Wrong id type or value")
        if len(car.license) == 0:
            errors.append("Empty license")
        if len(car.make) == 0:
            errors.append("Empty make")
        if len(car.model) == 0:
            errors.append("Empty model")
        return errors

c = Car(-11, '', '', '')
cv = CarValidator()
print(cv.validate(c))