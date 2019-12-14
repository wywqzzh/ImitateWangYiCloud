def getJsonByPath(path):
    f = open(path, encoding='UTF-8')
    line = f.readline()
    line = line[:-1]
    x = ''
    c = {}
    while line:
        x=0
        for i in range(2,len(line)):
            if(line[i]==']'):
                x=i
                break
        c.update({line[:x+1]: line[x+1:]})
        line = f.readline()
        line = line[:-1]
    return c

