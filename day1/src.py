total_cal_value = 0

replace_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

enhanced_replace_map = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

with open('input.txt', 'r') as f:
# with open('input_sample.txt', 'r') as f:

    while True:
        line = f.readline()
        if not line:
            break
        print(line)

        for k, v in enhanced_replace_map.items():
            line = line.replace(k, v)

        print(line)
        for c in line:
            if c.isdigit():
                first_digit = c
                break
        
        for c in line[::-1]:
            if c.isdigit():
                last_digit = c
                break
        if first_digit and last_digit:
            value = first_digit + last_digit
        else:
            value = 0
        # print(value)

        total_cal_value += int(value)


print(total_cal_value)