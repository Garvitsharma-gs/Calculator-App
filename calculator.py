import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x600")
window.config(bg="#121212")  # Dark background


# Global variables
expression = ""
equation = tk.StringVar()


def press(num):
    """Handles button presses for numbers and operators."""
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    """Evaluates the current expression."""
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except Exception:
        equation.set("Error")
        expression = ""


def clear():
    """Clears the current expression."""
    global expression
    expression = ""
    equation.set("")


def backspace():
    """Deletes the last character in the expression."""
    global expression
    expression = expression[:-1]
    equation.set(expression)


# Entry for displaying the equation
entry = tk.Entry(
    window,
    textvariable=equation,
    font=("Segoe UI", 24),
    borderwidth=0,
    justify="right",
    bg="#1e1e1e",
    fg="#ffffff",
    highlightthickness=0,
)
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Frame for buttons
button_frame = tk.Frame(window, bg="#121212")
button_frame.pack(expand=True, fill="both")


# Function to create circular buttons
def create_button(text, row, col, bg_color, fg_color, command):
    btn = tk.Button(
        button_frame,
        text=text,
        font=("Segoe UI", 18),
        bg=bg_color,
        fg=fg_color,
        activebackground="#555555",
        activeforeground=fg_color,
        relief="flat",
        command=command,
        height=3,  # Set height
        width=3,   # Set width
        bd=0,       # Border width
        padx=0,     # Padding to center text
        pady=0,     # Padding to center text
    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button_frame.grid_columnconfigure(col, weight=1)
    button_frame.grid_rowconfigure(row, weight=1)
    
    # Make the button appear circular by ensuring the width and height are equal
    btn.config(width=4, height=2)


# Button configuration
buttons = [
    ("AC", 0, 0, "#388e3c", "#ffffff", clear),
    ("(", 0, 1, "#1565c0", "#ffffff", lambda: press("(")),
    (")", 0, 2, "#1565c0", "#ffffff", lambda: press(")")),
    ("÷", 0, 3, "#1565c0", "#ffffff", lambda: press("/")),
    ("7", 1, 0, "#333333", "#ffffff", lambda: press("7")),
    ("8", 1, 1, "#333333", "#ffffff", lambda: press("8")),
    ("9", 1, 2, "#333333", "#ffffff", lambda: press("9")),
    ("×", 1, 3, "#1565c0", "#ffffff", lambda: press("*")),
    ("4", 2, 0, "#333333", "#ffffff", lambda: press("4")),
    ("5", 2, 1, "#333333", "#ffffff", lambda: press("5")),
    ("6", 2, 2, "#333333", "#ffffff", lambda: press("6")),
    ("-", 2, 3, "#1565c0", "#ffffff", lambda: press("-")),
    ("1", 3, 0, "#333333", "#ffffff", lambda: press("1")),
    ("2", 3, 1, "#333333", "#ffffff", lambda: press("2")),
    ("3", 3, 2, "#333333", "#ffffff", lambda: press("3")),
    ("+", 3, 3, "#1565c0", "#ffffff", lambda: press("+")),
    ("0", 4, 0, "#333333", "#ffffff", lambda: press("0")),
    (".", 4, 1, "#333333", "#ffffff", lambda: press(".")),
    ("⌫", 4, 2, "#ffa000", "#000000", backspace),
    ("=", 4, 3, "#1565c0", "#ffffff", equalpress),
]

# Create the buttons
for text, row, col, bg_color, fg_color, command in buttons:
    create_button(text, row, col, bg_color, fg_color, command)


# Run the application
window.mainloop()
