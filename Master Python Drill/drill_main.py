
import tkinter
import os
from tkinter import *                   
from tkinter import filedialog
from tkinter import messagebox
import shutil

import drill_db
import drill_txt_find

def browse_button(folder_path):
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    return filename

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def submit_button(folder_path1, folder_path2):
    # Check fields to see if they contain anything
    if folder_path1.get() and folder_path2.get() =='':
        print("You must choose both filepaths")
        pass
    # Continue with main program
    else:
        drill_txt_find.checkFile(folder_path1.get(),folder_path2.get())
        drill_db.createDB()
        drill_db.insertFiles(folder_path2.get())

class ParentWindow(Frame):              
    def __init__(self, master,*args, **kwargs):        
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(450, 160))
        self.master.title('Check Files')


        # Buttons
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1,command=lambda: browse_button(folder_path1))
        self.btnBrowse1.grid(row=0, column=0, padx=(35,0), pady=(25,0), sticky=NW)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1,command=lambda: browse_button(folder_path2))
        self.btnBrowse2.grid(row=1, column=0, padx=(35,0), pady=(10,0), sticky=NW)

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2,command=lambda: submit_button(folder_path1, folder_path2))
        self.btnCheck.grid(row=2, column=0, padx=(35,0), pady=(10,0), sticky=NW)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2,command=lambda: ask_quit(self))
        self.btnClose.grid(row=2, column=4, padx=(35,0), pady=(10,0), sticky=SE)

        # Fields
        self.txtBrowse1 = Entry(self.master,textvariable=folder_path1,font=("Helvetica",14),fg='black')
        self.txtBrowse1.grid(row=0,column=1,padx=(30,0),pady=(25,0),columnspan=4)

        self.txtBrowse2 = Entry(self.master,textvariable=folder_path2,font=("Helvetica",14),fg='black')
        self.txtBrowse2.grid(row=1,column=1,padx=(30,0),pady=(10,0),columnspan=4)









if __name__ == "__main__":
    root = Tk()
    folder_path = StringVar()
    folder_path1 = StringVar()
    folder_path2 = StringVar()
    
    App = ParentWindow(root)
    root.mainloop()
