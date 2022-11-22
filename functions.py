### CONTAINS



def contains(arr, item):
    for element in arr:
        if element == item:
            return True
    
    return False


### REVERSE
def reverse(arr):
    nlist = []
    for i in range(len(arr) - 1, -1, -1):
        nlist.append(arr[i])
    return nlist

    
### indexof
def indexof(arr, element):

    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1
        

### SWAP
def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

### INDEX OF MIN



def indexofmin(arr):
    for i in range(1, len(arr)):
        if i < arr[0]:
            arr[0] = arr[i]
    return i


     

        
        
        

numarray = [21, 34, 12, 9, 3, 4, 6, 2]
coolest_array = ["snow", "ice", "blizzard", "santa", "hi"]
functionarray = ["contains", "indexof", "reverse", "swap", "indexofMin"]

loop = True
while loop:
    ### print functionsarray
    for i in functionarray:
        print(i, end = ' ')

    print("\n\nSelect an option:")
    print("1: contains")
    print("2: indexof")
    print("3: reverse")
    print("4: swap")
    print("5: indexofmin")

    runfun = int(input("which function would you like to run (1-...)")) - 1
    if runfun == 0:
        ### CONTAINS FUNCTION
        print("Function 1")
        for i in coolest_array:
            print(i, end = ' ')
        print("----")
        if contains(coolest_array, "santa"):
            print("Merry christmans")
        else:
            print("not so very merry")
    elif runfun == 1:
        ### INDEXOF FUNCTION
        print("Function 2")
        for i in coolest_array:
            print(i, end = ' ')
        print("----")
        print(indexof(coolest_array, "hi"))
    elif runfun == 2:
        ### REVERSE FUNCTION
        print("Function 3")

        coolest_array = ["snow", "ice", "blizzard", "santa", "hi"]
        reversed_list = reverse(coolest_array)
        print(reversed_list)

    
        print(coolest_array)
    
        print("done")
    elif runfun == 3:
        ### SWAP FUNCTION
        print("Function 4")
        ele1 = int(input("What is the first element that you'd like to swap"))
        ele2 = int(input("What is the secdond element that you'd like to swap"))
        print(swap(coolest_array, ele1, ele2))
    elif runfun == 4:
        ### INDEXOFMIN FUNCTION
        print("Function 5")
        w = indexofmin(numarray)
        print(w)
    elif runfun == 5:
        ## QUIT
        print("Quit")
        loop =  False








