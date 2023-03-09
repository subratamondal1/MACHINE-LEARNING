filename = '12.txt'
# write to file
with open(filename, 'w') as f:
    data = input('Enter data: ')
    f.write(data)
# read from file
with open(filename, 'r') as f:
    data = f.read()
    print('Data read from file:', data)