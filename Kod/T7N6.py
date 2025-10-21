with open('input.txt', 'a+') as f:
    f.write('\nNew line')

with open ('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
