#Remove all duplicates from a given string


# Multiple ways to solve this problem

# Method 1:
print "******************* Method 1 *********************** "
foo = "python programing"
print ''.join(set(foo)) # if order is not important
print ''.join(sorted(set(foo), key=foo.index)) # if order does matters Time Complexity: O(n^2)

# Method 2:
print "******************* Method 2 *********************** "
seen = set()
result = []
for c in foo:
    if c not in seen:
        result.append(c)
        seen.add(c)
result = ''.join(result)
print result

# Method 3:
print "******************* Method 3 *********************** "
foo = "SSYYNNOOPPSSIISS"
import collections
print ''.join(collections.OrderedDict.fromkeys(foo))

print "******************* Method 4 *********************** "
# Method 4
# Time Complexity: O(n)

# Python program to remone duplicate characters from an
# input string
NO_OF_CHARS = 256

# Since strings in Python are immutable and cannot be changed
# This utility function will convert the string to list


def toMutable(string):
    List = []
    for i in string:
        List.append(i)
    return List

# Utility function that changes list to string


def toString(List):
    return ''.join(List)

# Function removes duplicate characters from the string
# This function work in-place and fills null characters
# in the extra space left


def removeDups(string):
    bin_hash = [0] * NO_OF_CHARS
    ip_ind = 0
    res_ind = 0
    temp = ''
    mutableString = toMutable(string)

    # In place removal of duplicate characters
    while ip_ind != len(mutableString):
        temp = mutableString[ip_ind]
        if bin_hash[ord(temp)] == 0:
            bin_hash[ord(temp)] = 1
            mutableString[res_ind] = mutableString[ip_ind]
            res_ind += 1
        ip_ind += 1

    return toString(mutableString[0:res_ind])

# Driver program to test the above functions
string = "SSYYNNOOPPSSIISS"
print removeDups(string)
