class Light:
    def __init__(self, color, position, direction, intensity):
        self.color = color
        self.position = position
        self.direction = direction
        self.intensity = intensity
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"Light {self.position} turned on")

    def turn_off(self):
        self.is_on = False
        print(f"Light {self.position} turned off")


class LightGroup:
    def __init__(self, lights):
        self.lights = lights

    def synchronize_lights(self):
        print("Synchronizing lights...")
        # Logic to synchronize the lights


class Prop:
    def __init__(self, shape, position):
        self.shape = shape
        self.position = position


class Band:
    def __init__(self, members):
        self.members = members
