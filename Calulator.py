import tkinter as tk
from tkinter import messagebox

# Calculator class definition
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")  # Set the window title
        self.root.geometry("400x600")  # Set the window size

        self.expression = ""  # This will store the current expression
        self.text_input = tk.StringVar()  # This is used to update the display

        # Create the display entry widget
        self.entry = tk.Entry(root, textvariable=self.text_input, font=('Arial', 20, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)  # Position the entry widget

        # Define the buttons for the calculator
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        # Create buttons and position them in a grid
        row = 1
        col = 0
        for button in buttons:
            self.create_button(button).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create and position the clear button
        clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 20, 'bold'), command=self.clear)
        clear_button.grid(row=row, column=0, columnspan=4, sticky="nsew")

        # Configure grid rows and columns to adjust to window size changes
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    # Function to create a button
    def create_button(self, text):
        return tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 20, 'bold'), command=lambda: self.button_click(text))

    # Function to handle button clicks
    def button_click(self, item):
        if item == "=":  # If equals button is clicked, evaluate the expression
            try:
                result = str(eval(self.expression))  # Evaluate the expression and convert to string
                self.text_input.set(result)  # Update display with the result
                self.expression = result  # Update expression with result for further calculations
            except:  # If there's an error in evaluation, display error message
                self.text_input.set("Error")
                self.expression = ""
        else:
            self.expression += str(item)  # Append the clicked button text to the expression
            self.text_input.set(self.expression)  # Update the display

    # Function to clear the display and reset the expression
    def clear(self):
        self.expression = ""  # Reset the expression
        self.text_input.set("")  # Clear the display

# Main execution block
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    Calculator(root)  # Create an instance of the Calculator class
    root.mainloop()  # Run the Tkinter main loop
    
