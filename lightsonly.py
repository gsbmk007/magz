import time

class Light:
    def __init__(self, color, position, direction, intensity):
        self.color = color
        self.position = position
        self.direction = direction
        self.intensity = intensity
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"Light at position {self.position} turned on. Color: {self.color}")
    
    def turn_off(self):
        self.is_on = False
        print(f"Light at position {self.position} turned off.")
    
    def change_color(self, new_color):
        self.color = new_color
        print(f"Light at position {self.position} changed color to {self.color}.")
    
    def change_intensity(self, new_intensity):
        self.intensity = new_intensity
        print(f"Light at position {self.position} changed intensity to {self.intensity}.")
    
    def move(self, new_position):
        self.position = new_position
        print(f"Light moved to new position: {self.position}.")
    
    def rotate(self, new_direction):
        self.direction = new_direction
        print(f"Light rotated to new direction: {self.direction}.")

# Create lights
lights = [
    Light("Red", (100, 100), "Down", 8),
    Light("Blue", (200, 200), "Down", 6)
]

# Simulate the concert stage
while True:
    for light in lights:
        light.turn_on()
    
    # Do other stage operations...
    
    for light in lights:
        light.change_color("Green")
        light.change_intensity(10)
        light.move((300, 300))
        light.rotate("Left")
    
    # Pause for a certain duration between iterations
    time.sleep(1)
