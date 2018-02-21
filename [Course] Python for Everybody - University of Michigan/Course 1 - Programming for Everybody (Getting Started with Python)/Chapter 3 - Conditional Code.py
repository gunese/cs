# Chapter 3 - Conditional Code Quiz


# 1.
# What do we do to a Python statement that is immediately after an if statement to
# indicate that the statement is to be executed only when the if statement is true?


# Indent the line below the if statement


# 2.
# Which of these operators is not a comparison / logical operator?


# =


# 3.
# What is true about the following code segment:

if x == 5:
   print('Is 5' )
   print('Is Still 5')
   print('Third 5')


# Depending on the value of x, either all three of the print statements will
# execute or none of the statements will execute


# 4.
# When you have multiple lines in an if block, how do you indicate the end of the if block?


# You de-indent the next line past the if block to the same level of indent as the original if statement


# 5.
# You look at the following text:

if x == 6 :
   print('Is 6')
   print('Is Still 6')
   print('Third 6')

# It looks perfect but Python is giving you an 'Indentation Error' on the second print
# statement. What is the most likely reason?


# You have mixed tabs and spaces in the file


# 6.
# What is the Python reserved word that we use in two-way if tests to indicate the block of
# code that is to be executed if the logical test is false?


# else


# 7.
# What will the following code print out?

x = 0
if x < 2 :
   print('Small')
elif x < 10 :
   print('Medium')
else :
   print('LARGE')
print('All done')


# Small
# All done


# 8.
# For the following code,

if x < 2 :
    print('Below 2')
elif x >= 2 :
    print('Two or more')
else :
    print('Something else')

# What value of 'x' will cause 'Something else' to print out?


# This code will never print 'Something else' regardless of the value for 'x'


# 9.
# In the following code (numbers added) - which will be the last line to execute
# successfully?

# (1)   astr = 'Hello Bob'
# (2)   istr = int(astr)
# (3)   print('First', istr)
# (4)   astr = '123'
# (5)   istr = int(astr)
# (6)   print('Second', istr)


# 1


# 10.
# For the following code:

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1

# What will the value be for istr after this code executes?


# -1


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 3 - Conditional Code Assignments


# Assignment 3.1


hrs = input("Enter Hours:")  # Enter 45
h = float(hrs)
rate = input("Enter Rate:")  # Enter 10.5
r = float(rate)
if h > 40:
    result = h * r
    a = (h - 40) * (r * 0.5)
    result = result + a
else:
    result = h * r

print(result)


# Assignment 3.3


try:
    score = float(input("Enter Score: "))
    if score == 0.9:
        print("A")
    elif score == 0.8:
        print("B")
    elif score == 0.7:
        print("C")
    elif score == 0.6:
        print("D")
    elif score < 0.6:
        print("F")
except:
    print("Error")
