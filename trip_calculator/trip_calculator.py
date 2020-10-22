'''

Create a python script that asks a user questions in the command line. The script should follow the outlined specs.

## Specs

Receive the following arguments from the user:

- kilometers to drive
- liters-per-kilometer usage of the car
- price per liter of fuel

Calculate the cost of the trip and display it to the user in the console.

'''


km_drive = input("Please insert the number of kms to drive: ")
# Changed from L/km to L/100 km because this is more conventional
efficiency_car = float(input("Please insert the liter per 100 km of your car: "))
price_fuel = float(input("Please insert the price of fuel per liter: "))

cost_trip = (efficiency_car * float(km_drive)/100) * price_fuel
print(round(cost_trip, 2))