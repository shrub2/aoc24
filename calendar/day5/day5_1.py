
with open('input.txt', 'r') as file:
    input_text = file.read().strip().split("\n\n")
    
page_rules = input_text[0].strip().split("\n")
page_numbers = input_text[1].strip().split("\n")


page_rules_dict = {}
for page_rule in page_rules:
    key, value = map(int, page_rule.split("|"))
    page_rules_dict.setdefault(key, []).append(value)

page_numbers_list = []
for line in page_numbers:
    page_numbers_list.append(list(map(int, line.split(","))))



