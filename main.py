import json

with open('input.json', 'r') as f:
    input_dict = json.load(f)

print(input_dict['couriers'])