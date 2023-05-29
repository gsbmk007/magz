class SmokeMachine:
    def __init__(self, position, direction, intensity):
        self.position = position
        self.direction = direction
        self.intensity = intensity
        self.is_emitting = False

    def emit_smoke(self):
        self.is_emitting = True
        print("Smoke emitted")

    def clear_smoke(self):
        self.is_emitting = False
        print("Smoke cleared")
