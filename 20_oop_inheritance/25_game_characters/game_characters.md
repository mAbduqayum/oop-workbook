# Exercise: Game Characters

Design a character system for a video game using inheritance and polymorphism.

## Requirements

Create a character hierarchy with different classes and abilities:

### Base Class: `Character`
- **Attributes:**
  - `name` (string): Character name
  - `health` (int): Current health points (max 100)
  - `max_health` (int): Maximum health points
  - `level` (int): Character level (starts at 1)
  - `experience` (int): Experience points (starts at 0)

- **Methods:**
  - `__init__(name)`: Constructor
  - `attack()`: Return attack damage (to be overridden)
  - `defend(damage)`: Reduce damage taken (to be overridden)
  - `take_damage(damage)`: Apply damage after defense
  - `heal(amount)`: Restore health points
  - `gain_experience(exp)`: Add experience and check for level up
  - `level_up()`: Increase level and restore health
  - `is_alive()`: Return True if health > 0
  - `get_status()`: Return character status string

### Derived Class: `Warrior`
- **Additional Attributes:**
  - `armor` (int): Armor rating (reduces damage)
  - `weapon` (string): Weapon type

- **Override Methods:**
  - `attack()`: Base damage 25 + (level * 2)
  - `defend(damage)`: Reduce damage by armor rating
  - `level_up()`: Gain +5 armor and +10 max health per level

### Derived Class: `Mage`
- **Additional Attributes:**
  - `mana` (int): Current mana points (max 50)
  - `max_mana` (int): Maximum mana points
  - `spells` (list): List of known spells

- **Override Methods:**
  - `attack()`: Base damage 30 + (level * 3), costs 10 mana
  - `defend(damage)`: Reduce damage by 20% (magical shield)
  - `level_up()`: Gain +10 max mana and learn new spell
  - `cast_spell(spell_name)`: Cast spell with mana cost

### Derived Class: `Archer`
- **Additional Attributes:**
  - `arrows` (int): Number of arrows (starts with 30)
  - `bow_type` (string): Type of bow
  - `accuracy` (float): Hit accuracy (0.0 to 1.0)

- **Override Methods:**
  - `attack()`: Base damage 20 + (level * 2.5), uses 1 arrow
  - `defend(damage)`: Reduce damage by 10% (agility)
  - `level_up()`: Gain +0.05 accuracy and +10 arrows
  - `reload_arrows(count)`: Add arrows to inventory

## Example Usage

```python
# Create characters
warrior = Warrior("Conan")
mage = Mage("Gandalf")
archer = Archer("Legolas")

# Display initial status
print(warrior.get_status())
print(mage.get_status())
print(archer.get_status())

# Combat simulation
print(f"\n{warrior.name} attacks for {warrior.attack()} damage!")
print(f"{mage.name} attacks for {mage.attack()} damage!")
print(f"{archer.name} attacks for {archer.attack()} damage!")

# Take damage
warrior.take_damage(15)
mage.take_damage(20)
archer.take_damage(12)

# Gain experience and level up
warrior.gain_experience(100)
mage.gain_experience(150)
archer.gain_experience(120)

print("\nAfter combat:")
print(warrior.get_status())
print(mage.get_status())
print(archer.get_status())
```

## Expected Output

```
Warrior Conan - Level 1
Health: 100/100, Armor: 10, Weapon: Steel Sword
Status: Alive

Mage Gandalf - Level 1
Health: 100/100, Mana: 50/50
Spells: ['Magic Missile']
Status: Alive

Archer Legolas - Level 1
Health: 100/100, Arrows: 30, Bow: Longbow
Accuracy: 85%
Status: Alive

Conan attacks for 27 damage!
Gandalf attacks for 33 damage!
Legolas attacks for 22 damage!

After combat:
Warrior Conan - Level 2
Health: 110/110, Armor: 15, Weapon: Steel Sword
Status: Alive

Mage Gandalf - Level 2
Health: 100/100, Mana: 60/60
Spells: ['Magic Missile', 'Fireball']
Status: Alive

Archer Legolas - Level 2
Health: 88/100, Arrows: 39, Bow: Longbow
Accuracy: 90%
Status: Alive
```

## Learning Objectives

- Implement complex inheritance hierarchies
- Practice method overriding with different behaviors
- Work with class-specific attributes and methods
- Understand polymorphism in game design
- Handle resource management (mana, arrows)
- Implement leveling and progression systems