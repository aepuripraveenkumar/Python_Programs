# Problem Statement: Given an array A[] and a number x, check for pair in A[] with sum as x
# Write a program that, given an array A[] of n numbers and another number x,
# determines whether or not there exist two elements in S whose sum is exactly x.

# Time Complexity: Depends on what sorting algorithm we use.
# If we use Merge Sort or Heap Sort then O(nlogn) in worst case.
# If we use Quick Sort then O(n^2) in worst case.
# Auxiliary Space : Again, depends on sorting algorithm. For example 
# auxiliary space is O(n) for merge sort and O(1) for Heap Sort.


def hasArrayTwoCandidates(arr, Sum):
    arr = sorted(arr)   # sort array
    left = 0
    right = len(arr) - 1
    found = False
    while(left < right):
        if arr[left] + arr[right] < Sum:
            left += 1
        elif arr[left] + arr[right] > Sum:
            right -= 1
        else:
            print "Two elements", arr[left], "and", arr[right], "found whose sum is exactly", Sum
            left += 1
            right -= 1
            found = True
    return found


# O(n) method. Using Hashing
# This method works in O(n) time if range of numbers is known.
# Time Complexity: O(n)
# Auxiliary Space: O(R) where R is range of integers.
# If range of numbers include negative numbers then also it works.
# All we have to do for negative numbers is to make everything positive by adding
# the absolute value of smallest negative integer to all numbers.
# ex: A[]={ 1 , -8 , 12}, Sum = 4
# First find the smallest no. Here -8 is the smallest number.
# Add the absolute of the no. to each element in the array
# new array becomes {9 , 0 , 20}
# Now for (sum+8) i.e. 4+(8+8)=20.
# if a pair is present print the nos. subtracting 8 from each.
# pair= (0,20) i.e. (-8,12)
# --------------------------
CONST_MAX = 10000


def print_pairs(arr, Sum):
    lst = [0] * CONST_MAX
    found = False
    for ele in arr:
        temp = Sum - ele
        if temp > 0 and lst[temp] == 1:
            print "Two elements", ele, "and", temp, "found whose sum is exactly", Sum
            found = True
        lst[ele] = 1
    return found

if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10, -8, 8, 8]
    n = 16
    print "********** O(nlogn) or O(n^2)solution **********************"
    if (hasArrayTwoCandidates(arr, n)):
        print("Array has two elements with the given sum")
    else:
        print("Array doesn't have two elements with the given sum")

    # o(n) solution
    print ""
    print "********** O(n) solution **********************"
    if (print_pairs(arr, n)):
        print("Array has two elements with the given sum")
    else:
        print("Array doesn't have two elements with the given sum")