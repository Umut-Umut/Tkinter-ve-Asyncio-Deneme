import tkinter as tk

#=========================== INTERFACE
win = tk.Tk()
win.title("Timer")
win.geometry("300x300")

#=========================== FRAMES
frame = tk.Frame(win)

#=========================== LABELS
main_label = tk.Label(win, font="Arial 24 bold")

#=========================== BUTTONS
button  = tk.Button(frame, text="button")

#=========================== ENTRYS
entry = tk.Entry(win, justify="center")

#=========================== FRAME PACK
button.pack(side='left')

#=========================== WINDOW PACK
pack_order = [main_label, entry, frame]
for i in pack_order:
    i.pack()


if __name__ == "__main__":
    win.mainloop()