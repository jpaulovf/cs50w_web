class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Flight():

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

p = Point(2, 8)
print(p.x)
print(p.y)

flight = Flight(3)

people = ["Ash", "Misty", "Brock", "Prof. Oak"]

for person in people:
    if flight.add_passenger(person):
        print(f"Passenger {person} added successfully!")
    else:
        print(f"No room for {person}!")