# Program statement: Return maximum occurring character in the input string
# Write an efficient program to return maximum occurring character in the input string
# e.g., if input string is "test" then function should return 't'
# If more than one characters have the same count and that count is maximum
# then the function returns the first character with maximum count in input string.
# For example if input string is "test sample" then there are three characters with
# same and maximum count two i.e. "t", "e" and "s" but our program will result "t" because "t" comes first
# in input string. Similarly, the output for "cbbbbccc" would be "c".

# Time Complexity: O(n)
# Space Complexity: O(1) Because we are using fixed space (Hash array) irrespective of input string size.

ASCII_SIZE = 256


def getMaxOccuringChar(Str):
    # Create array to keep the count of individual characters
    # Initialize the count array to zero
    count = [0] * ASCII_SIZE
    maximum = -1
    c = ""
    for i in Str:
        count[ord(i)] += 1

    for i in Str:
        if maximum < count[ord(i)]:
            maximum = count[ord(i)]
            c = i
    return c, maximum

if __name__ == "__main__":
    ex_str = "maximumuu"
    print "Max occurring character is %s and which occurs %s times" % getMaxOccuringChar(ex_str)

    # Shorter version of the program
    print "******************* Shorter version of the program ***************************"
    import collections
    ex_str = "sample string"
    print "Max occurring character is " + collections.Counter(ex_str).most_common(1)[0][0] + " and which occures " + str(collections.Counter(ex_str).most_common(1)[0][1]) + " times"
