import csv


# with open(file='data.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

fileds = []
rows = []
with open(file='data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        rows.append(row)
    print(f'Number of rows: {reader.line_num}')


for row in rows:
    for col in row:
        print('%15s' % col, end=' ')
    print('\n')
