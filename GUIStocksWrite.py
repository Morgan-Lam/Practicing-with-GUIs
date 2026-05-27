import  tkinter as tk
from tkinter import ttk

class GUIStocks (ttk.Frame):
   def __init__(self, parent):
      self.parent = parent
      ttk.Frame.__init__(self, padding="10  10 10 10")
      self.pack(fill=tk.BOTH, expand=True)
      self.name = tk.StringVar()
      self.stocksym = tk.StringVar()
      self.stockcount = tk.StringVar()
      self.stockprice = tk.StringVar()
      self.totalprice = tk.StringVar()
      ttk.Label(self, text="Name").grid(row=0, column=0, padx=20, pady=5, sticky=tk.E)
      ttk.Entry(self, width=20, textvariable=self.name).grid(row=0, column=1, sticky=tk.W)

      ttk.Label(self, text="Stock Symbol").grid (row=1, column=0, sticky=tk.E)
      ttk.Entry(self, width=8, textvariable=self.stocksym).grid(row=1, column=1, sticky=tk.W)

      ttk.Label(self, text="Stock Count").grid(row=2, column=0, sticky=tk.E)
      ttk.Entry(self, width=8, textvariable=self.stockcount).grid(row=2, column=1, sticky=tk.W)

      ttk.Label(self, text="Stock Price").grid(row=3, column=0, sticky=tk.E)
      ttk.Entry(self, width=8, textvariable=self.stockprice).grid(row=3, column=1, sticky=tk.W)

      ttk.Label(self, text="Total price").grid(row=4, column=0, sticky=tk.E)
      ttk.Label(self, width=8, textvariable=self.totalprice).grid(row=4, column=1, sticky=tk.W)

      ttk.Button(self, text="Calculate Price", command=self.StockTotal).grid(row=5, column=0, columnspan=2, padx=75)
      ttk.Button(self, text="Write to File", command=self.WriteRecord).grid(row=6, column=0,  padx=75)
      ttk.Button(self, text="Exit", command=self.exit).grid(row=6, column=2, columnspan=2, padx=75)
      for child in self.winfo_children():
          child.grid_configure(padx=5, pady=9)

        
   def StockTotal(self):
       try:
           stockp = float(self.stockprice.get())
           stockc = float(self.stockcount.get())
           self.totalprice.set('${0:7.2f}'.format(float(stockp*stockc)))
       except Exception as e:
            self.totalprice.set(100)

   def WriteRecord(self):
        self.outfile = open("Stocks.txt", 'a')
        print(self.name.get(), self.stocksym.get(), self.stockcount.get(), self.stockprice.get())

        record=(self.name.get() + ","+ self.stocksym.get() +","+ self.stockcount.get()
                +"," + self.stockprice.get() +"\n")
        self.outfile.write(record)
        self.outfile.close()
   def exit(self):
        window.destroy()
        

if __name__ == "__main__":
    window = tk.Tk()
    window.title("CIMP 8A")
    GUIStocks(window)
    window.mainloop()
