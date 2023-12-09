import re
total = 0

# # part 1
# # with open("input_sample.txt", "r") as f:
# with open("input.txt", "r") as f:

#     while True:
#         line = f.readline().replace("\n", "")
#         if not line:
#             break
#         print(line)
#         winning_numbers = [i for i in line.split("|")[0].split(":")[-1].split(" ") if i]
#         got_numbers = [i for i in line.split("|")[-1].split(" ") if i]

#         match = 0
#         for i in got_numbers:
#             if i in winning_numbers:
#                 match += 1
#         if match:
#             total += 1 * 2 ** (match - 1)

# print(total)


# part 2
all_cards_count = {}
all_cards_match = {}
card_id = 1
# with open("input_sample.txt", "r") as f:
with open("input.txt", "r") as f:

    while True:

        line = f.readline().replace("\n", "")
        if not line:
            break

        all_cards_count[card_id] = 1

        winning_numbers = [i for i in line.split("|")[0].split(":")[-1].split(" ") if i]
        got_numbers = [i for i in line.split("|")[-1].split(" ") if i]

        match = 0
        for i in got_numbers:
            if i in winning_numbers:
                match += 1
        all_cards_match[card_id] = match

        card_id += 1

print(all_cards_match)
print(all_cards_count)

for card_id in all_cards_count:
    if all_cards_match[card_id] == 0:
        continue
    else:
        for copy_idx in range(1, all_cards_match[card_id] + 1):
            increase = 1 * all_cards_count[card_id]
            all_cards_count[card_id+copy_idx] += increase

print(all_cards_count)

print(sum(all_cards_count.values()))
