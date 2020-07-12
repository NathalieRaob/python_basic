# 1- Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
    ##declare a function 
    ##for loop
    ##if number is positive, set it to "big"
    ##return same list 

def biggie_size(a_list):
    for i in range (len(a_list)):
        if a_list[i] > 0:
            a_list[i] = "Big"
    return a_list
print(biggie_size([2,3,-4,5,-8]))

# 2- Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
    ##declare a function 
    ##declare count variable 
    ##for loop 
    ##return the list 

def count_positives(lst):
    count = 0
    for i in range (len(lst)):
        if i > 0:
            count = count + 1 
    lst[len(lst)-1] = count
    return lst 

# 3- Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
    ##Declare a function
    ##declare a sum variable
    ##looping through the list 
    ##return the sum 

    def sum_total(mylist):
        sum = 0
        for i in mylist:
            sum += i 
        return sum
    print(sum_total([1,2,3]))
    

# 4- Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
    ##Declare a function
    ##declare a sum variable

    def average(mylist):
        sum = 0 
        for i in range(len(mylist)):
            sum = sum + mylist[i]
        return sum/len(mylist)
    print(average([1,2,3,4]))




# 5- Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
    ##declare a function
    ##for loop
    ##return lenght of the list 

def length(mylist):
    for i in range(len(mylist)):
        return len(mylist)
print(length([1,2,3,34,0]))



# 6- Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
    ##declare a function
    ##declare a min variable
    ##for loop
        ###if statement
    ##return 
def minimum(mylist):
    min = mylist[0]
    for i in mylist:
        if(i < min):
            min = i
    return min 
    if len(mylist) == 0:
        return False
print(minimum([1,3,5,-4,9,-8]))

    



# 7- Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
    ##declare a function
    ##declare a max variable
    ##fo loop 
        ###if statement
    ##return 
def maximum(mylist):
    max = mylist[0]
    for i in mylist:
        if(i > max):
            max = i
    return max 
    if len(mylist) == 0:
        return False 
print(maximum([37,2,1,-9]))




# 8- Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
    ##declare a function
    ##declare variables: sumtotal, minimum, maximum, and length of the list
    ##dictionary
       ##for loop 
    ##return dictionary 
def ultimate_analysis(mylist):
    max = mylist[0]
    min = mylist[0]
    sum = 0
    return_dico = {}
    for i in range(len(mylist)):
        if mylist[i] < min:
            min = mylist[i]
        if mylist[i] > max:
            max = mylist[i]
        sum = sum + mylist[i]
    average = sum/len(mylist)
    return_dico["max"] = max
    return_dico["min"] = min
    return_dico["average"] = average
    return_dico["length"] = len(mylist)
    return_dico["sum"] = sum 
    return return_dico

print(ultimate_analysis([37,2,1,-9]))    



# 9- Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
    ##declare a function, taking a list
    ##declare a temporary variable
    ##swap values
    ##return list with values swapped 

def reverse(mylist):
    temp = mylist[0]
    mylist[0] = mylist[len(mylist)-1]
    mylist[len(mylist)-1] = temp
    return mylist
print(reverse([2,34,48]))
