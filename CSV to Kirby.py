# -*- coding: utf-8 -*-

# Comma to Colon
# A script to turn a CSV file into a Kirby CMS content file.

def filesafe(filename): # Create a Kirby safe filename
    safename = filename.replace(' ','-')
    safename = filename.replace('&','-')
    safename = filename.replace(',','-')
    safename = safename.replace("'",'-').lower()
    return safename

try: # For importing the CSV module
    import csv
except:
    print("CSV module is required")
    exit()
try:
    import os
except:
    print('Needs OS module')
    exit()
try: # For file dialog
    from tkinter import filedialog
    from tkinter import *
except:
    print("tkinter.filedialog is required")
    exit()
    
# Open the CSV
filecsv = Tk()
filecsv.filename = filedialog.askopenfilename(initialdir = "~/",title = "Select csv file to open",filetypes = (("CSV files","*.csv"),("all files","*.*")))
print ("Opening file " + filecsv.filename)
cn = input("What is the name of the Kirby blueprint being used? ")
blueprint = cn + '.txt'
directory = filedialog.askdirectory(title = "Select where to save")
# Start work on the CSV file
sep = '\n\n----\n\n'
with open(filecsv.filename, 'r') as f: # Open the file
    worklist = csv.DictReader(f)
    for row in worklist:
        line = ''
        title = row['title'] # title is the one heading that must be present
        filename = filesafe(title) + '/' + blueprint # Createa Kirby safe folder and use blueprint name
        for val,item in row.items():
            line += val + ': ' + item + sep
        fullfile = directory + '/' + filename
        os.makedirs(os.path.dirname(fullfile), exist_ok=True)
        with open(fullfile,'w+') as sf:
            sf.write(line)
print("Finished")
exit()