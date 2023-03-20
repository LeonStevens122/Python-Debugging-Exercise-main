# Implementation of the Quicksort algorithm

# I dont know why this took e so long, but the problem is in the partition function.
# The condition for the while loop in the second loop is incorrect.
# It should check that rightmark is greater than or equal to leftmark,
# and only then should it check that numbers[rightmark] >= pivotvalue.
# So you need to swap these two conditions in the second loop:

# Also, the if condition for checking if the while loop is done should be
# rightmark < leftmark, not rightmark < leftmark - 1:
# Whcih is what caused the infinite loop in my first correction of the code.

# This was an interesting challenge and forced me to actually pay attention and understand the Quicksort
# in a way that I havent done before, I tend to be in the "If it aint broke dont fix it" team when it comes to
# things like sorting. This challenge changed my mind


def quick_sort(numbers):
    # The functions takes a list of numbers and calls a helper function
    quick_sort_helper(numbers, 0, len(numbers)-1)


def quick_sort_helper(numbers, first, last):
    # this helper function takes a list of numbers and the first and last index of the subArray,
    # The function sorts the subarray by recursively partitioning it and sorting the left and right subarrays.

    if first < last:

        splitpoint = partition(numbers, first, last)
        quick_sort_helper(numbers, first, splitpoint-1)
        quick_sort_helper(numbers, splitpoint+1, last)


def partition(numbers, first, last):
    # This function takes a list of numbers, the first & last index of the subarray to be partitioned,
    # It selects the first element as the pivot value and partitions the array into two subarrays:
    # one with values less than or equal to the pivot, and one with values greater than the pivot.
    pivotvalue = numbers[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and numbers[leftmark] <= pivotvalue:
            # This loop moves the leftmark to the right until it finds an element
            # that is greater than the pivot value.
            leftmark = leftmark + 1
            print("Leftmark in first loop: " + str(leftmark),
                  "Rightmark : "+str(rightmark))

        while rightmark >= leftmark and numbers[rightmark] >= pivotvalue:
            # This loop moves the rightmark to the left until it finds an element that
            # is less than the pivot value.
            rightmark = rightmark - 1
            print("rightmark in second loop: " + str(rightmark),
                  "Leftmark: " + str(leftmark))

        if rightmark < leftmark:
            # If the rightmark is to the left of the leftmark, exit the while loop
            done = True
        else:
            # Otherwise, we swap the left and right elements to ensure that the left subarray has values less than or equal to the pivot, and the right subarray has values greater than the pivot.
            temp = numbers[leftmark]
            numbers[leftmark] = numbers[rightmark]
            numbers[rightmark] = temp

    # Finally, we swap the pivot value with the rightmark, which is the last element of the left subarray and the first element of the right subarray.
    temp = numbers[first]
    numbers[first] = numbers[rightmark]
    numbers[rightmark] = temp

    # Return the rightmark index so that we can partition the left and right subarrays recursively.
    return rightmark


numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before Sort: {}".format(numbers))
quick_sort(numbers)
print("After Sort: {}".format(numbers))
