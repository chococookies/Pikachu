#csv processing
import csv
#file navigation
import os, sys

canvas_dict = {}
gform_dict = {}
turnin_folder = "/share/turnin/graders/lara/cs327epj2/"
project_filenames = ['makefile', 'XML.html', 'XML.log', 'XML.py', 'RunXML.in', 'RunXML.out', 'RunXML.py', 'TestXML.out', 'TextXML.py']

# Process Canvas Csv
with open('grad.csv', 'rb') as grades:
    rd = csv.reader(grades)
    #csv row[0] is the name field
    for row in rd:
        canvas_dict[row[0]] = row[1:]

# Process google forms
with open('forms.csv', 'rb') as gforms:
    rd = csv.reader(gforms)
    #gforms, 1 is name, 2 is last name\
    #       12, 13 is partner name, lastname
    for row in rd:
        name = str(row[2] + ', ' + row[1]).upper()
        gform_dict[name] = row[3:]
        if row[12] != "":
            name = str(row[13] + ', ' + row[12]).upper()
            gform_dict[name] = row[3:]

             


#print canvas_dict
#Check which students didn't turn in Google Form from class
for name in canvas_dict:
    if name not in gform_dict:
        #check for canvas artifacts
        if name == "Student":
            #print canvas_dict[name]
            pass
        elif name == "    Points Possible":
            #print canvas_dict[name]
            pass
        else:
            print name + " did not turn in a google form but is in class list."


#Now check actual submission
submissions = {}
folders = os.listdir(turnin_folder)
for f in folders:
     print f
     submissions[f] = ""

    

#print gform_dict
#works so far


