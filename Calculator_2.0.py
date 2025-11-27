import tkinter as tk

def on_button_click(char):
    """Updates the entry widget when a button is clicked."""
    if char == '=':
        try:
            # Evaluate the expression in the entry field
            result = str(eval(entry_display.get()))
            entry_display.delete(0, tk.END)
            entry_display.insert(0, result)
        except Exception as e:
            entry_display.delete(0, tk.END)
            entry_display.insert(0, "Error")
    elif char == 'C':
        # Clear the display
        entry_display.delete(0, tk.END)
    else:
        # Append the character to the current display
        entry_display.insert(tk.END, char)

# --- Set up the main application window ---
root = tk.Tk()
root.title("Simple Python Calculator")
root.resizable(False, False) # Prevents window resizing

# --- Create the Display (Entry Widget) ---
entry_display = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 16), justify="right")
# sticky="nsew" makes the widget expand to fill the cell
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# --- Define the buttons ---
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# --- Place the buttons using a loop ---
for (text, row, column) in buttons:
    # command=lambda t=text: on_button_click(t) passes the button text to the function
    btn = tk.Button(root, text=text, padx=20, pady=15, font=("Arial", 12),
                    command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

# --- Start the Tkinter event loop ---
# This line runs the application until you close the window
root.mainloop()
