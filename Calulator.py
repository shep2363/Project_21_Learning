import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("700x900")
        
        self.expression = ""
        self.text_input = tk.StringVar()

        # Display
        self.entry = tk.Entry(root, textvariable=self.text_input, font=('Arial', 60, 'bold'), bd=30, insertwidth=60, width=30, borderwidth=20)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            self.create_button(button).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 20, 'bold'), command=self.clear)
        clear_button.grid(row=row, column=0, columnspan=4, sticky="nsew")

        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def create_button(self, text):
        return tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 20, 'bold'), command=lambda: self.button_click(text))

    def button_click(self, item):
        if item == "=":
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except:
                self.text_input.set("Error")
                self.expression = ""
        else:
            self.expression += str(item)
            self.text_input.set(self.expression)

    def clear(self):
        self.expression = ""
        self.text_input.set("")

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
