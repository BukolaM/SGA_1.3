
##• Create an class called car
# • Give 5 attributes of the car class
# • Give 5 methods of the car class

class Car:
    colour = 'black'
    wheels = 4
    year = 2014
    brand = 'Ford'
    seats = 6 

    def car_colour(self, colour):
        self.colour = colour

    def car_wheels(self, wheels):
        self.wheels = wheels

    def car_year(self, year):
        self.year = year

    def car_brand(self, brand):
        self.brand = brand

    def car_seats(self, seats):
        self.seats = seats


car_obj = Car()
print(car_obj.colour)  

print(car_obj.wheels)  

print(car_obj.year)  

print(car_obj.brand)  

print(car_obj.seats)  

