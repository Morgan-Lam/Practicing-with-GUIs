import  tkinter as tk
from tkinter import ttk

class GUIExit (ttk.Frame):
    def __init__(self, parent):
        self.parent = parent
        ttk.Frame.__init__(self, padding="10  10 10 10")
        self.pack(fill=tk.BOTH, expand=True)

        self._btnExit=ttk.Button(self, text="Exit")
        self._btnExit.pack()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("messing with GUIs")
    window.geometry("300x200")
    GUIExit(window)
    window.mainloop()
