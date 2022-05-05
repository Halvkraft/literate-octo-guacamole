# Lista
# Alla filer med rätt format läggs till i listan. Eller? 
# En funktion för att göra en lista av alla filer
# En funktion för att sålal bort alla felaktiga filer
# En funktion för att sortera filerna
# En funktion för att skriva ut filerna 

import os, sys, time
path = "C:\\Users\\Filip Sundblad\\Documents\\0. Projekt"
dirs = os.listdir(path)

# funktion 1:
def total_file_list(List):
    for file in dirs:
        filename = path + "\\" + file
        List.append(file) 
    return List

# funktion 2
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

# funktion 3
def completeSorter(List):
    x = False
    while x == False:
        List = sorter(List)
        x = checkIfSorted(List)
        # print(x)
    return List 

# funktion 4
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

# funktion 5
def checkIfSorted(List):
    z = len(List)-1

    for x in range(0, z):
        if os.path.getctime(path + "\\" + List[x]) < os.path.getctime(path + "\\" + List[x+1]):
            return False
    return True




theList = []        
theList = total_file_list(theList)
theList = sift_the_list(theList)
theList = completeSorter(theList)

# print(theList)
for x in theList:
    print (x)
    print (path + "\\" + x)
    print (os.path.getctime(path + "\\" + x))
    print(time.ctime(os.path.getctime(path + "\\" + x)))
