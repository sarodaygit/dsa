# Merge Sort function with print statements
def merge_sort(arr, depth=0):
    # indent = "  " * depth  # Indentation for easier readability in the output
    # print(f"depth {depth} => {indent} Splitting: {arr}")
    print(f"depth {depth} => Splitting: {arr}")
    
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        
        # Dividing the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        print(f'depth {depth} => left_half {left_half}   right_half {right_half}')
        

        # Recursive calls to sort both halves
        merge_sort(left_half, depth + 1)
        merge_sort(right_half, depth + 1)

        # Initialize pointers for left_half, right_half, and the main array
        i = 0  # Pointer for left_half
        j = 0  # Pointer for right_half
        k = 0  # Pointer for the main array 'arr'
        
        # Merging the sorted halves
        print("Merging:", left_half, "and", right_half)
        while i < len(left_half) and j < len(right_half):
            print(f"Comparing left_half[{i}] = {left_half[i]} with right_half[{j}] = {right_half[j]}")
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                print(f"arr[{k}] = left_half[{i}] -> {arr[k]}")
                i += 1
            else:
                arr[k] = right_half[j]
                print(f"arr[{k}] = right_half[{j}] -> {arr[k]}")
                j += 1
            k += 1
            print(f"Updated indices: i = {i}, j = {j}, k = {k}")

        # Checking if any element was left in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            print(f"arr[{k}] = left_half[{i}] -> {arr[k]} (Remaining element from left_half)")
            i += 1
            k += 1

        # Checking if any element was left in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            print(f"arr[{k}] = right_half[{j}] -> {arr[k]} (Remaining element from right_half)")
            j += 1
            k += 1
            print(f"Updated indices after processing right_half: j = {j}, k = {k}")
            print(f"Array after merging: {arr}")

        print(f"depth {depth} Merging: {arr}")
    else:
        print(f"depth {depth} Base case reached: {arr}")


# Test the merge sort function with print statements
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    merge_sort(arr)
    print("Sorted array:", arr)
