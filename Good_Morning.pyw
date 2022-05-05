# Good Morning
import tkinter, sys, time, os
from tkinter import *

# Path to the folder of all the paths
path = "C:\\Users\\Filip Sundblad\\Documents\\0. Projekt"
dirs = os.listdir(path)


# This function adds all files in dirs to a list. 
def total_file_list(List):
    for file in dirs: 
        List.append(file) 
    return List

# This function removes all objects in the list of files with the wrong file format
# by creating a new list and only adding the files of the correct format.
# this is dumb, I could probably just create that lsit from the start
# but not now 
def sift_the_list(List):
    placeholderlist = []
    filetype = ".tex"
    for file in List:
        correctFileType = False
        for x in range(1, 4):
            if file[len(file) -x] == filetype[len(filetype)-x]:
                correctFileType = True
            else: 
                correctFileType = False
                break
        if correctFileType == True:
            placeholderlist.append(file)
    return placeholderlist


# This function sorts two items at a time in the list using bubblesort
# Needs to be run repeatedly until the list is sorted
def sorter(List):
    placeholder = 0
    z = len(List)-1
    for x in range(0, z):
        # if time.ctime(os.path.getctime(path + "\\" + List[x])) > time.ctime(os.path.getctime(path + "\\" + List[x-1])):
        if os.path.getctime(path + "\\" + List[x]) < os.path.getctime(path + "\\" + List[x-1]):
            placeholder = List[x+1]
            List[x+1] = List[x]
            List[x] = placeholder
    return List

# This function checks to see if a list is sorted
def checkIfSorted(List):
    z = len(List)-1
    for x in range(0, z):
        if os.path.getctime(path + "\\" + List[x]) < os.path.getctime(path + "\\" + List[x+1]):
            return False
    return True

# This function runs a loop that runs the sorter and then checks if the list is sorted until
# the answer is yes 
def completeSorter(List):
    x = False
    while x == False:
        List = sorter(List)
        x = checkIfSorted(List)
    return List 


# Open window 
window = Tk()
window.title("Good Morning")
window.configure(bg='white')

# creates the list, adds the files, 
listOfProjects = []     
listOfProjects = total_file_list(listOfProjects)
listOfProjects = sift_the_list(listOfProjects)
listOfProjects = completeSorter(listOfProjects)

# Adds every filename plus when it was latest modified to the window. 
for file in listOfProjects:
    text = Text(window)
    text.insert(END, file + "\n" + time.ctime(os.path.getctime(path + "\\" + file)) + '\n')
    text.pack()

#The window is moved manually to the second screen and then fullscreened. 
movewindow = "+-300+-300"
window.geometry (movewindow)
window.state('zoomed')




# Runs the window
window.mainloop()

