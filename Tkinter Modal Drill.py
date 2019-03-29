import tkinter                          
from tkinter import *
from tkinter import filedialog

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    return filename

class ParentWindow(Frame):              
    def __init__(self, master):        
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(400, 100))
        self.master.title('Find Directory')

        # Button
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1, command=browse_button)
        self.btnBrowse1.grid(row=0, column=0, padx=(35,0), pady=(25,0), sticky=NW)
        # Text Field
        self.txtBrowse1 = Entry(self.master,textvariable=folder_path,font=("Helvetica",10),fg='black')
        self.txtBrowse1.grid(row=0,column=1,padx=(30,0),pady=(25,0),columnspan=10)


if __name__ == "__main__":
    root = Tk()
    folder_path = StringVar()
    App = ParentWindow(root)
    root.mainloop()
