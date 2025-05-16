import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Keyboard Tester")
root.geometry("600x400")

# Label to show key pressed
key_label = tk.Label(root, text="Press a key!", font=("Arial", 14))
key_label.pack(pady=20)

# Dictionary to store key buttons 
key_buttons  = {}

# Function to handle key press
def on_key_press(event):
    key = event.keysym
    key_label.config(text=f"key pressed: {key}")
    if key in key_buttons:
        key_buttons[key].config(bg="yellow")
# Function to handle key press
def on_key_release(event):
    key = event.keysym
    key_label.config(text=f"Key Pressed: {key}")
    if key in key_buttons:
        key_buttons[key].config(bg="SystemButtonFace")

# create a frame for the keyboard
keyboard_frame = tk.Frame(root)  
keyboard_frame.pack(pady=20)

# Simple keyboard layout (A-Z)
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    btn = tk.Button(keyboard_frame, text=letter,  width=3, height=2)
    btn.grid(row=i // 13, column=i % 13, padx=2, pady=2)
    key_buttons[letter.lower()]= btn

# Bind Key events
root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)



# start the app
root.mainloop()