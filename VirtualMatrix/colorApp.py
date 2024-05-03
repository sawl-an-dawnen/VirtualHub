import tkinter as tk
import Fiber

def display_colors():
    color1 = entry_fiber_count.get()  # Get the first color from the entry widget
    color2 = entry_fiber_color.get()  # Get the second color from the entry widget
    # Create a new window
    window = tk.Toplevel(root)
    # Set the background color of the window to color1
    window.configure(bg=color1)
    # Create a label to display the second color
    label = tk.Label(window, text="Second Color", bg=color2, font=("Helvetica", 20))
    label.pack(padx=20, pady=20)

def display_fiber_colors():
    # Create a Fiber object with user input
    fiber = Fiber.Fiber(int(entry_fiber_count.get()), entry_buffer_color.get(), entry_fiber_color.get())

    # Create a new window
    window = tk.Toplevel(root)

    # Set the background color of the window to buffer color
    window.configure(bg=fiber.buffer_color)

    # Create a label to display the fiber color
    label = tk.Label(window, text=f"{fiber.fiber_count}"+"F", bg=fiber.fiber_color, font=("Helvetica", 20))
    label.pack(padx=20, pady=20)

# Create the main window
root = tk.Tk()
root.title("Color Display App")

# Create entry widgets to input fiber information
tk.Label(root, text="Fiber Count:").pack()
entry_fiber_count = tk.Entry(root)
entry_fiber_count.pack(pady=5)

tk.Label(root, text="Buffer Color:").pack()
entry_buffer_color = tk.Entry(root)
entry_buffer_color.pack(pady=5)

tk.Label(root, text="Fiber Color:").pack()
entry_fiber_color = tk.Entry(root)
entry_fiber_color.pack(pady=5)

# Create a button to display the colors
button = tk.Button(root, text="Display Colors", command=display_fiber_colors)
button.pack(pady=10)

# Run the application
root.mainloop()