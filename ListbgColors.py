import  tkinter as tk
from tkinter import ttk


class ColorBg(ttk.Frame):
   def __init__(self,parent):
     self.parent = parent
     #ttk.Frame.__init__(self, parent, padding="10  10 10 10")
     #self.pack(fill=tk.BOTH, expand=True)
     self.name = tk.StringVar()
     self.LColors=["red", "yellow", "light blue", "orange"]
     self.LlstColors = tk.StringVar()

     self.lstColors = tk.Listbox(window, width=10, height=5,
                 listvariable=self.LlstColors)
     self.lstColors.grid(row=0, column = 1)

     self.lstColors.pack()

     self.LlstColors.set(tuple(self.LColors))
     self.LlstColors.set(tuple(self.LColors))
     self.lstColors.bind("<<ListboxSelect>>",self.changeBackgroundColor)


   def changeBackgroundColor(self, event):
      self.lstColors["bg"] = self.lstColors.get   \
           (self.lstColors.curselection())

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Colors")
    window.geometry("300x200")
    ColorBg(window)
    window.mainloop()