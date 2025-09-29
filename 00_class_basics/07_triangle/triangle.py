import math


class Triangle:
    def __init__(self, a, b, c):
        if not abs(a - c) < b < a + c:
            raise ValueError("Invalid triangle: sides do not satisfy triangle inequality")
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_type(self):
        sides = sorted([self.a, self.b, self.c])
        if sides[0] == sides[1] == sides[2]:
            return "equilateral"
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            return "isosceles"
        else:
            return "scalene"

    def get_angles(self):
        a, b, c = self.a, self.b, self.c

        angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_c = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

        return [angle_a, angle_b, angle_c]

    def get_angle_type(self):
        angles = self.get_angles()
        max_angle = max(angles)

        if abs(max_angle - 90) < 1e-9:
            return "right"
        elif max_angle > 90:
            return "obtuse"
        else:
            return "acute"

    def scale(self, factor):
        return Triangle(self.a * factor, self.b * factor, self.c * factor)

    def is_similar(self, other_triangle: "Triangle") -> bool:
        self_sides = sorted([self.a, self.b, self.c])
        other_sides = sorted([other_triangle.a, other_triangle.b, other_triangle.c])

        ratio1 = self_sides[0] / other_sides[0]
        ratio2 = self_sides[1] / other_sides[1]
        ratio3 = self_sides[2] / other_sides[2]

        return abs(ratio1 - ratio2) < 1e-9 and abs(ratio1 - ratio3) < 1e-9


if __name__ == "__main__":
    triangle1 = Triangle(3, 4, 5)
    print(triangle1.calculate_perimeter())
    print(triangle1.calculate_area())
    print(triangle1.get_type())
    print(triangle1.get_angles())
    print(triangle1.get_angle_type())

    scaled = triangle1.scale(2)
    print(scaled.a, scaled.b, scaled.c)

    print(triangle1.is_similar(scaled))

    try:
        Triangle(1, 1, 5)
    except ValueError as e:
        print(e)
