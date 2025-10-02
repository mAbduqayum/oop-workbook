# Exercise: Smart Home System - Composition and Aggregation

Create a simple smart home system using composition and aggregation to demonstrate object relationships.

## Key Concepts

**Composition (HAS-A)**: When one object contains another as an essential part
- Device HAS-A PowerMonitor (can't exist without it)

**Aggregation (HAS-A)**: When one object contains others but they can exist independently
- SmartHome HAS devices (devices can exist without the home system)

## Requirements

### 1. `PowerMonitor` Class (Used in Composition)
- **Attributes:**
  - `base_watts` (float): Base power consumption
  - `current_watts` (float): Current power usage

- **Methods:**
  - `__init__(base_watts)`: Initialize with base consumption
  - `update_power(watts)`: Update current consumption
  - `get_usage()`: Return current power usage

### 2. `Device` Class (Base Device)
- **Attributes:**
  - `device_id` (string): Unique identifier
  - `name` (string): Device name
  - `is_on` (boolean): Power state
  - `power_monitor` (PowerMonitor): Power monitoring (composition)

- **Methods:**
  - `__init__(device_id, name, base_watts)`: Initialize device
  - `turn_on()`, `turn_off()`: Control power state
  - `get_status()`: Return device status
  - `get_power_usage()`: Return power consumption

### 3. Device Types (Simple Examples)

#### `Light` Class
- **Additional Attributes:**
  - `brightness` (int): Brightness level 0-100

- **Additional Methods:**
  - `set_brightness(level)`: Adjust brightness

#### `Thermostat` Class
- **Additional Attributes:**
  - `temperature` (float): Target temperature

- **Additional Methods:**
  - `set_temperature(temp)`: Set target temperature

#### `Camera` Class
- **Additional Attributes:**
  - `recording` (boolean): Recording status

- **Additional Methods:**
  - `start_recording()`, `stop_recording()`: Control recording

### 4. `SmartHome` Class (Uses Aggregation)
- **Attributes:**
  - `name` (string): Home name
  - `devices` (list): Collection of devices (aggregation)

- **Methods:**
  - `__init__(name)`: Initialize smart home
  - `add_device(device)`: Add device to home
  - `remove_device(device_id)`: Remove device from home
  - `get_total_power()`: Calculate total power usage
  - `list_devices()`: Show all devices and their status

## Example Usage

```python
# Create devices (each device HAS-A PowerMonitor - composition)
living_room_light = Light("L001", "Living Room Light", 10)
main_thermostat = Thermostat("T001", "Main Thermostat", 25)
front_camera = Camera("C001", "Front Door Camera", 8)

# Create smart home system (aggregation)
my_home = SmartHome("My Smart Home")

# Add devices to home system (aggregation - devices can exist independently)
my_home.add_device(living_room_light)
my_home.add_device(main_thermostat)
my_home.add_device(front_camera)

# Control individual devices
living_room_light.turn_on()
living_room_light.set_brightness(75)

main_thermostat.turn_on()
main_thermostat.set_temperature(68.5)

front_camera.turn_on()
front_camera.start_recording()

# Display home status
my_home.list_devices()
print(f"Total power usage: {my_home.get_total_power()}W")

# Demonstrate aggregation - device can exist independently
independent_light = Light("L002", "Bedroom Light", 5)
independent_light.turn_on()
print(f"Independent device power: {independent_light.get_power_usage()}W")
```

## Expected Output

```
=== My Smart Home Devices ===
Device: Living Room Light (L001) - Status: On, Brightness: 75%, Power: 7.5W
Device: Main Thermostat (T001) - Status: On, Temperature: 68.5°F, Power: 25.0W
Device: Front Door Camera (C001) - Status: On, Recording: Yes, Power: 8.0W

Total power usage: 40.5W
Independent device power: 5.0W
```

## Learning Objectives

- Understand composition (HAS-A) vs inheritance (IS-A)
- Implement objects that contain other objects as essential parts
- Practice aggregation where objects can exist independently
- See how composition creates stronger relationships than aggregation
- Work with simple, clear object relationships
- Demonstrate when to use composition vs aggregation patterns