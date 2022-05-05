import random

List1 = []
List2 = []
List3 = []

def Listmaker(List): 
    while len(List) < 10: 
        random_number = random.randrange(1, 10)
        List += [random_number]
    return(List)

Listmaker(List1)
Listmaker(List2)
Listmaker(List3)

print(List1, List2, List3)

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

List1 = completeSorter(List1)
List2 = completeSorter(List2)
List3 = completeSorter(List3)

print(List1, List2, List3)