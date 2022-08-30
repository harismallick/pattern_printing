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

print()
# Pattern 13
# 13.      *
#         * *
#        *   *
#       *     *
#      *********

# Algorithm to print this pattern -- print spaces unless the index is (no. of columns)/2 +- counter.
# At the +- 1 counter positions, an '*' is printed. The counter increments by 1 at each interation of the for loop.

#print(int(9/2))
p13_col = 9
p13_row = 5
p13_counter = 0

for i in range(p13_row):
    if i == (p13_row-1):
        print(f'{"*"*p13_col}', end='')
        break

    for j in range(p13_col):
        if j == (int(p13_col/2)-p13_counter) or j == (int(p13_col/2)+p13_counter):
            print('*', end='')

        else:
            print(' ', end='')
    p13_counter += 1

    print()

print()

# Patter 14
# 14.  *********
#       *     *
#        *   *
#         * *
#          *

# This pattern is the previous one in reverse.

p14_col = 9
p14_row = 5
p14_counter = 3
middle = int(p14_col/2)
#print(middle)

for i in range(p14_row):
    if i == 0:
        print(f'{"*"*p14_col}', end='')
        print()
        continue

    for j in range(p14_col):
        if j == (middle-p14_counter) or j == (middle+p14_counter):
            print('*', end='')

        else:
            print(' ', end='')
    p14_counter -= 1

    print()

print()

# Pattern 15
# 15.      *
#         * *
#        *   *
#       *     *
#      *       *
#       *     *
#        *   *
#         * *
#          *

p15_col = 9 
p15_row = 9
p15_counter = 0
middle = int(p15_col/2)

for i in range(p15_row):
    for j in range(p15_col):
        if j == (middle-p15_counter) or j == (middle+p15_counter):
            print('*', end='')

        else:
            print(' ', end='')

    if i < middle:
        p15_counter += 1

    else:
        p15_counter -= 1

    print()


print()
# Pattern 16
# 16.           1
#             1   1
#           1   2   1
#         1   3   3   1
#       1   4   6   4   1

# This is the Pascal's triangle. Algorithm for getting the numbers:
# Find the number of rows you want to plot in the triangle.
# Number of columns in each row goes up by 1 each time.
# Pascal's rule: (n, k) = (n-1, k-1) + (n-1, k)
# Where n is the row index and k is the column index.

# Pattern 17
# 17.      1
#         212
#        32123
#       4321234
#        32123
#         212
#          1

# In this instace, lets define a variable n = 4
# No of rows for this pattern is 2n-1
# No of columns is also 2n-1
# The number to print before and after the central '1' determined by the variable n.

p17_n = 4
p17_rows = 2*p17_n - 1
p17_cols = 2*p17_n - 1
p17_middle = int((p17_cols+1)/2)
#print(p17_middle)
p17_counter = 1
p17_num_counter = 1


for i in range(p17_rows):
    temp = int((p17_num_counter+1)/2)

    print(f'{(p17_middle-p17_counter)*" "}', end='')
    #temp = int((p17_num_counter+1)/2)
    for num in range(p17_num_counter):
        
        print(temp, end='')
        if num >= int((p17_num_counter+1)/2)-1:
            temp += 1
        
        else:
            temp -= 1

    if i >= p17_n-1:
        p17_counter -= 1
        p17_num_counter -= 2

    else:
        p17_counter += 1
        p17_num_counter += 2

    print()

print()
# Pattern 28
# 28.      *
#         * *
#        * * *
#       * * * *
#      * * * * *
#       * * * *
#        * * *
#         * *
#          *

p28_col = 9
p28_row = 9
p28_middle = int(9/2)
p28_counter = 1

for i in range(p28_row):
    print(f'{(p28_middle-p28_counter+1)*" "}{p28_counter*"* "}', end='')

    if i < p28_middle:
        p28_counter += 1

    else:
        p28_counter -= 1

    print()

print()

