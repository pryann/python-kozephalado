lista = ["alma", "korte", "zsiraf", "akarat", "haz", "alaptetel"]
print([x for x in lista if x.startswith('a')])


product_list = {
    "alma" : 12,
    "korte" : 66,
    "barack" : 14,
    "ragogumi": 2
}
print([key for key, value in product_list.items() if value > 13])


new_list = []
for key, value in product_list.items():
    if value > 13:
      new_list.append(key)
print(new_list)

new_list = []
for key in product_list:
    if product_list[key] > 13:
      new_list.append(key)
print(new_list)