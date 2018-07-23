import time

N = 100000
N2 = 1000000
N3 = 10000000
s = 21500


# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) / 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# binary search for N=100,000  ==================================================================================
array = []
for x in range(s, s + N):
    array.append(x)
print("array length", len(array))

elementArray = []
count = 0
while (count < 1000):
    if (count < 150):
        for x in range(100, s, s / 150):
            elementArray.append(x)
            count += 1
    elif (count < 700 and count > 150):
        for x in range(s + 700, s + N, N / 700):
            elementArray.append(x)
            count += 1
    else:
        for x in range(N + 100, N + s, s / 150):
            elementArray.append(x)
            count += 1

print("length element array", len(elementArray))


# Function cal
start_time = time.time()
for x in range(0, len(elementArray)):
    result = binarySearch(array, 0, len(array) - 1, elementArray[x])
    # if result != -1:
    #     print result
    # else:time()
    #     print result
end_time = time.time()

print("time difference for N", (end_time - start_time) * 1000)

# Binary search for N=1,000,000 =================================================================================
array2 = []
for x in range(s, s + N2):
    array2.append(x)
print("array length", len(array2))

elementArray2 = []
count = 0
while (count < 1000):
    if (count < 150):
        for x in range(100, s, s / 150):
            elementArray2.append(x)
            count += 1
    elif (count < 700 and count > 150):
        for x in range(s + 500, s + N2, N2 / 700):
            elementArray2.append(x)
            count += 1
    else:
        for x in range(N2 + 100, N2 + s, s / 150):
            elementArray2.append(x)
            count += 1

print("length element array2", len(elementArray2))

# Function cal
start_time = time.time()
for x in range(0, len(elementArray2)):
    result = binarySearch(array2, 0, len(array2) - 1, elementArray2[x])
    # if result != -1:
    #     print result
    # else:time()
    #     print result
end_time = time.time()

print("time difference for N2", (end_time - start_time) * 1000)

# Binary search for N= 10,000,000 =========================================================================
array3 = []
for x in range(s, s + N3):
    array3.append(x)
print("array length", len(array3))

elementArray3 = []
count = 0
while (count < 1000):
    if (count < 150):
        for x in range(100, s, s / 150):
            elementArray3.append(x)
            count += 1
    elif (count < 700 and count > 150):
        for x in range(s + 500, s + N3, N3 / 700):
            elementArray3.append(x)
            count += 1
    else:
        for x in range(N3 + 100, N3 + s, s / 150):
            elementArray3.append(x)
            count += 1

print("length element array3", len(elementArray3))

# Function cal
start_time = time.time()
for x in range(0, len(elementArray3)):
    result = binarySearch(array3, 0, len(array3) - 1, elementArray3[x])
    # if result != -1:
    #     print result
    # else:time()
    #     print result
end_time = time.time()

print("time difference for N3", (end_time - start_time) * 1000)