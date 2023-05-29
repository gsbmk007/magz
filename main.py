import samplestage
import smokemachine
import lights
import tkinter as tk
from tkinter import messagebox

# Create a window
window = tk.Tk()
window.title("Button Window")
window.geometry("400x400")

# Button 1
button1 = tk.Button(window, text="Lights", command=lights)
button1.pack()

# Button 2
button2 = tk.Button(window, text="Smokemachine", command=smokemachine)
button2.pack()

# Button 3
button3 = tk.Button(window, text="Samplestage",command=samplestage)
button3.pack()

# Run the window's event loop
window.mainloop()