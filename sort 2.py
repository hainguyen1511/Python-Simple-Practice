#Name: Hai T. Nguyen
#CS299
import math
def merge(data, temp, low, mid, high):
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if data[i] < data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1

    while i <= mid:
        temp.append(data[i])
        i += 1

    while j <= high:
        temp.append(data[j])
        j += 1

    for k in range(low, high + 1):
        data[k] = temp[k - low]

def my_sort(data, low, high):
    if low < high:
        mid = (low + high) // 2
        my_sort(data, low, mid)
        my_sort(data, mid + 1, high)
        temp = []
        merge(data, temp, low, mid, high)
################# MAIN ##################
data = []
print("Enter the data, and finish with -1")
z = float(input())
while z >= 0:
    data.append(z)
    z = float(input())
print("Unsorted data:", data)
my_sort(data, 0, len(data) - 1)
print("Sorted data:", data)