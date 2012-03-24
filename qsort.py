
def choosePivotLow(A, l, r):
# Write your code here.

def choosePivotHigh(A, l, r):
# Write your code here.

def choosePivotMedian(A, l, r):
# Write your code here.

def partition(A, l, r):
# Write your code here.

def quicksort(A, l, r, choosePivot):
# Write your code here, make sure to return number of comparisons.
# The last parameter is a function that given an array, lower and upper
# boundaries, takes care of pivot selection, for example one of the ones above.


# open the file, load the numbers into a list, quicksort it
# and print the number of comparisons
if __name__== "__main__":
  with open(sys.argv[1]) as file:
    strings = file.read().split("\n")
    l = [int(x) for x in strings if len(x)]
    c = quicksort(l, 0, len(l)-1, choosePivotLow)
    print c