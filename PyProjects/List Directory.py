# Runs through a filepath to print all .txt files and their date creation stamp.

import os


fPath = 'C:\\PyProjects\\' # Filepath on system
fName = '' # Filename instantiation
textString = 'txt' #what filetype we search for

def checkFile(fPath,fName,textString):
    print("Of the following {} files, here are the text files and creation timestamps: \n".format(len(os.listdir(fPath))))
    for s in os.listdir(fPath):
        if s.endswith(textString):
            fName = s
            allPath = os.path.join(fPath,fName)
            print("-   ",allPath," --- ",os.path.getmtime(allPath))
    print("\nThank you for searching with us today.")


if __name__ == "__main__":
    checkFile(fPath,fName,textString)
    

