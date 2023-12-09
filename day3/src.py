import re

symbol_list = ['-', '+', '=', '#', '$', '&', '/', '*', '%', '@']

# with open("input_sample.txt", "r") as f:
with open("input.txt", "r") as f:
# with open("input_redit.txt", "r") as f:


    lines = [i.replace("\n", "") for i in f.readlines()]

unique_c = {'.'}
for l in lines:
    unique_c = unique_c.union(set([i for i in l if not i.isdigit()]))
print(unique_c)

row_length = len(lines[0])
pad_rows = "." * (row_length+2)
padded_lines = ["." + i + "." for i in lines]
padded_lines.insert(0, pad_rows)
padded_lines.append(pad_rows)

for i in padded_lines:
    print(i)


def get_number_indices(s):
    result = []
    for match in re.finditer(r'\d+', s):
        number = int(match.group())
        start_idx = match.start()
        indices = list(range(start_idx, start_idx + len(match.group())))
        result.append((number, indices))
        # result[number] = indices
    return result

def adjacent_to_symbol(padded_lines, row, col):

    prev_c = padded_lines[row][col - 1]
    next_c = padded_lines[row][col + 1]
    above_c = padded_lines[row-1][col-1:col+2]
    below_c = padded_lines[row+1][col-1:col+2]

    adjacent_c = prev_c + next_c + above_c + below_c


    if any(sym in adjacent_c for sym in symbol_list):
        return True
    else:
        return False

def get_gear_ratio(padded_lines, row, col):

    def number_within_overlap_range(line, col):
        tmp = []
        overlap_range = range(col-1, col+2)
        number_idx = get_number_indices(line)
        for number_tuple in number_idx:
            if any(idx in overlap_range for idx in number_tuple[1]):
                tmp.append(number_tuple[0])
        
        return tmp

    adjacent_numbers = []
    # check above line
    above_line_adj_number = number_within_overlap_range(padded_lines[row - 1], col)
    current_line_adj_number = number_within_overlap_range(padded_lines[row], col)
    below_line_adj_number = number_within_overlap_range(padded_lines[row + 1], col) 

    print("Above: ", above_line_adj_number)
    print("Curr: ", current_line_adj_number)
    print("Below: ", below_line_adj_number)


    adjacent_numbers = above_line_adj_number + current_line_adj_number + below_line_adj_number

    if len(adjacent_numbers) == 2:
        print("Gear: ", adjacent_numbers)
        return adjacent_numbers[0] * adjacent_numbers[1]
    
    return 0
    
# part 2
gear_ratios = []

for row_idx in range(1, len(padded_lines) - 1):
    # get col_idx of '*'
    for match in re.finditer(r'\*', padded_lines[row_idx]):
        idx = match.start()
        print("<" * 20)
        print("Star: ", row_idx, idx)

        gear_ratios.append(get_gear_ratio(padded_lines, row_idx, idx))    

print(gear_ratios)
print(sum(gear_ratios))


# part 1
# numbers_adj_sym = []

# for row_idx in range(1, len(padded_lines)-1):
#     curr_line = padded_lines[row_idx]
#     print("<" * row_length)
#     print(padded_lines[row_idx-1])
#     print(curr_line)
#     print(padded_lines[row_idx+1])

#     result = get_number_indices(curr_line)
#     print(result)

#     if result:
#         for res in result:
#             k = res[0]
#             v = res[1]
#             print(k)
#             print(v)
#             for col_idx in v:
#                 if adjacent_to_symbol(padded_lines, row_idx, col_idx):
#                     numbers_adj_sym.append(k)
#                     print(k)
#                     break       
#             # break
#     # break

# print(numbers_adj_sym)
        
# print(sum(numbers_adj_sym))