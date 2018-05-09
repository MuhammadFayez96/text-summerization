stock = {
    'a': 120,
    'b': 123,
    'x': 121
}
sorted_dict = sorted(zip(stock.values(), stock.keys()))

new_dict = {}

for i in range(2):
    new_dict.update({sorted_dict[(len(sorted_dict) - 1) - i][1]: sorted_dict[(len(sorted_dict) - 1) - i][0]})
    print(sorted_dict[(len(sorted_dict) - 1) - i])
print(new_dict)

n = 100
p = 10
print(int((p/100) * n))