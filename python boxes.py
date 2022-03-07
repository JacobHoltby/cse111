import math
quantity = int(input('Enter the number of items: '))
limit = int(input('Enter the number of items per box: '))
calc = quantity / limit
answer = math.ceil(calc)
output = f'For {quantity} items, packing {limit} items in each box, you will need {answer} boxes.'
print()
print(output)
