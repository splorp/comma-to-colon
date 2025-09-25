# Comma to Colon

This script converts an CSV file to a flat file YAML structure for use with [Kirby](https://getkirby.com/).

This version of the code is based on the original [Comma to Colon](https://github.com/myleswrite/Comma-to-Colon) script by [Myles Winstone](https://writeandweb.uk/).

## Requirements

+ [Python](https://www.python.org/downloads/) 3.8 or later

### How it works

+ Run the script.
+ Specify the CSV file you want to convert.
+ Specify the name of the .yml blueprint file you want to use, eg: `item`
+ Each row in the CSV will be converted into a file in its own folder, eg: `item.txt`
+ Specify a directory where you want to save the converted files and folders.
+ Voilà!

### Notes

+ The first row of the CSV file is taken to be a header row for the columns of data.
+ One of the headers must be named `title` and must be lowercase.
+ All other headers can be named anything you like.
+ The script will create text files using the header names to label the fields.
