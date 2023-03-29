#  Task №2. Create class a circle
import math


class Circle:
    """The Circle class creates a circle centered at center_a and center_b with radius - radius"""
    def __init__(self, center_a, center_b, radius):
        self.center_a = center_a
        self.center_b = center_b
        self.radius = radius

    def area(self):
        """The area method finds the area of a circle"""
        a = math.pi * self.radius ** 2
        return round(a)

    def perimeter(self):
        """The perimeter method finds the perimeter of a circle"""
        p = 2 * math.pi * self.radius
        return round(p, 1)

    def test_belongs(self, point_x, point_y):
        """The test_belongs method checks if a point with coordinates point_x, point_y belongs
         circle centered at center_a and center_b and radius - radius.
         Returns True if the point belongs to the circle.
         Returns False if the point does not belong to the circle."""
        if (point_x - self.center_a) ** 2 + (point_y - self.center_b) ** 2 <= self.radius ** 2:
            return True
        return False


ring = Circle(8, 6, 10)
print(ring.area())
print(ring.perimeter())
print(ring.test_belongs(5, 6))
print(ring.test_belongs(66, 6))
