class Vehicle:
    # all measurements are in miles or miles per hour
    def __init__(self, seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed):
        self.seats = seats
        self.max_driving_distance = max_driving_distance
        self.fuel_source = fuel_source
        self.has_all_wheel_drive = has_all_wheel_drive
        self.top_speed = top_speed

    def drive(self):
        print("Vroom Vroom")

    def turn(self, direction):
        print(f"Turning {direction}")

    def stop(self):
        print("The vehicle stops")


class model3performance(Vehicle):
    def __init__(self, seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed):
        super().__init__(seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed )

    def drive(self):
        print("The murky black Model 3 drives past silently")

    def turn(self, direction):
        print(f"The car turns itself to the {direction}")

    def stop(self):
        print("The car stops itself")


class modelSperformance(Vehicle):
    def __init__(self, seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed):
        super().__init__(seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed)

    def drive(self):
        print("The murky black Model S drives past silently")

    def turn(self, direction):
        print(f"The car turns itself to the {direction}")

    def stop(self):
        print("The car stops itself")


class mclaren720Sperformance(Vehicle):
    def __init__(self, seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed):
        super().__init__(seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed)

    def drive(self):
        print("The murky black 720S drives past loudly")


class huracánPerformante(Vehicle):
    def __init__(self, seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed):
        super().__init__(seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed)

    def drive(self):
        print("The murky black Performante drives past loudly")


class rangeRoverSport(Vehicle):
    def __init__(self, seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed):
        super().__init__(seats, max_driving_distance, fuel_source, has_all_wheel_drive, top_speed)

    def drive(self):
        print("The murky black Range Rover Sport drives past loudly")



Model3 = model3performance(5, 322, "electric", True, 145)
ModelS = modelSperformance(5, 348, "electric", True, 163)
Mclaren = mclaren720Sperformance(2, 418, "gas", False, 212)
Huracán = huracánPerformante(2, 380, "gas", True, 209)
RangeRover = rangeRoverSport(7, 367, "gas", True, 130)

cars = [Model3, ModelS, Mclaren, Huracán, RangeRover]

for car in cars:
    car.drive()
    car.turn("right")
    car.stop()