import tkinter as tk
import random

# List of musical notes
musical_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def update_label():
    # Update the label with a randomly selected musical note
    selected_note = random.choice(musical_notes)
    current_note.config(text=selected_note)

    # Update the background color
    new_color = random_color()
    current_note.config(bg=new_color)

    if update_state:
        root.after(int(delay_slider.get() * 1000), update_label)

def adjust_font_size(event):
    # Adjust the label's font size based on the window's width
    label_width = event.width
    font_size = max(10, label_width // 15)  # Adjust this value as needed
    current_note.config(font=("Arial", font_size))

def toggle_updating_state():
    global update_state
    if update_state:
        update_state = False
        on_button.config(state="active")
        off_button.config(state="disabled")
    else:
        update_state = True
        on_button.config(state="disabled")
        off_button.config(state="active")
        update_label()

def random_color():
    # Generate a random color in hexadecimal format
    return f"#{random.randint(0, 255):02X}{random.randint(0, 255):02X}{random.randint(0, 255):02X}"

# Create the main window
root = tk.Tk()
root.title("Random Musical Note")

# Create a label
current_note = tk.Label(root, text="", font=("Arial", 24), bg=random_color())
current_note.pack(pady=20, fill="both", expand=True)

# Create a slider for delay
delay_slider = tk.Scale(root, from_=0.1, to=5.0, resolution=0.1, orient="horizontal", label="Delay (s)")
delay_slider.set(1.0)  # Initial value
delay_slider.pack()

# Initialize the update state
update_state = False

# Create an "On" button
on_button = tk.Button(root, text="On", command=toggle_updating_state, state="active")
on_button.pack()

# Create an "Off" button
off_button = tk.Button(root, text="Off", command=toggle_updating_state, state="disabled")
off_button.pack()

# Bind the adjust_font_size function to window resizing events
root.bind("<Configure>", adjust_font_size)

# Start the Tkinter main loop
root.mainloop()


