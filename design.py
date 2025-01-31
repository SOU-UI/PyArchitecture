class Building:
    def __init__(self, name, length, width, height):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_volume(self):
        return self.length * self.width * self.height
