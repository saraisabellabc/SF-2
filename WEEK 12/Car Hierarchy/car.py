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
class Car:
    def __init__(self, make, model, year, odometer = 0):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer = odometer

    def __repr__(self) -> str:
        return f'{self.make.capitalize()} {self.model.capitalize()} {self.year} ' # capitalize()
    
    # def odometerReading():

    

    
    def changeValue(self, value):
        self.odometer = value


    def updateOdometer(self, mileage : int) -> None:
        if mileage >= self.odometer:
            self.odometer = mileage 
        else:
            print('it has to be higher')

    def changeBattery(self, battery) -> None:
        self.battery_size = battery
    

# if __name__ == '__main__':
