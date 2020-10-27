def binary_search(list,item):
    #low and high keep track of which part of the lilst you'll search in
    low = 0 
    high = len(list)-1

    while low <= high: 
        mid = (low + high) #check the middle element
        guess = list[mid]
        if guess == item: #found the item
            return mid 
        if guess > item: 
            high = mid-1 #the guess is too high
        else: 
            low = mid + 1 #the guess is too low
    return None #the item does not exist

    #test
    my_list = [1,3,5,7,9]

print binary_search(my_list, 3) 