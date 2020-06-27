import tkinter as tk
r = tk.Tk()
r.minsize(500, 450)
r.title("Ajax Program")
button =  tk.Button(r, text="Stop", width=25, command = r.destroy)
button.place(x=20, y=20)
r.mainloop()  