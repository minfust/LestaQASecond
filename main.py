# Класс фигуры Circle
class Circle:
    def __init__(self, x, y, radius, color='black'):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        return f"Drawing Circle: Center at ({self.x}, {self.y}), Radius: {self.radius}, Color: {self.color}"

# Класс фигуры Triangle
class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, color='black'):
        self.points = [(x1, y1), (x2, y2), (x3, y3)]
        self.color = color

    def draw(self):
        return f"Drawing Triangle: Points: {self.points}, Color: {self.color}"

# Класс фигуры Rectangle
class Rectangle:
    def __init__(self, x, y, width, height, color='black'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        return f"Drawing Rectangle: Top-left corner at ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}, Color: {self.color}"

# Класс движка Engine2D
class Engine2D:
    def __init__(self):
        self.canvas = []
        self.current_color = 'black'

    def add_shape(self, shape):
        self.canvas.append(shape)

    def change_color(self, color):
        self.current_color = color

    def draw(self):
        for shape in self.canvas:
            shape.color = self.current_color
            print(shape.draw())  # Выводим отрисованные фигуры в консоль
        self.canvas = []  # Очищаем canvas после отрисовки

def main():
    # Создание движка
    engine = Engine2D()

    # Создание фигур
    circle = Circle(0, 0, 5)
    triangle = Triangle(1, 1, 3, 3, 5, 1)
    rectangle = Rectangle(2, 2, 4, 3)

    # Добавление фигур на холст
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)

    # Изменение цвета
    engine.change_color('red')

    # Отрисовка всех фигур
    engine.draw()

    engine.change_color('blue')
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)
    engine.draw()
    
# Проверка, что скрипт запущен как основной и вызов функции main()
if __name__ == "__main__":
    main()


import pytest

# Фикстура для создания экземпляра движка Engine2D
@pytest.fixture
def engine():
    return Engine2D()

# Тесты для отрисовки каждой фигуры
def test_circle_draw():
    circle = Circle(0, 0, 5)
    assert circle.draw() == "Drawing Circle: Center at (0, 0), Radius: 5, Color: black"

def test_triangle_draw():
    triangle = Triangle(1, 1, 3, 3, 5, 1)
    assert triangle.draw() == "Drawing Triangle: Points: [(1, 1), (3, 3), (5, 1)], Color: black"

def test_rectangle_draw():
    rectangle = Rectangle(2, 2, 4, 3)
    assert rectangle.draw() == "Drawing Rectangle: Top-left corner at (2, 2), Width: 4, Height: 3, Color: black"

# Тесты для движка Engine2D
def test_engine_add_shape(engine):
    circle = Circle(0, 0, 5)
    engine.add_shape(circle)
    assert len(engine.canvas) == 1

def test_engine_change_color(engine):
    circle = Circle(0, 0, 5)
    engine.add_shape(circle)
    engine.change_color('red')
    engine.draw()
    assert circle.color == 'red'
