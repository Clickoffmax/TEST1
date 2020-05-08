# with open('text.txt') as file:
#     content = file.read()
#     print(content)

file_path = 'text.txt'


file = open(file_path)
content = file.readlines()
print(content)

for line in content:






file.close()


