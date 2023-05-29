import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Choreography:
    def __init__(self, lights, smoke_machine, file_path):
        self.lights = lights
        self.smoke_machine = smoke_machine
        self.file_path = file_path

    def execute(self):
        # Read the choreography file and execute the commands
        with open(self.file_path, 'r') as file:
            commands = file.readlines()

        for command in commands:
            command = command.strip()
            if command.startswith("Light"):
                # Parse and execute light commands
                command_parts = command.split(" ")
                light_position = tuple(map(int, command_parts[1].strip("()").split(",")))
                light_action = command_parts[2]
                light = self.get_light_at_position(light_position)

                if light:
                    if light_action == "on":
                        light.turn_on()
                    elif light_action == "off":
                        light.turn_off()
                    # Handle other light actions (e.g., color change, intensity change)
            elif command.startswith("Smoke"):
                # Parse and execute smoke machine commands
                command_parts = command.split(" ")
                smoke_action = command_parts[1]
                if smoke_action == "emit":
                    self.smoke_machine.emit_smoke()
                elif smoke_action == "clear":
                    self.smoke_machine.clear_smoke()
            # Handle other commands (e.g., Prop, Band, Backdrop)

            # Plot the stage after executing each command
            self.plot_stage()

    def get_light_at_position(self, position):
        for light in self.lights:
            if light.position == position:
                return light
        return None

    def plot_stage(self):
        fig, ax = plt.subplots()

        # Plot lights
        for light in self.lights:
            if light.is_on:
                color = light.color
            else:
                color = 'black'
            ax.add_patch(patches.Circle(light.position, radius=2, color=color))

        # Plot smoke machine
        if self.smoke_machine.is_smoke_emitted:
            ax.add_patch(patches.Rectangle((295, 295), 10, 10, color='gray'))

        # Set plot limits and labels
        ax.set_xlim(0, 500)
        ax.set_ylim(0, 500)
        ax.set_aspect('equal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Stage')

        # Show the plot
        plt.show()
