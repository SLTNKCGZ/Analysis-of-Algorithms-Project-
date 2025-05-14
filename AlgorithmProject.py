import gc

import re
import time
from collections import defaultdict

import sys
#Increasing the recursion limit for algorithms like Quick Sort that rely on recursion.
sys.setrecursionlimit(100000) 
import matplotlib.pyplot as plt

# Finds the majority element using brute-force comparison.
# Time complexity: O(n^2)
def find_majority(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > n // 2:
            return arr[i]
    return -1

# Sorts the array using insertion sort.
# Time complexity: O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Uses insertion sort to sort the array and picks the middle element as candidate.
def majority_insertion_sort(arr):
    sorted_arr = insertion_sort(arr.copy())
    n=len(arr)
    candidate = sorted_arr[n // 2]
    count = arr.count(candidate)
    return candidate if count > n // 2 else -1

# Sorts the array using merge sort.
# Time complexity: O(n log n)
def merge_sort(arr):
    n=len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        merged.append(left[i] if left[i] <= right[j] else right[j])
        if left[i] <= right[j]: i += 1
        else: j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Uses merge sort to sort and selects the middle element as a candidate.
def majority_merge_sort(arr):
    n=len(arr)
    sorted_arr = merge_sort(arr.copy())
    candidate = sorted_arr[n // 2]
    count = arr.count(candidate)
    return candidate if count > n // 2 else -1

# Helper function for partitioning used in quick sort.
def partition(arr, low, high):
    pivot_index = low
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while j >= i and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

# Sorts the array using quick sort.
# Time complexity: O(n log n) on average
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Uses quick sort and picks the middle element as candidate.
def majority_quick_sort(arr):
    arr_copy = arr.copy()
    n=len(arr) 
    quick_sort(arr_copy, 0, n - 1)
    candidate = arr_copy[n // 2]
    count = arr.count(candidate)
    return candidate if count > n // 2 else -1

# Uses divide and conquer to recursively find the majority element.
# Time complexity: O(n log n)
def divide_conquer(arr):
    def majority_element(left, right):
        if left == right:
            return arr[left]
        mid = (right - left) // 2 + left
        left_majority = majority_element(left, mid)
        right_majority = majority_element(mid + 1, right)
        if left_majority == right_majority:
            return left_majority
        left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_majority)
        right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_majority)
        if left_count > (right - left + 1) // 2:
            return left_majority
        if right_count > (right - left + 1) // 2:
            return right_majority
        return -1
    return majority_element(0, len(arr) - 1)

# Uses a hash table to count element frequencies.
# Time complexity: O(n)
def hashing_majority(arr):
    count_map = defaultdict(int)
    n = len(arr)
    for num in arr:
        count_map[num] += 1
        if count_map[num] > n // 2:
            return num
    return -1

# Uses Boyer-Moore majority vote algorithm.
# Time complexity: O(n)
def boyer_moore(arr):
    n = len(arr)
    candidate = -1
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    count = sum(1 for num in arr if num == candidate)
    return candidate if count > n // 2 else -1




# Uses bit manipulation to find the majority element.
# Time complexity: O(N*logN)
def bit_majority(arr):
    n = len(arr)
    INT_SIZE = 32  
    result = 0

    for i in range(INT_SIZE):
        bit_count = 0
        for num in arr:
            if (num >> i) & 1:
                bit_count += 1
        if bit_count > n // 2:
            result |= (1 << i)

    if arr.count(result) > n // 2:
        return result
    return -1

#Test algorithms and measure the time for each algorithm.
def test_all_algorithms(arr):
    methods = [
        ("Brute Force", find_majority),
        ("Insertion Sort", majority_insertion_sort),
        ("Merge Sort", majority_merge_sort),
        ("Quick Sort", majority_quick_sort),
        ("Divide and Conquer", divide_conquer),
        ("Hashing", hashing_majority),
        ("Boyer Moore", boyer_moore),
        ("Bit Manipulation", bit_majority)
    ]


    print(f"{'Algorithm':<22} | {'Result':<6} | {'Time (ms)':<10}")
    print("-" * 45)
    durations = []
    
    for name, func in methods:
        gc.disable()
        start = time.perf_counter()
        result = func(arr)
        duration = (time.perf_counter() - start) * 1000 
        gc.enable()
        print(f"{name:<22} | {str(result):<6} | {duration:<12.5f}")
        durations.append(duration)
    
    return durations


#Read the file and parse arrays from the file.
def parse_arrays_from_file(file_path):
    arrays = []
    buffer = ""
    count=0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            count=count+1
            buffer += line.strip()
            if "]" in buffer:
                matches = re.findall(r"\[([^\]]+)\]", buffer)
                for match in matches:
                    numbers = [int(num.strip()) for num in re.split(r'[,\s]+', match) if num.strip().isdigit()]
                    arrays.append(numbers)
                buffer = "" 
    return arrays


if __name__ == "__main__":
    files = ["input_1000.txt", "input_3000.txt","input_5000.txt","input_10000.txt", "input_12500.txt","input_15000.txt","input_20000.txt", "input_25000.txt", "input_37500.txt","input_50000.txt"]
    array=[]
    #Take files and array in the each file.Then take algorithm's durations. 
    for file in files:
        
        inputs = parse_arrays_from_file(file)  

        if not inputs:
           print("Could not find array.")
        else:
           arr=[]
           for input in inputs:
              duration=test_all_algorithms(input)
              arr.append(duration)
              print("\n\n")


        array.append(arr)
        print("*" * 180)
        print("\n")
 
    algorithms=["Brute Force","Insertion Sort","Merge Sort","Quick Sort","Divide and Conquer","Hashing","Boyer Moore","Bit Manipulation"]
    inputs=["Pure Majority","Balanced Pairs","First Element Majority","Last Element Majority","All Unique Elements","Balanced Half Elements","Random Early Majority","Random Late Majority","Periodic Distribution","Sorted Ascending","Sorted Descending"]
    sizes=[1000,3000,5000,10000,12500,15000,20000,25000,37500,50000]
    #print durations
    for alg in range(len(algorithms)):
        print(f"{algorithms[alg]}:\n")
    
        header = f"{'Input':<22}" + ''.join(f"| {str(sizes[size]):>12.8} " for size in range(len(sizes)))
        print(header)
        print("-" * len(header))

        for inp in range(len(inputs)):
            row = f"{inputs[inp]:<22}"
            for size in range(len(sizes)):
                row += f"| {str(array[size][inp][alg]):>12.8} "
                
            print(row)
        print("\n\n") 
     
linestyles = ['-', '--', '-.', ':', '-', '--']
markers = ['o', 's', '^', 'D', 'v', '*']
#Create graphs
for alg_idx, alg_name in enumerate(algorithms):
    plt.figure(figsize=(10, 5))

    for inp_idx, input_name in enumerate(inputs):
        execution_times = [array[size_idx][inp_idx][alg_idx] for size_idx in range(len(sizes))]
        plt.plot(sizes, execution_times,
                 marker=markers[inp_idx % len(markers)],
                 linestyle=linestyles[inp_idx % len(linestyles)],
                 label=input_name)

    plt.title(f'Performance of {alg_name}')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (ms)')
    plt.xticks(sizes, rotation=30)  
    plt.grid(True)
    plt.legend(title="Input Type", loc='upper left')
    plt.tight_layout()
    plt.show()
