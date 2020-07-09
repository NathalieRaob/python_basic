# 1 Basic- Print all integers from 0 to 150 

for integers in range(0,151):
    print(integers)

# 2 Multiples of Five- Print all the multiples of 5 from 5 to 1,000

for multiples in range(5,1005,5):
    print(multiples)

# 3 Counting, the Dojo Way- Print integers 1 to 100. if divisible by 5, print "Coding" instead. if divisible by 10, print "Coding Dojo".

for num in range(1,100):
    if num%5==0:
        print("Coding")
    elif num%10==0:
        print("Coding Dojo")
    else:
        print(num)

# 4 Whoa. That Sucker's Huge- Add odd integers from 0 to 500,000, and print the final sum
total = 0
for integers in range(0,500000,2):
    total += integers
    print(total)


# 5 Countdown by fours- Print positive numbers starting at 2018, counting down by fours

count = 2018
while count > 0:
    print(count)
    count -= 4

# 6 Flexible counter- Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
lowNum = 2
highNum = 9
mult = 3
for num in range(2,9):
    if num%mult == 0:
        print(num)  #This was my first answer 

    

def Flexcounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum +1):
        if i%mult == 0:
            print(i)

Flexcounter(2,9,3) #This was my answer after checking the solution 


