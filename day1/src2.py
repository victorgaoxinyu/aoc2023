total_cal_value = 0

with open('input.txt', 'r') as f:

    while True:
        line = f.readline()

        if not line:
            break

        print(line)

        for i in len(line):
            