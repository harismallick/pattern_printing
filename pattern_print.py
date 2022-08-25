## using the following video tutorial first: https://www.youtube.com/watch?v=k8SXsT5TLxQ&t=32s

# The pattern to print -
####
####
####
####

# When having to print the same thing repeatedly, the best course of action is to try putting it into a loop.
# Having multiple print statement to do the same thing is not optimised code.

# How to print the pattern shown above:

for i in range(4): # This is to loop for each line
    for j in range(4): # This is to loop for each hash in each line

        print('#', end='')

    print() # This will add a '\n' between each iteration of the nested for loop

print()
# The next pattern to print -
#
##
###
####

for i in range(5):
    hash_list = ['#']*i

    for h in hash_list:
        print(h, end='')

    print() # Add the '\n' separator between each nested for loop iteration

# Alternative solution - 

for i in range(4):
    for j in range(i+1):
        print('#', end='')

    print()

print()
# The next pattern to print - 
####
###
##
#

#print(sorted(range(4), reverse=True))
print()
for i in sorted(range(4), reverse=True):
    for j in range(i+1):
        print('#', end='')

    print()

n = 5
i = 0

while i <= n:
    for j in range(n-i):
        print('#', end='')
    i += 1
    print()


###############################

# Next video tutorial being followed: https://www.youtube.com/watch?v=lsOOs5J8ycw
# All the patterns can be found here: https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md 

# The general trick to outputting patterns and designs in the terminal is to use nested for loops.
# First thing to look at:
# The outer-most for loop should target the number of lines that you are going to have in your pattern.
# Divide your pattern into rows and columns.
# no. of lines = no. of rows (in pattern) = no. of iterations the outer for loops will have to run.

# Second thing to look at:
# How many columns are there for each row in your pattern?
# Look at the types of items that are in each column of each row.

# Third thing to look at:
# Item being printed in each line and column.
print()
# Print the following pattern-4:
#1
#12
#123
#1234
#12345

for i in range(5):
    for j in range(i+1):
        print(f'{1+j}', end='')
    print()
print()
# Print the following, pattern-5:
#*
#**
#***
#****
#*****
#****
#***
#**
#*

n = 1
for i in range(9): # Because there are 9 rows in this pattern

    if i < 5:
        for j in range(i+1):
            print('*', end='')
        print()

    else:
        for j in range(i-n):
            print('*', end='')
        print()
        n += 2


print()
# Pattern 6:
# 6.       *
#         **
#        ***
#       ****
#      *****

# There are 5 rows, so 5 iterations for the outer loop.
# There are 5 columns in each row made up of either spaces or '*'.
# In each successive iteration, a space is replaced by a column.

n = 5
for i in range(n+1):

    #for j in range(i):
    print(f'{" "*n}', end="")
    print(f'{"*"*i}', end="")

    print()
    n -= 1

print()
# Pattern 7
# 7.   *****
#       ****
#        ***
#         **
#          *

n = 5
m = 0
for i in range(n+1):
    print(f'{" "*m}{"*"*n}', end='')
    print()
    n -= 1
    m += 1

print()
# Pattern 8
# 8.      *
#        ***
#       *****
#      *******
#     *********

# Number of rows in this pattern: 5
# Number of columns in this patter: 9
# The pattern is to replace white space with '*' in each row to create a triangle.

col = 9
row = 5
counter_space = 0
counter_ast = 1
#print(col//2) # Need to use floor divide for this pattern

for i in range(row):
    print(f'{(col//2-counter_space)*" "}{(counter_ast)*"*"}{(col//2-counter_space)*" "}', end='')
    counter_space += 1
    counter_ast += 2
    print()

print()
# Pattern 9
# 9.  *********
#      *******
#       *****
#        ***
#         *

p9_col = 9
p9_row = 5
p9_space = 0
p9_asterisk = 9

for i in range(p9_row):
    print(f'{p9_space*" "}{p9_asterisk*"*"}{p9_space*" "}', end='')
    print()
    p9_space += 1
    p9_asterisk -= 2 

print()
# Pattern 10
# 10.      *
#         * *
#        * * *
#       * * * *
#      * * * * *

# This samples still contains 10 columns, based on the pattern monomer.
# The pattern is an asterisk with a space - '* '

p10_col = 10 # Including a column of white space at the end if the monomer for pattern is '* '
p10_row = 5
pattern_counter = 1
for i in range(p10_row):
    print(f'{(p10_row-pattern_counter)*" "}{pattern_counter*"* "}{(p10_row-pattern_counter)*" "}', end='')
    print()
    pattern_counter += 1
    #print()

print()
# Pattern 11
# 11.  * * * * *
#       * * * *
#        * * *
#         * *
#          *

p11_col = 10 # Including a column of white space at the end if the monomer for pattern is '* '
p11_row = 5
pattern_counter = 5
for i in range(p11_row):
    print(f'{(p11_row-pattern_counter)*" "}{pattern_counter*"* "}{(p11_row-pattern_counter)*" "}', end='')
    print()
    pattern_counter -= 1

print()
# Pattern 12
# 12.  * * * * *
#       * * * *
#        * * *
#         * *
#          *
#          *
#         * *
#        * * *
#       * * * *
#      * * * * *

# This pattern is a concatenation of the last two patterns we've done.

p12_col = 10
p12_row = 10
p12_counter = 5
for i in range(p12_row):
    if i < p12_row/2:
        print(f'{(int(p12_row/2)-p12_counter)*" "}{p12_counter*"* "}{(int(p12_row/2)-p12_counter)*" "}', end='')
        if p12_counter != 1:
            p12_counter -= 1

    else:
        print(f'{(int(p12_row/2)-p12_counter)*" "}{p12_counter*"* "}{(int(p12_row/2)-p12_counter)*" "}', end='')
        p12_counter += 1

    print()

