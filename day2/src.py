import re


sum_of_game_id = 0

limit = {
    "red": 12,
    "blue": 14,
    "green": 13,
}


# with open("input.txt", "r") as f:
with open("input_sample.txt", "r") as f:

    while True:

        line = f.readline()
        if not line:
            break
        
        possible = True
        game_id = re.search(r'Game\ (.*?)\:', line).group(1)

        content = line.split(":")[-1]
        for entry in content.split(";"):
            entry_result = {}
            for s in entry.split(","):
                pattern = r"\s(\d+)\s(\w+)"
                match = re.search(pattern, s)
                if match:
                    color = match.group(2)
                    number = match.group(1)
                    if int(number) > limit[color]:
                        possible = False
            
            # print(entry_result)     

        if possible:
            sum_of_game_id += int(game_id)     


print(sum_of_game_id)