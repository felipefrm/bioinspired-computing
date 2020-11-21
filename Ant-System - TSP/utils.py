def readDistFile(fileName):
    try:
        with open('instances' + '/' + fileName, 'r') as f:
            dist = []
            for line in f:
                line = ' '.join(line.split())
                line = line.split(' ')
                line = [ int(x) for x in line ]
                dist.append(line)
            return dist
    except IOError:
        exit('File not found.')
