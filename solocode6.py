class Vehicle:
    def __init__(self, name, fuel_capacity, cost_per_gallon, mpg):
        self._name = name
        self._fuel_capacity = fuel_capacity
        self._cost_per_gallon = cost_per_gallon
        self._mpg = mpg

    @property
    def name(self):
        return self._name

    @property
    def range(self):
        return self._fuel_capacity * self._mpg

    @property
    def cost_per_mile(self):
        return self._cost_per_gallon / self._mpg



vehicles = [
    Vehicle("Car", 14, 3.50, 30),
    Vehicle("Bus", 100, 3.20, 8),
    Vehicle("Train", 500, 3.00, 15),
    Vehicle("Plane", 5000, 5.50, 5)
]


vehicles_sorted = sorted(vehicles, key=lambda v: v.cost_per_mile)


print(f"{'Name':<10} {'Range':<12} {'Cost per Mile':<15}")
print("-" * 37)

for v in vehicles_sorted:
    print(f"{v.name:<10} {v.range:<12.2f} {v.cost_per_mile:<15.4f}")