import random


class Car:
    def __init__(self, model, color):
        self.fuel = random.randint(1, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        if self.fuel > 0:
            actual_distance = min(distance, self.fuel)
            self.trip_distance += actual_distance
            self.fuel -= actual_distance


cars = [
    Car('BMW', 'Black'),
    Car('Honda', 'Green'),
    Car('Renault', 'Red')
]

desired_dist = 50

winner = None
while winner is None:
    for car in cars:
        if car.fuel > 0:
            distance = random.randint(0, 9)
            car.move(distance)
            print(
                f'{car.model} {car.color} came {distance}, general distance: {car.trip_distance}, fuel remnant: {car.fuel}')

            if car.trip_distance >= desired_dist:
                winner = car
                break


print(f'\nWinner: {winner.model} {winner.color}, distance: {winner.trip_distance}')

print('\nResults:')
for car in cars:
    print(f'{car.model} {car.color}: came {car.trip_distance}, fuel remnant {car.fuel}')