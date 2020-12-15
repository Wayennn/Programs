class Plane:
    def __init__(self, name, airspeed = 0, altitude = 0, direction = 0, vspeed = 0, fuel = 0):
        self.name = str(name)
        self.airspeed = airspeed
        self.altitude = altitude
        self.direction = direction
        self.vspeed = vspeed
        self.fuel = fuel

    def engines(self, throttle):
        self.airspeed = throttle
    def elevator(self, elv):
        self.vspeed = elv

def status():
    for i in range(len(names)):
        print(flight[i].name)
        print("Airspeed = " + str(flight[i].airspeed) + " Altitude = " + str(flight[i].altitude))

names = ["B777", "A380", "B787"]
flight = [Plane(i) for i in names]
status()
flight[0].engines(100)
status()