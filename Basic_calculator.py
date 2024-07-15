Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tkinter as tk
>>>
>>> # Create the main window
>>> root = tk.Tk()
>>> root.title("Calculator")
''
>>> root.geometry("400x500")
''
>>> root.resizable(0, 0)
''
>>>
>>> # Set the main window background color
>>> root.configure(bg="lightgrey")
>>>
>>> # Create an entry widget for the display
>>> display = tk.Entry(root, width=16, borderwidth=0, font=("Arial", 24), justify='right', bd=10)
>>> display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
>>>
>>> # Define button click function
>>> def button_click(number):
...     current = display.get()
...     display.delete(0, tk.END)
...     display.insert(0, current + str(number))
...
>>> # Define clear button function
>>> def button_clear():
...     display.delete(0, tk.END)
...
>>> # Define add function
>>> def button_add():
...     first_number = display.get()
...     global f_num
...     global math
...     math = "addition"
...     f_num = float(first_number)
...     display.delete(0, tk.END)
...
>>> # Define subtract function
>>> def button_subtract():
...     first_number = display.get()
...     global f_num
...     global math
...     math = "subtraction"
...     f_num = float(first_number)
...     display.delete(0, tk.END)
...
>>> # Define multiply function
>>> def button_multiply():
...     first_number = display.get()
...     global f_num
...     global math
...     math = "multiplication"
...     f_num = float(first_number)
...     display.delete(0, tk.END)
...
>>> # Define divide function
>>> def button_divide():
...     first_number = display.get()
...     global f_num
...     global math
...     math = "division"
...     f_num = float(first_number)
...     display.delete(0, tk.END)
...
>>> # Define equal button function
>>> def button_equal():
...     second_number = display.get()
...     display.delete(0, tk.END)
...
...     if math == "addition":
...         display.insert(0, f_num + float(second_number))
...     elif math == "subtraction":
...         display.insert(0, f_num - float(second_number))
...     elif math == "multiplication":
...         display.insert(0, f_num * float(second_number))
...     elif math == "division":
...         display.insert(0, f_num / float(second_number))
...
>>> # Create button styles
>>> button_font = ("Arial", 18)
>>> button_bg = "#f0f0f0"
>>> button_fg = "#333"
>>> button_active_bg = "#ddd"
>>> button_active_fg = "#000"
>>>
>>> # Define buttons
>>> buttons = [
...     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3, button_divide),
...     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3, button_multiply),
...     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3, button_subtract),
...     ('0', 4, 0), ('C', 4, 1, button_clear), ('+', 4, 2, button_add), ('=', 4, 3, button_equal)
... ]
>>>
>>> for button in buttons:
...     text, row, col = button[:3]
...     action = button[3] if len(button) == 4 else lambda x=text: button_click(x)
...     tk.Button(
...         root, text=text, font=button_font, bg=button_bg, fg=button_fg,
...         activebackground=button_active_bg, activeforeground=button_active_fg,
...         width=5, height=2, command=action
...     ).grid(row=row, column=col, padx=5, pady=5)
...
>>> # Run the main loop
>>> root.mainloop()
>>>
