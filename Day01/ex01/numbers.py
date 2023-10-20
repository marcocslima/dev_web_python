def numbers():
    with open('numbers.txt', 'r') as numfile:
        content = numfile.read().split(',')
    for i in range(0, len(content)):
        print(content[i])

if __name__ == '__main__':
    numbers()