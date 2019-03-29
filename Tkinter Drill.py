
import tkinter                          
from tkinter import *                   


class ParentWindow(Frame):              
    def __init__(self, master):        
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(450, 160))
        self.master.title('Check Files')
        #self.master.config(bg='lightgrey')

        # Buttons
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse1.grid(row=0, column=0, padx=(35,0), pady=(25,0), sticky=NW)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=1, column=0, padx=(35,0), pady=(10,0), sticky=NW)

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCheck.grid(row=2, column=0, padx=(35,0), pady=(10,0), sticky=NW)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2)
        self.btnClose.grid(row=2, column=4, padx=(35,0), pady=(10,0), sticky=SE)

        # Fields
        self.txtBrowse1 = Entry(self.master,font=("Helvetica",16),fg='black')
        self.txtBrowse1.grid(row=0,column=1,padx=(30,0),pady=(25,0),columnspan=4)

        self.txtBrowse2 = Entry(self.master,font=("Helvetica",16),fg='black')
        self.txtBrowse2.grid(row=1,column=1,padx=(30,0),pady=(10,0),columnspan=4)









if __name__ == "__main__":
    root = Tk()                         
    App = ParentWindow(root)
    root.mainloop()
