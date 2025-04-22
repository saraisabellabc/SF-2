'''
Design and implement an OOP hierarchy that will allow you to build a Car and an ElectricCar objects.  

A Car object is initialized with attributes make, model, year, odometer_reading. With a Car object we should be able to do the following:
--> print a Car descriptive with the make, the model, the year all separated by a space and each should start with a capital letter
--> allow functionality of reading the odometer, overwriting the current value of the odometer with another provided value, update the current value of the odometer by a given value. 

An ElectricCar object is initialized with attributes make, model, year, battery where the battery size is set to 40.  With an ElectricCar object we should be able to do the following: 
--> print a descriptive with the make, the model, the year all separated by a space and each should start with a capital letter
--> print a descriptive that this car has no gas tank
--> print a descriptive on the car battery size
--> allow functionality to change the battery with a bigger battery size
--> allow functionality to print a descriptive the range in mileage on full battery depending on the battery size.  If the battery size is 40, then the mileage is 150, if the battery size is 65, then the mileage is 225.  
'''

from car import Car 
from battery import Battery

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # third class is battery 
        self.battery_size = Battery()
        

    def fillGazTank(self) -> None:
        print('This car has no gaz tank')


if __name__ == '__main__':
    my_car = ElectricCar('Honda', 'Civic', 2020)
    print(my_car)

    my_car.battery.describeBattery()





