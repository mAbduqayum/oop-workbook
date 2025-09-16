# 📱 Python OOP Practice - Lesson: Smartphone System with Inheritance and Composition

## 📝 Exercise: Build a Complete Smartphone Ecosystem

Create a sophisticated smartphone system that demonstrates **inheritance**, **strong composition**, and **weak composition (aggregation)**. This exercise teaches when to use each relationship type and how they work together in complex systems.

**Your Complete Task:**

### Part 1: Inheritance Hierarchy (IS-A relationships)
1. Create a base `Device` class with:
   - `brand`, `model`, `is_on` attributes
   - `power_on()`, `power_off()`, `get_info()` methods

2. Create a `MobileDevice` class that inherits from `Device`:
   - Add `phone_number` and `network_type` attributes
   - Override `get_info()` to include mobile-specific details
   - Add `connect_to_network()` and `disconnect_from_network()` methods

3. Create a `Smartphone` class that inherits from `MobileDevice`:
   - Add `operating_system` and `storage_capacity` attributes
   - Override `get_info()` to include smartphone-specific details
   - Add `install_app()` and `take_photo()` methods

### Part 2: Strong Composition (HAS-A, integral parts)
Create components that cannot exist without the smartphone:

4. Create a `Battery` class:
   - `capacity`, `current_charge`, `is_charging` attributes
   - `charge()`, `drain(amount)`, `get_battery_info()` methods

5. Create a `Screen` class:
   - `size`, `resolution`, `brightness`, `is_cracked` attributes
   - `adjust_brightness(level)`, `crack_screen()`, `get_screen_info()` methods

6. Create a `Camera` class:
   - `megapixels`, `has_flash`, `photos_taken` attributes
   - `take_photo()`, `toggle_flash()`, `get_camera_info()` methods

### Part 3: Weak Composition/Aggregation (HAS-A, independent parts)
Create components that can exist independently:

7. Create an `App` class:
   - `name`, `version`, `size_mb`, `category` attributes
   - `launch()`, `update()`, `get_app_info()` methods

8. Create a `Contact` class:
   - `name`, `phone_number`, `email` attributes
   - `call()`, `send_message()`, `get_contact_info()` methods

9. Create a `Network` class:
   - `name`, `signal_strength`, `network_type` attributes
   - `broadcast_signal()`, `get_network_info()` methods

### Part 4: Integration
10. Modify your `Smartphone` class to use composition:
    - **Strong composition**: Include `Battery`, `Screen`, `Camera` objects (created in `__init__`)
    - **Weak composition**: Manage lists of `App` and `Contact` objects
    - **Aggregation**: Reference a `Network` object (passed in, not created)

11. Add comprehensive methods to demonstrate all relationships:
    - `check_battery()`, `adjust_screen()`, `use_camera()`
    - `install_app(app)`, `remove_app(app_name)`, `list_apps()`
    - `add_contact(contact)`, `remove_contact(name)`, `call_contact(name)`
    - `connect_to_network(network)`, `check_signal()`

**What You'll Learn:**
- **Inheritance**: "IS-A" relationships (Smartphone IS-A MobileDevice IS-A Device)
- **Strong Composition**: Components that cannot exist without the container
- **Weak Composition (Aggregation)**: Components that can exist independently
- **Object lifecycle management**: When objects are created, destroyed, and shared
- **Real-world system modeling**: How complex systems use multiple relationship types
- **Method overriding**: Specialized behavior in subclasses
- **Encapsulation**: Hiding internal component details

**Example Usage:**
```python
# Create independent components (weak composition/aggregation)
contact1 = Contact("Alice", "555-0101", "alice@email.com")
contact2 = Contact("Bob", "555-0102", "bob@email.com")

app1 = App("Instagram", "2.1", 150, "Social")
app2 = App("Calculator", "1.0", 5, "Utility")

network = Network("Verizon", 85, "5G")

# Create smartphone (inheritance + strong composition)
phone = Smartphone("Apple", "iPhone 15", "555-0100", "5G", "iOS 17", 256)

# Test inheritance
phone.power_on()  # From Device
phone.connect_to_network()  # From MobileDevice
print(phone.get_info())  # Overridden in Smartphone

# Test strong composition (integral components)
phone.check_battery()  # Uses internal Battery object
phone.adjust_screen(80)  # Uses internal Screen object
phone.use_camera()  # Uses internal Camera object

# Test weak composition (independent components)
phone.add_contact(contact1)
phone.add_contact(contact2)
phone.install_app(app1)
phone.install_app(app2)

# Test aggregation (shared resource)
phone.connect_to_network(network)
phone.check_signal()

# Demonstrate independence
print(f"Contact exists independently: {contact1.get_contact_info()}")
print(f"App exists independently: {app1.get_app_info()}")
print(f"Network serves multiple devices: {network.get_network_info()}")

# Show what happens when phone is "destroyed"
phone.power_off()
# Battery, Screen, Camera are destroyed with phone (strong composition)
# But Contacts, Apps, and Network continue to exist (weak composition/aggregation)
print(f"Contact still exists: {contact1.name}")
print(f"App still exists: {app1.name}")
print(f"Network still exists: {network.name}")
```

**Expected Output:**
```
Device Apple iPhone 15 powered on
Connected to 5G network
Device: Apple iPhone 15 | Mobile: 555-0100 (5G) | Smartphone: iOS 17, 256GB storage

Battery: 85% charged, 4000mAh capacity
Screen brightness adjusted to 80%
Photo taken! Total photos: 1, Camera: 12MP

Contact Alice added to smartphone
Contact Bob added to smartphone
App Instagram installed (150MB)
App Calculator installed (5MB)

Connected to network: Verizon (5G, 85% signal)
Network signal: 85% (5G - Verizon)

Contact exists independently: Alice - 555-0101 (alice@email.com)
App exists independently: Instagram v2.1 - Social (150MB)
Network serves multiple devices: Verizon (5G) - Signal: 85%

Device Apple iPhone 15 powered off
Contact still exists: Alice
App still exists: Instagram
Network still exists: Verizon
```

**Key Learning Points:**

1. **When to use Inheritance:**
   - Device → MobileDevice → Smartphone (clear "IS-A" relationships)
   - Each level adds specialized functionality
   - Polymorphism allows treating all as Device objects

2. **When to use Strong Composition:**
   - Battery, Screen, Camera are integral to smartphone
   - Cannot exist without the smartphone
   - Lifecycle tied to the container object

3. **When to use Weak Composition/Aggregation:**
   - Apps can be transferred between devices
   - Contacts exist independently and can be shared
   - Networks serve multiple devices simultaneously

4. **Real-world Complexity:**
   - Systems often combine multiple relationship types
   - Each relationship type serves a specific purpose
   - Understanding the difference helps design better systems

**Challenge Extensions:**
- Add different types of smartphones (Android, iOS) with specialized features
- Implement different battery types with varying behaviors
- Create specialized apps that require specific smartphone features
- Add multiple camera types (front, back, telephoto)
- Implement data transfer between smartphones
- Add network switching and roaming capabilities