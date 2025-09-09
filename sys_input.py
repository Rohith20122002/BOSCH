 
import sys

def reverseArray(A):

    # Reverse the list and return it

    return A[::-1]





data = sys.stdin.read().split()



A = list(map(int, data[0:]))  # Read the space-separated integers into a list

reversed_array = reverseArray(A) # Reverse the array

print(reversed_array)

print(' '.join(map(str, reversed_array)))

