# Chapter 5 - Loops and Iteration Quiz


# 1.
# What is wrong with this Python loop:

n = 5
while n > 0 :
    print(n)
print('All done')


# This loop will run forever.


# 2.
# What does the break statement do?


# Exits the currently executing loop


# 3.
# What does the continue statement do?


# Jumps to the "top" of the loop and starts the next iteration


# 4.
# What does the following Python program print out?

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)


# 5


# 5.
# What is the iteration variable in the following Python code:

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')


# friend


# 6.
# What is a good description of the following bit of Python code?

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)


# Sum all the elements of a list


# 7.
# What will the following code print out?

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)


# -1


# 8.
# What is a good statement to describe the is operator as used in the following if statement:

if smallest is None :
     smallest = value


# matches both type and value


# 9.
# Which reserved word indicates the start of an "indefinite" loop in Python?


# while


# 10.
# How many times will the body of the following loop be executed?

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')


# 0


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 5 - Loops and Iteration Assignments


# Assignment 5.2


largest = None
smallest = None

while True:

    num = input("Enter a number: ") # Enter 7, 2, bob, 10, 4 and done
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
