import re

txt = 'The rain is cold 123'
x = re.search('^The', txt)


if x:
    print('Found')
else:
    print('Not found')

print(x)

pattern = re.compile('\d')
result = pattern.findall(txt)
print(len(result))
