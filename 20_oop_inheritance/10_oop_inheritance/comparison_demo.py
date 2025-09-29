"""
OOP CONCEPTS COMPARISON - Inheritance vs Composition vs Aggregation

This file demonstrates the key differences between the three main OOP relationships
using simple, side-by-side examples.
"""

print("=" * 80)
print("OOP RELATIONSHIPS COMPARISON")
print("=" * 80)

# ============================================================================
# INHERITANCE EXAMPLE - "IS-A" Relationship
# ============================================================================
print("\n1. INHERITANCE - 'IS-A' Relationship")
print("-" * 40)


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound"


class Dog(Animal):  # Dog IS-A Animal
    def make_sound(self):
        return f"{self.name} barks: Woof!"


# Demonstration
dog = Dog("Buddy")
print(f"Created: {dog.name}")
print(f"Behavior: {dog.make_sound()}")
print(f"Type check: {isinstance(dog, Animal)} (Dog is an Animal)")
print("Key: Child inherits from parent, shares identity")

# ============================================================================
# COMPOSITION EXAMPLE - "HAS-A" Relationship (Strong)
# ============================================================================
print("\n2. COMPOSITION - 'HAS-A' Relationship (Strong)")
print("-" * 40)


class Engine:
    def __init__(self, type) -> None:
        self.type = type
        self.running = False

    def start(self):
        self.running = True
        return f"{self.type} engine started"


class Car:  # Car HAS-A Engine (owns it exclusively)
    def __init__(self, model) -> None:
        self.model = model
        self.engine = Engine("V6")  # Car creates and owns engine

    def start(self):
        return f"{self.model}: {self.engine.start()}"


# Demonstration
car = Car("Toyota")
print(f"Created: {car.model}")
print(f"Action: {car.start()}")
print("Key: Car owns engine exclusively, engine can't exist without car")

# ============================================================================
# AGGREGATION EXAMPLE - "HAS-A" Relationship (Weak)
# ============================================================================
print("\n3. AGGREGATION - 'HAS-A' Relationship (Weak)")
print("-" * 40)


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.teams = []

    def join_team(self, team):
        self.teams.append(team)


class Team:  # Team HAS Players (but players exist independently)
    def __init__(self, name) -> None:
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        player.join_team(self)


# Demonstration
player1 = Player("Alice")  # Player exists independently
team1 = Team("Eagles")
team1.add_player(player1)  # Team aggregates existing player

print(f"Created player: {player1.name}")
print(f"Created team: {team1.name}")
print(f"Player joined: {player1.name} is in {len(player1.teams)} team(s)")
print("Key: Player exists independently, can be part of multiple teams")

# ============================================================================
# SIDE-BY-SIDE COMPARISON
# ============================================================================
print("\n" + "=" * 80)
print("SIDE-BY-SIDE COMPARISON")
print("=" * 80)

print(f"{'Aspect':<20} {'Inheritance':<20} {'Composition':<20} {'Aggregation':<20}")
print("-" * 80)
print(f"{'Relationship':<20} {'IS-A':<20} {'HAS-A (Strong)':<20} {'HAS-A (Weak)':<20}")
print(f"{'Coupling':<20} {'Tight':<20} {'Tight':<20} {'Loose':<20}")
print(f"{'Lifecycle':<20} {'Shared':<20} {'Dependent':<20} {'Independent':<20}")
print(f"{'Ownership':<20} {'N/A':<20} {'Exclusive':<20} {'Shared':<20}")
print(
    f"{'Example':<20} {'Dog IS Animal':<20} {'Car HAS Engine':<20} {'Team HAS Players':<20}"
)

# ============================================================================
# PRACTICAL DECISION GUIDE
# ============================================================================
print("\n" + "=" * 80)
print("WHEN TO USE WHICH?")
print("=" * 80)

scenarios = [
    ("A Manager in a company", "Inheritance", "Manager IS-A Employee"),
    ("A Car's engine", "Composition", "Engine is integral part of Car"),
    ("Students in a university", "Aggregation", "Students exist independently"),
    ("A Circle shape", "Inheritance", "Circle IS-A Shape"),
    ("A Computer's CPU", "Composition", "CPU is integral component"),
    ("Books in a library", "Aggregation", "Books exist independently"),
]

for scenario, approach, reason in scenarios:
    print(f"• {scenario:<25} → {approach:<12} ({reason})")

print("\n" + "=" * 80)
print("QUICK DECISION RULES")
print("=" * 80)
print("1. Ask: 'Is this an IS-A relationship?' → Use INHERITANCE")
print("2. Ask: 'Can the part exist without the whole?' → If NO: COMPOSITION")
print("3. Ask: 'Can the part exist without the whole?' → If YES: AGGREGATION")
print("4. Ask: 'Do multiple containers share the same parts?' → Use AGGREGATION")
print("5. Ask: 'Is the part fundamental to the whole?' → Use COMPOSITION")

# ============================================================================
# INTERACTIVE EXAMPLES
# ============================================================================
print("\n" + "=" * 80)
print("INTERACTIVE EXAMPLES")
print("=" * 80)

# Inheritance - Polymorphism
animals = [Dog("Rex"), Dog("Max")]
print("\nInheritance - Polymorphism:")
for animal in animals:
    print(f"  {animal.make_sound()}")

# Composition - Integrated behavior
cars = [Car("Honda"), Car("Ford")]
print("\nComposition - Integrated behavior:")
for car in cars:
    print(f"  {car.start()}")

# Aggregation - Flexible relationships
player2 = Player("Bob")
team2 = Team("Lions")
team1.add_player(player2)  # Bob joins Eagles
team2.add_player(player2)  # Bob also joins Lions
print("\nAggregation - Flexible relationships:")
print(f"  {player2.name} plays for {len(player2.teams)} teams")
print(f"  Eagles have {len(team1.players)} players")
print(f"  Lions have {len(team2.players)} players")

print("\n" + "=" * 80)
