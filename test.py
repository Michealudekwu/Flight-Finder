from tkinter import *

window = Tk()
window.title("Checkbutton Example")

# 1. Create a variable to store the checked state
subscribe_var = IntVar()  # Use IntVar for 0/1 or BooleanVar for True/False

# 2. Create the Checkbutton
subscribe_check = Checkbutton(window, text="Subscribe to newsletter", variable=subscribe_var)
subscribe_check.pack(pady=10)

# 3. Function to check the status
def show_status():
    if subscribe_var.get():
        print("Subscribed ✅")
    else:
        print("Not Subscribed ❌")

# 4. Button to trigger check
submit_btn = Button(window, text="Submit", command=show_status)
submit_btn.pack(pady=10)

window.mainloop()
