# For_Loops_Basic1_
for i in range(0, 151):
    print(i)

### Multiples of 5
for i in range(0, 1000, 5):
    print(i)

#Counting the Dojo Way
for i in range(0, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Add odd integers from 0 to 500,000, and print the final sum
sum = 0

for i in range(1,500001,2):
    print(i)
    sum += i
print(sum)

# Print positive numbers starting at 2018, counting down by fours.

for i in range(2018,0,-4):
    print(i)


###
## Set three variables: lowNum, highNum, mult. 
## Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
## For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
###
lowNum = 2
highNum = 9 
mult = 3

for i in range(lowNum,highNum + 1):
    if i % mult == 0:
        print(i)
