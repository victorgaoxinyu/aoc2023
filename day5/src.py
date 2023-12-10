import re
import yaml
seeds = []
from tqdm import tqdm

def get_raw_map(f):
    raw_map = []
    while True:
        next_line = f.readline()
        if not next_line or next_line == "\n":
            break
        raw_map.append([int(i) for i in next_line.replace("\n", "").split(" ")])
    
    print(raw_map)
    return raw_map

# def get_processed_map(raw_map):
#     processed_map = {}
#     for i in raw_map:
#         print("Parsing: ", i)
#         dst = i[0]
#         src = i[1]
#         lth = i[2]
#         for r in tqdm(range(lth)):
#             processed_map[src + r] = dst + r
#     return processed_map

def get_processed_map(raw_map):
    # [[src], [dst]]
    src_list = []
    dst_list = []
    for i in tqdm(raw_map):
        print("Parsing: ", i)
        dst = i[0]
        src = i[1]
        lth = i[2]
        src_list.extend(range(src, src + lth))
        dst_list.extend(range(dst, dst + lth))
    
    return [src_list, dst_list]
        

def save_dict(mapping, name):
    with open(f"{name}.yml", "w") as outfile:
        yaml.dump(mapping, outfile)

def get_value(key, mapping):
    return(mapping.get(key, key))

# with open("input_sample.txt") as f:
with open("input.txt") as f:

    while True:
        line = f.readline()
        if not line:
            break
        if "seeds: " in line:
            seeds = [int(i) for i in line.replace("\n", "").split(": ")[-1].split(" ")]
            continue
        
        if "map" in line:
            map_name = re.search(r"(.*?)\ map", line).group(1)
            match map_name:
                case "seed-to-soil":
                    print("converting seed-to-soil")
                    # raw_map = get_raw_map(f)
                    s2s_map = get_raw_map(f)
                    # s2s_map = get_processed_map(raw_map)

                case "soil-to-fertilizer":
                    print("Converting: soil-to-fertilizer")

                    s2f_map = get_raw_map(f)
                    # s2f_map = get_processed_map(get_raw_map(f))

                case "fertilizer-to-water":
                    print("Converting: fertilizer-to-water")
                    f2w_map = get_raw_map(f)
                    # f2w_map = get_processed_map(get_raw_map(f))

                case "water-to-light":
                    print("Converting: water-to-light")
                    w2l_map = get_raw_map(f)
                    # w2l_map = get_processed_map(get_raw_map(f))

                case "light-to-temperature":
                    print("Converting: light-to-temperature")
                    l2t_map = get_raw_map(f)
                    # l2t_map = get_processed_map(get_raw_map(f))

                case "temperature-to-humidity":
                    print("Converting: temperature-to-humidity")
                    t2h_map = get_raw_map(f)
                    # t2h_map = get_processed_map(get_raw_map(f))

                case "humidity-to-location":
                    print("Converting: humidity-to-location")
                    h2l_map = get_raw_map(f)
                    # h2l_map = get_processed_map(get_raw_map(f))
                case _:
                    print("something is wrong")

def get_value_from_lists(number, src_list, dst_list):
    if not number in src_list:
        return number
    else:
        index = src_list.index(number)
        return dst_list[index]

def get_value_from_raw_map(number, raw_map):
    for dst, src, lth in raw_map:
        if src <= number <= src + lth:
            return dst + (number - src)
        else:
            continue
    return number

locations = []
min_location = float('inf')
# part 2
updated_seeds = []
idx = 0

for idx in range(0, len(seeds), 2):
    start = seeds[idx]
    length = seeds[idx + 1]
    for s in tqdm(range(start, start + length)):
        soil = get_value_from_raw_map(s, s2s_map)
        fert = get_value_from_raw_map(soil, s2f_map)
        watr = get_value_from_raw_map(fert, f2w_map)
        ligt = get_value_from_raw_map(watr, w2l_map)
        temp = get_value_from_raw_map(ligt, l2t_map)
        humd = get_value_from_raw_map(temp, t2h_map)
        loc = get_value_from_raw_map(humd, h2l_map)

        if loc < min_location:
            min_location = loc
    idx += 2    

# for i in seeds:
#     soil = get_value_from_raw_map(i, s2s_map)
#     fert = get_value_from_raw_map(soil, s2f_map)
#     watr = get_value_from_raw_map(fert, f2w_map)
#     ligt = get_value_from_raw_map(watr, w2l_map)
#     temp = get_value_from_raw_map(ligt, l2t_map)
#     humd = get_value_from_raw_map(temp, t2h_map)
#     loc = get_value_from_raw_map(humd, h2l_map)

#     locations.append(loc)


print(min_location)