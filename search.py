import math
def search (data,key):
    i = 0
    while(i < len(data)):
        if (data[i]==key):
            return i
        i = i + 1
    return -1
def bi_search(data,key):
    low = 0
    high = len(data) + 1
    while(low <= high): 
        mid = math.floor((low+high)/2)
        if (data[mid] == key):
            return mid
        elif (data[mid] > key):
            high = mid - 1
        elif (data[mid] < key):
            low = mid + 1
    return -1
data = [4,7,53,972,2,96,41,12]
key = int(input("Enter a key: "))
loc = bi_search(data,key)
print(loc)