"""
1. Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
2. Drive the taxi 40 km
3. Print the taxi's details and the current fare
4. Restart the meter (start a new fare) and then drive the car 100 km
5. Print the details and the current fare
"""
from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
my_taxi.drive(40)
print(my_taxi)
print(f"Current fare is {my_taxi.get_fare()}")

my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(f"Current fare is {my_taxi.get_fare()}")