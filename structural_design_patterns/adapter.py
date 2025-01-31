# Adaptee
class Battery:
    def supply_power(self):
        return "Supplying 8 amps"

# Target Interface
class SocketClass:
    def supply_power_in_volts(self):
        raise NotImplementedError

# Adapter
class BatteryToSocketClassAdapter(SocketClass):
    def __init__(self, battery):
        self.battery = battery

    def supply_power_in_volts(self):
        amps = self.battery.supply_power()
        # Convert amps to volts (dummy calculation for example)
        volts = "Converting 8 amps to 100 volts"
        return volts

# Client code
battery = Battery()
adapter = BatteryToSocketClassAdapter(battery)

print(adapter.supply_power_in_volts())  # Output: Converting 8 amps to 120 volts
