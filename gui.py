import tkinter as tk
from tkinter import ttk

class Gui:
    def __init__(self):
        self.root = tk.Tk()

        self.treeview = ttk.Treeview(self.root, columns=("czynnosci", "poprzedni", "nastepny"), show="headings")

        self.treeview.heading("#0", text="ID")
        self.treeview.heading("czynnosci", text="Czynnosc")
        self.treeview.heading("poprzedni", text="Poprzedni")
        self.treeview.heading("nastepny", text="Nastepny")

        self.treeview.insert("", "end", "item1", text="1", values=("1", "A", "B"))
        self.treeview.insert("", "end", "item2", text="2", values=("2", "B", "C"))
        self.treeview.insert("", "end", "item3", text="3", values=("3", "A", "C"))
        self.treeview.insert("", "end", "item4", text="4", values=("", "", ""))
        self.treeview.insert("", "end", "item5", text="5", values=("", "", ""))
        self.treeview.insert("", "end", "item6", text="6", values=("", "", ""))
        self.treeview.insert("", "end", "item7", text="7", values=("", "", ""))
        self.treeview.insert("", "end", "item8", text="8", values=("", "", ""))
        self.treeview.insert("", "end", "item9", text="9", values=("", "", ""))

        self.treeview.bind("<Double-1>", lambda event: self.treeview_edit(event, self.treeview))
        self.treeview.bind("<Return>", lambda event: self.treeview_edit(event, self.treeview))
        self.treeview.bind("<KP_Enter>", lambda event: self.treeview_edit(event, self.treeview))
        
        self.treeview.focus()

        self.treeview.column("#0", width=50, minwidth=50, stretch=tk.NO)
        self.treeview.column("czynnosci", width=100, minwidth=100, stretch=tk.NO)
        self.treeview.column("poprzedni", width=100, minwidth=100, stretch=tk.NO)
        self.treeview.column("nastepny", width=100, minwidth=100, stretch=tk.NO)

        self.treeview.pack(fill=tk.BOTH, expand=1)

        # self.root.mainloop()

    def stop(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()

    def treeview_edit(self, event, treeview):
        selected_item = treeview.selection()[0]
        value = treeview.item(selected_item, "values")
        column = treeview.identify_column(event.x)
        row = treeview.identify_row(event.y)
        
        # added this block to allow the user to edit the cell value
        def save_edit(event):
            new_value = entry.get()
            treeview.set(selected_item, column, new_value)
            entry.destroy()
            self.root.bind("<Return>", lambda event: self.treeview_edit(event, self.treeview))
            self.root.bind("<KP_Enter>", lambda event: self.treeview_edit(event, self.treeview))
        
        entry = tk.Entry(self.root, width=20)
        entry.insert(0, value[int(column[1]) - 1])
        entry.bind("<Return>", save_edit)
        entry.bind("<KP_Enter>", save_edit)
        entry.pack()
        entry.focus_set()
        self.root

    def update_graph(self):
        pass
