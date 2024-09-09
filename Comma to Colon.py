# -*- coding: utf-8 -*-
#
# Comma to Colon
#
# Python 3 script that converts a CSV file into
# a folder of content files for use with Kirby CMS
# https://getkirby.com/
#
# Based on the original script by Myles Winstone
# https://github.com/myleswrite/Comma-to-Colon

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
    # Convert each row in the CSV into a Kirby content file
    for row in worklist:
        line = ''
        try:
            # A heading named 'title' must be present
            title = row['title']
            # Create a safely named folder and use the named Blueprint
            filename = filesafe(title) + '/' + blueprint
            print('Creating ' + filesafe(title) + '.txt')
        except:
            print("No 'title' heading found. A column heading named 'title' is required and must be lowercase.")
            exit()
        # Step through each column of each row in the CSV to create content files
        for val,item in row.items():
            line += val + ': ' + item + sep
        fullfile = directory + '/' + filename
        os.makedirs(os.path.dirname(fullfile), exist_ok=True)
        # Save the content file
        with open(fullfile,'w+') as sf:
            sf.write(line)
print("Finished")
exit()
