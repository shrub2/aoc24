
with open('input.txt', 'r') as file:
    input_text = file.read().strip().split("\n\n")
    
page_rules = input_text[0].strip().split("\n")
page_numbers = input_text[1].strip().split("\n")


page_rules_dict = {}
for page_rule in page_rules:
    key, value = page_rule.split("|")
    page_rules_dict.setdefault(key, []).append(value)

page_numbers_list = []
for line in page_numbers:
    page_numbers_list.append(line.split(","))

result = 0
for index, numbers in enumerate(page_numbers_list):
    valid_list = True
    i = 0
    n = len(numbers)
    while(i < n):
        try:
            rules = page_rules_dict[numbers[i]]
        except KeyError:
            rules = []
            i += 1
            continue
        numbers_before = numbers[:i]
        matched_numbers = set(rules) & set(numbers_before)
        if matched_numbers:
            valid_list = False
            for j, matched_number in enumerate(matched_numbers):
                numbers.remove(matched_number)
                numbers.insert(i+j, matched_number)
            i -= j
        i += 1
    if not valid_list:
        result += int(numbers[len(numbers) // 2])

print(result)
