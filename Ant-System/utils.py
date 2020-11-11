def readDistFile(fileName):
    with open('instances' + '/' + fileName, 'r') as f:
        dist = [[int(num) for num in line.strip().split('  ')] for line in f]

    return dist

