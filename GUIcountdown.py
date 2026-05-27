#countdown and countdown in tkinter

import time

#def countdown(t):
#   while t:
#      mins, secs = divmod(t, 60)
#      timer = '{:02d}:{:02d}'.format(mins, secs)
#      print(timer, end="\r")
#      time.sleep(1)
#      t -= 1
#   print('Blast Off!!!')

#t = input("Enter the time in seconds: ")
#countdown(int(t))

# Countdown with tkinter
import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self, cd =10):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        #self.countdown(10)
        self.countdown(cd)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    t = int(input("Enter the time in seconds: "))
    app = ExampleApp(t)
    app.mainloop()