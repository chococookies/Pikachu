#csv processing
import csv
#file navigation
import os, sys
#terminal commands
import subprocess

#contains all canvas csv information
canvas_dict = {}
#contains all gform csv information
gform_dict = {}
#contains all csid as key and their associated partner as value
#redundantly adds both. csid : partner csid, name (of key csid, not partner)
csid_dict = {}
#turnin base folder for the project
turnin_folder = "/share/turnin/graders/lara/cs327epj2/"
#list of filenames needed for the projects
zip_filename = "XML.zip"
project_filenames = ['XML.html', 'XML.log', 'XML.py', 'RunXML.in', 'RunXML.out', 'RunXML.py', 'TestXML.out', 'TestXML.py']

# Process Canvas Csv
with open('grad.csv', 'rb') as grades:
    rd = csv.reader(grades)
    #csv row[0] is the name field
    for row in rd:
        canvas_dict[row[0]] = row[1:]

# Process google forms
# Get all names of people who turned in
# Get all CS ids for people who allegedly
#     turned in (and partners who turned in).
with open('forms.csv', 'rb') as gforms:
    rd = csv.reader(gforms)
    #gforms, 1 is name, 2 is last name\
    #       12, 13 is partner name, lastname
    #       6, 16 is for CSids (useful to check turnin submissions)
    for row in rd:
        name = str(row[2] + ', ' + row[1]).upper()
        gform_dict[name] = row[3:]
        csid_dict[row[6]] = row[16], name
        #if student has a partner
        if row[12] != "":
            name = str(row[13] + ', ' + row[12]).upper()
            gform_dict[name] = row[3:]
            csid_dict[row[16]] = row[6], name
            

#print csid_dict


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
            print name + " did not turn in a google form but is in class list. Most likely did not turn in project."


#Now check actual submission
#submissions stores any problems with submissions
submissions = {}

folders = os.listdir(turnin_folder)
for f in folders:
     submissions[f] = []
     if f not in csid_dict:
         print "Submission by " + f + "does not have an associated google form"
     #checkoutput time! chaeck that files unzip, and have the correct amount of files
     unzip_file = turnin_folder+f+"/"+zip_filename
     unzip_folder = turnin_folder+f+"/submission"
     # print unzip_file
     # print turnin_folder
     try:
         unzip_result = subprocess.check_output(["unzip", "-o", unzip_file, "-d", unzip_folder])
         submitted_files = subprocess.check_output(["ls", unzip_folder])
         submitted_files = submitted_files.split()
     # print submitted_files
         for fil in project_filenames:
             if fil not in submitted_files:
                 #print fil
                 submissions[f] += [f + " did not turn in/couldn't find " + fil + "."]
     except:
         submissions[f] += ["Problem unzipping " + f+"/"+zip_filename + " could be a corrupt submission."]
     #just once for debug
     #sys.exit(0)
     

#Report all submission problems
for k in submissions:
    if submissions[k] != []:
          print submissions[k]
#print submissions
    

#print gform_dict
#works so far


