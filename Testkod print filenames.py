import os, sys, time
from turtle import end_fill
path = "C:\\Users\\Filip Sundblad\\Documents\\0. Projekt"
dirs = os.listdir( path)

# def huvudfunktion():

def fileTypeChecker(): 
    filetype = ".tex"
    List = []
    for file in dirs:
        correctFileType = False
        for x in range(len(file)-5, len(file)-1): 
            if file[x] == filetype[x]:
                correctFileType = True
            else: 
                correctFileType = False
                break
            if correctFileType == True:
                List += file
    return List

            




for file in dirs:
    filename = path + "\\" + file
    modificationTime = time.ctime(os.path.getctime(filename))
    print(file, modificationTime, os.path.getctime(filename))



def sorter(List):
    placeholder = 0
    z = len(List)-1
    for x in range(0, z):
        if List[x] > List[x+1]:
            placeholder = List[x+1]
            List[x+1] = List[x]
            List[x] = placeholder
    return List


def checkIfSorted(List):
    z = len(List)-1
    for x in range(0, z):
        if List[x] > List[x+1]:
            return False
    return True

def completeSorter(List):
    x = False
    while x == False:
        List = sorter(List)
        x = checkIfSorted(List)
    return List 