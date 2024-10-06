def binary_search(arr, target):
    lowindex = 0
    highindex = len(arr) - 1
    is_ascended = arr[lowindex] < arr[highindex]
    while lowindex <= highindex:
        midindex = (lowindex + highindex) // 2
        guess =  arr[midindex]
        if guess == target:
            return midindex
        if is_ascended:
            if guess < target:
                lowindex =  midindex +1
            elif guess > target:
                highindex = midindex -1
        else:
            if guess < target:
                highindex = midindex - 1
            elif guess > target:
                lowindex = midindex + 1


    return -1


# Example usage:
# arr = [9, 7, 5, 3, 1]  # Descending order array
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# arr = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
target = 1

result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")
