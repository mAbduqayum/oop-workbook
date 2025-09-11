# Exercise: Smart Home Devices

Create a hierarchy for smart home devices with inheritance and device control functionality.

## Requirements

Design a smart home system with different device types and control capabilities:

### Base Class: `SmartDevice`
- **Attributes:**
  - `device_id` (string): Unique device identifier
  - `name` (string): Human-readable device name
  - `is_connected` (boolean): Connection status
  - `power_consumption` (float): Power usage in watts
  - `manufacturer` (string): Device manufacturer

- **Methods:**
  - `__init__(device_id, name, manufacturer)`: Constructor
  - `connect()`: Connect device to network
  - `disconnect()`: Disconnect device from network
  - `get_status()`: Return device status (to be overridden)
  - `control_device(command, value)`: Send control command (to be overridden)
  - `get_power_usage()`: Return current power consumption
  - `reset()`: Reset device to default settings (to be overridden)

### Derived Class: `Light`
- **Additional Attributes:**
  - `brightness` (int): Brightness level (0-100)
  - `color` (tuple): RGB color values (r, g, b)
  - `is_on` (boolean): Light state

- **Override Methods:**
  - `get_status()`: Include light-specific information
  - `control_device(command, value)`: Handle "brightness", "color", "power" commands
  - `reset()`: Set to 100% brightness, white color, turn on
  - Additional methods: `turn_on()`, `turn_off()`, `set_brightness(level)`, `set_color(r, g, b)`

### Derived Class: `Thermostat`
- **Additional Attributes:**
  - `temperature` (float): Current temperature setting
  - `current_temp` (float): Actual room temperature
  - `mode` (string): Operating mode ("heat", "cool", "auto", "off")
  - `schedule` (dict): Temperature schedule by time

- **Override Methods:**
  - `get_status()`: Include thermostat-specific information
  - `control_device(command, value)`: Handle "temperature", "mode" commands
  - `reset()`: Set to 72°F, auto mode
  - Additional methods: `set_temperature(temp)`, `set_mode(mode)`, `add_schedule(time, temp)`

### Derived Class: `SecurityCamera`
- **Additional Attributes:**
  - `resolution` (string): Video resolution (e.g., "1080p", "4K")
  - `recording` (boolean): Recording status
  - `motion_detected` (boolean): Motion detection status
  - `storage_used` (float): Storage space used in GB

- **Override Methods:**
  - `get_status()`: Include camera-specific information
  - `control_device(command, value)`: Handle "recording", "resolution" commands
  - `reset()`: Stop recording, set to 1080p
  - Additional methods: `start_recording()`, `stop_recording()`, `detect_motion()`, `get_footage(duration)`

## Example Usage

```python
# Create smart home devices
living_room_light = Light("L001", "Living Room Light", "Philips")
main_thermostat = Thermostat("T001", "Main Thermostat", "Nest")
front_camera = SecurityCamera("C001", "Front Door Camera", "Ring")

# Connect all devices
devices = [living_room_light, main_thermostat, front_camera]
for device in devices:
    device.connect()

# Control devices
living_room_light.turn_on()
living_room_light.set_brightness(75)
living_room_light.set_color(255, 200, 100)

main_thermostat.set_temperature(68.5)
main_thermostat.set_mode("heat")

front_camera.start_recording()
front_camera.detect_motion()

# Display status
for device in devices:
    print(device.get_status())
    print(f"Power usage: {device.get_power_usage()}W\n")

# Use polymorphism for device control
for device in devices:
    if isinstance(device, Light):
        device.control_device("brightness", 50)
    elif isinstance(device, Thermostat):
        device.control_device("temperature", 70)
    elif isinstance(device, SecurityCamera):
        device.control_device("recording", True)
```

## Expected Output

```
Light: Living Room Light (L001) - Philips
Status: Connected, On
Brightness: 75%, Color: (255, 200, 100)
Power usage: 12.0W

Thermostat: Main Thermostat (T001) - Nest
Status: Connected, Heat Mode
Set Temperature: 68.5°F, Current: 70.2°F
Power usage: 25.5W

Security Camera: Front Door Camera (C001) - Ring
Status: Connected, Recording
Resolution: 1080p, Motion Detected: Yes
Storage Used: 15.3 GB
Power usage: 8.7W
```

## Learning Objectives

- Design inheritance hierarchies for IoT devices
- Implement device-specific control methods
- Practice method overriding with different behaviors
- Work with device state management
- Understand polymorphism in device control systems
- Handle different data types and validation
- Implement realistic smart home functionality