# Runs through a filepath to print all .txt files and their date creation stamp.

import os
import time
import drill_main
import drill_db
import shutil

fPath = ''
destPath = ''

def checkFile(fPath, destPath):
    # Filepath on system
    fName = '' # Filename instantiation
    textString = 'txt' #what filetype we search for
    print("Of the following {} files, here are the text files and creation timestamps: \n".format(len(os.listdir(fPath))))
    for s in os.listdir(fPath):
        if s.endswith(textString):
            fName = s
            allPath = os.path.join(fPath,fName)
            print("-   ",allPath," --- ",time.ctime(os.path.getmtime(allPath)))
            shutil.move(allPath, destPath)
    print("\nThank you for searching with us today. \n")


if __name__ == "__main__":
    #checkFile(fPath,fName,textString)
    pass
    

