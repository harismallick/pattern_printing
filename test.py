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