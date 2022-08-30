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
