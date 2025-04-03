# sorting function
import math
def merge(data, low, mid, high):
    left = data[low:mid+1]
    right = data[mid+1:high+1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

def my_sort(data, low, high):
    if low < high:
        mid = math.floor((low + high) / 2)

        my_sort(data, low, mid)
        my_sort(data, mid+1, high)

        merge(data, low, mid, high)

data = []
print("Enter the data, and finish with -1")
z = float(input())
while z >= 0:
    data.append(z)
    z = float(input())

print("Unsorted data:", data)
my_sort(data, 0, len(data)-1)

print("Sorted data:", data)
