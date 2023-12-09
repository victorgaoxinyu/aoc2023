import re


sum_of_game_id = 0

limit = {
    "red": 0,
    "blue": 0,
    "green": 0,
}


with open("input.txt", "r") as f:
# with open("input_sample.txt", "r") as f:

    while True:

        line = f.readline()
        if not line:
            break

        limit = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        
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
                    limit[color] = max(limit[color], int(number))
            
            # print(entry_result)     
        power = 1
        for k, v in limit.items():
            power = power * v  

        print(power)

        sum_of_game_id += power
print(sum_of_game_id)