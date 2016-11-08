import random as ran
import glob
from postTool import config_parse, post

#Initialize holding list for text file data. Read in all text files in directory.
temp = []
files = glob.glob('./*.txt')

#Cycle through list of files, read in data as seperate lines, select 3 lines at random
for i in files:
    with open(i) as f:
        stor  = f.readlines()
        temp.append(ran.sample(stor, 3))

#Initialize workout lists with title blocks and spacing
workout1 = ["----Workout #1----\n"]
workout2 = ["\n----Workout #2----\n"]
workout3 = ["\n----Workout #3----\n"]

#Append elements from imbedded lists in list "temp" to workout lists
for i in temp:
    workout1.append(i[0])
    workout2.append(i[1])
    workout3.append(i[2])

#Combine formatted lists for Wordpress post tool
workout = "".join(workout1) + "".join(workout2) + "".join(workout3)
post(workout, ["Workout"])

