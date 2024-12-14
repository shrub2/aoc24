
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
for numbers in page_numbers_list:
    valid_list = True
    for index, number in enumerate(numbers):
        try:
            rules = page_rules_dict[number]
        except KeyError:
            rules = []
            continue
        numbers_before = numbers[:index]
        if set(rules) & set(numbers_before):
            valid_list = False
            break
    if valid_list:
        result += int(numbers[len(numbers) // 2])

print(result)
