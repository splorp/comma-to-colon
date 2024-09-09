# -*- coding: utf-8 -*-
# Comma to Colon
# A script to turn a CSV file into a folder of Kirby CMS content files.
# Try Kirby for free: https://getkirby.com/


def filesafe(filename): # Create a Kirby safe filename
    safename = filename.replace(' ','-')
    safename = safename.replace('&','-')
    safename = safename.replace(',','-')
    safename = safename.replace('.','-')
    safename = safename.replace("'",'-')
    safename = safename.replace("%",'-')
    safename = safename.lower()
    return safename

try: # For importing the CSV module
    import csv
except:
    print("CSV module is required")
    exit()
try: # os required to create the individual folders
    import os
except:
    print('OS module is required')
    exit()

# Open the CSV file
csvsource = input('What is the name of the CSV file? ')
print ('Opening file: ' + csvsource)
blueprint = input('What is the name of the Kirby blueprint being used (without the .yml extension)? ') + '.txt'
directory = input('What is the name of the directory to save the files? ')

# Process the CSV file
sep = '\n\n----\n\n'
with open(csvsource, 'r') as f: # Open the file
    worklist = csv.DictReader(f)
    for row in worklist: # Turn each row into a Kirby content txt file
        line = ''
        try:
            title = row['title'] # title is the one heading that must be present
            filename = filesafe(title) + '/' + blueprint # Create a Kirby safe folder and use blueprint name
            print('Creating ' + filesafe(title) + '.txt')
        except:
            print("No 'title' item found so stopping. 'title' must be a heading and written in lowercase for the conversion to work.")
            exit()
        for val,item in row.items(): # Go through each column of each row in the CSV to create a Kirby file.
            line += val + ': ' + item + sep
        fullfile = directory + '/' + filename
        os.makedirs(os.path.dirname(fullfile), exist_ok=True)
        with open(fullfile,'w+') as sf: # Write the content txt file
            sf.write(line)
print("Finished")
exit()