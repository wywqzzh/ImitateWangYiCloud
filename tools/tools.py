def getJsonByPath(path):
    f = open(path, encoding='UTF-8')
    line = f.readline()
    line = line[:-1]
    x = ''
    c = {}
    while line:
        c.update({line[:11]: line[11:]})
        line = f.readline()
        line = line[:-1]
    return c
# print(getJsonByPath('../static/words/1403757375.txt'))
