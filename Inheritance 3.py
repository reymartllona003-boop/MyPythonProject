#super inheritance

class shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(shape):
    def __init__(self, color, is_filled, radius ):
     super().__init__(color, is_filled)
     self.radius = radius

class Square(shape):
    def __init__(self,color, is_filled, width):
     super().__init__(color, is_filled)
     self.width = width

class Tringle(shape):
   def __init__(self,color, is_filled, width, height):
     super().__init__(color, is_filled)
     self.width = width
     self.height = height


circle = Circle(color = "red",is_filled = True, radius=5 )
square = Square(color = "blue",is_filled = False, width=5 )
tringle = Tringle (color = "yellow",is_filled = True, width=7, height= 8 )

print(circle.color)
print(circle.radius)