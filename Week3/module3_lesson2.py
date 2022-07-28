
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
        self.car_seats = seats


car_methods= Car
print(car_methods.colour)  

print(car_methods.wheels)  

print(car_methods.year)  

print(car_methods.brand)  

print(car_methods.seats)  


y = [6,4,2]
x=[12,8,4]
for k in x:
    y.append(k)
print (y)


