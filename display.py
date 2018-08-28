import tkinter as tk
import vector

window = tk.Tk() # create window

lbl1 = tk.Label(window, text="Node List:", fg='black', font=("Helvetica", 16, "bold"))
lbl2 = tk.Label(window, text="Node Information:", fg='black', font=("Helvetica", 16,"bold"))
lbl1.grid(row=0, column=0, sticky=tk.W)
lbl2.grid(row=0, column=1, sticky=tk.W)

frm = tk.Frame(window)
frm.grid(row=1, column=0, sticky=tk.N+tk.S)
window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)

scrollbary = tk.Scrollbar(frm, orient="vertical")
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)

scrollbarx = tk.Scrollbar(frm, orient="horizontal")
scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)

lbx = tk.Listbox(frm, width=50, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set, font=("Helvetica", 12))
selected_item = tk.StringVar()
def select_title(event):
    line = lbx.curselection()[0]
    item = lbx.get(line)
    selected_item.set(item)
lbx.bind("<<ListboxSelect>>", select_title)
lbx.pack(expand=True, fill=tk.Y)

print(selected_item)

scrollbary.config(command=lbx.yview)
scrollbarx.config(command=lbx.xview)

searchbutton = tk.Button(window, text='search similar recipes')
searchbutton.grid(row=1, column=1, sticky=tk.E+tk.W+tk.N)

listSelection = tk.Listbox(window, height=4, font=("Helvetica", 12))
listSelection.grid(row=1, column=1, sticky=tk.E+tk.W)


for title in vector.TITLES:
    lbx.insert(tk.END, title)

listSelection.insert(tk.END, selected_item.get())
    
tk.mainloop()