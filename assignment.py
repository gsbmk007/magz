import matplotlib.pyplot as plt
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

class Choreography:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def execute(self):
        # Read the choreography file and execute the commands
        with open(self.file_path, 'r') as file:
            commands = file.readlines()
        
        for command in commands:
            command = command.strip()
            if command.startswith("Light"):
                # Parse and execute light commands
                light_command = command.split(":")[1].strip()
                light_position = light_command.split(",")[0].strip()
                light_action = light_command.split(",")[1].strip()
                
                # Find the corresponding light object based on position
                for light in lights:
                    if light.position == light_position:
                        if light_action == "on":
                            light.turn_on()
                        elif light_action == "off":
                            light.turn_off()
                        break
            elif command.startswith("Smoke"):
                # Parse and execute smoke machine commands
                smoke_command = command.split(":")[1].strip()
                smoke_action = smoke_command.split(",")[0].strip()
                
                if smoke_action == "emit":
                    smoke_machine.emit_smoke()
                elif smoke_action == "clear":
                    smoke_machine.clear_smoke()
            elif command.startswith("Wait"):
                # Parse and execute wait commands
                wait_time = int(command.split(":")[1].strip())
                time.sleep(wait_time)

# Create lights
lights = [
    Light("Red", (100, 100), "Down", 8),
    Light("Blue", (200, 200), "Down", 6)
]

class SmokeMachine:
    def __init__(self, position, direction, intensity):
        self.position = position
        self.direction = direction
        self.intensity = intensity
        self.smoke_level = 0
    
    def emit_smoke(self):
        self.smoke_level += 1
        print("Smoke emitted.")
    
    def clear_smoke(self):
        self.smoke_level = 0
        print("Smoke cleared.")

# Create smoke machine
smoke_machine = SmokeMachine((300, 300), "Center", 10)

# Prepare the figure and axis
fig, ax = plt.subplots()

# Simulate the concert stage
while True:
    # Clear the plot
    ax.clear()

    # Plot the lights
    for light in lights:
        position = light.position
        color = light.color
        ax.plot(position[0], position[1], 'o', color=color)
    
    # Set the axis limits
    ax.set_xlim(0, 500)  # Adjust the values based on your stage dimensions
    ax.set_ylim(0, 500)
    
    # Add any additional visual elements or annotations if desired
    
    # Show the plot
    plt.pause(0.1)  # Pause for a short duration to display the plot

    # Perform other stage operations...
    # Example: execute choreography
    choreography = Choreography("FOP_Ass_BEF\choreography.txt")
    choreography.execute()

    # Pause for a certain duration between iterations
    time.sleep(1)
