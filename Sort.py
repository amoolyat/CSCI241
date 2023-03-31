import random
import copy
import sys

def insertion_sort(arr):
    for k in range(1,len(arr)):
        cur = arr[k]
        j = k
        while j>0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = cur

def selection_sort(arr):
    for k in range(len(arr)-1):
        minloc = k
        j = k + 1
        while j < len(arr):
            if arr[j] < arr[minloc]:
                minloc = j
            j+=1
        temp = arr[k]
        arr[k] = arr[minloc]
        arr[minloc] = temp
        
 if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Sort.py 10000 increasing
  # then printing the contents of sys.argv shows
  # ['Sort.py', '10000', 'increasing']
  # Note that the contents are all strings and may 
  # need to be converted as appropriate.
    if len(sys.argv) < 3 or not sys.argv[1].isnumeric or sys.argv[2] not in ('increasing','decreasing','random'):
    # This means the user did not provide the required arguments.
    # Show the correct usage.
        print('Usage: python Sort.py <array_length> <increasing|decreasing|random>')
    else:
        if sys.argv[2] == "increasing":
      # this syntax for generating a list is called "list comprehension"
            insertion_arr = [i for i in range(int(sys.argv[1]))]
        elif sys.argv[2] == "decreasing":
            insertion_arr = [int(sys.argv[1])-i for i in range(int(sys.argv[1]))]
        elif sys.argv[2] == "random":
      # the _ symbol is a placeholder for a variable whose value is ignored
            insertion_arr = [random.randint(0, 1000000000) for _ in range(int(sys.argv[1]))]
    selection_arr = copy.deepcopy(insertion_arr)
    insertion_sort(insertion_arr)
    selection_sort(selection_arr)
    #
    # Uncomment these two print lines to test with small arrays.
    #print(insertion_arr)
    #print(selection_arr)
  
