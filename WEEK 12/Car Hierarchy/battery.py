class Battery:
    def __init__(self, battery_size : int = 40):
        self.battery_size = battery_size

    def describeBattery(self):
        print(f'This car has {self.battery_size}-kWH battery')

    def getRange(self) -> str:
        range = -1 
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f'This car can go about {range} miles on a full charge')

    def changeBattery(self, new_size) -> None:
        self.battery_size = new_size



    