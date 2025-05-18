from tkinter import *

main = Tk()

class App():
    def __init__(self):
        self.man = main 
        self.tela() 
        main.mainloop()
    def tela(self):
        self.man.title('Wanessa')
        self.man.configure(background= '#4169E1')
        self.man.geometry('700x500')
        self.man.resizable(True, True)
        self.man.maxsize(width=900, height=700)
        self.man.minsize(width=400, height=300)



App()


