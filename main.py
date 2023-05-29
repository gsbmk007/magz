import time
from light import Light, LightGroup, Prop, Band
from smoke import SmokeMachine
from backdrop import Backdrop
from choreography import Choreography


def main():
    # Create light objects
    light1 = Light("Red", (100, 100), 0, 0.5)
    light2 = Light("Green", (200, 200), 45, 0.8)
    lights = [light1, light2]

    # Create a light group
    light_group = LightGroup([light1, light2])

    # Create a smoke machine object
    smoke_machine = SmokeMachine((300, 300), 90, 0.7)

    # Create prop and band objects
    prop1 = Prop("Circle", (40, 40))
    band = Band(["Guitarist", "Bassist", "Drummer"])

    # Create a backdrop object
    backdrop = Backdrop("backdrop.jpg")

    # Create a list of lights
    lights = [light1, light2]

    # Create a Choreography object
    choreography = Choreography(lights, smoke_machine, "/Users/bala/Desktop/Curtin/1 Year/Sem2/MAGZ/Assignment /choreography.txt")
    # choreography.execute()
    # Execute the choreography
    choreography.execute()


if __name__ == '__main__':
    main()
