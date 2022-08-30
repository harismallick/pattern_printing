# Pattern 16
# 16.           1
#             1   1
#           1   2   1
#         1   3   3   1
#       1   4   6   4   1
# 1
# 11
# 121
# 1331
# 14641

# This is the Pascal's triangle. Algorithm for getting the numbers:
# Find the number of rows you want to plot in the triangle.
# Number of columns in each row goes up by 1 each time.
# Pascal's rule: (n, k) = (n-1, k-1) + (n-1, k)
# Where n is the row index and k is the column index.

p16_n = 5

pascal_arr = [[1],[1,1]]

for i in range(2, p16_n):
    temp_list = [1]
    for j in range(1, i):
        
        num = pascal_arr[i-1][j] + pascal_arr[i-1][j-1]
        #print(num)
        temp_list.append(num)

    temp_list.append(1)
    pascal_arr.append(temp_list)

print(pascal_arr)

counter = 1

for arr in pascal_arr:
    print(f'{(p16_n-counter)*" "}', end='')

    for item in arr:
        print(f'{item} ', end='')
    counter += 1

    print()
    

