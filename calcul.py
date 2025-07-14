import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg='#ff5733')

# Display area
display = tk.Entry(root, font=('Arial', 20), justify='right', bg='#ecf0f1', fg='#ff9933')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Function to handle button clicks
def button_click(value):
    if value == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, value)

# Create buttons
row = 1
col = 0
for button in buttons:
    cmd = lambda x=button: button_click(x)
    tk.Button(root, text=button, font=('Arial', 14), bg='#ff9933', fg='white', 
              command=cmd, width=5, height=2).grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text='C', font=('Arial', 14), bg='#ffffff', fg='black',
          command=lambda: display.delete(0, tk.END), width=5, height=2).grid(row=row, column=0, columnspan=4, padx=2, pady=2)

# Configure grid weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
root.mainloop() 