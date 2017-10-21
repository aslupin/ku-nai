def printlis(l):
    for i in l:
        for j in i:
            print(j,end=' ')
        print()
def baseList():
    f = open("building-name.txt",'r')
    lis = []
    for line in f:
        if '#' in line:
            continue
        line = line.split()
        level = []
        for i in range(int(line[2])):
            level.append({})
        lis.append([line[0],line[1],line[2],level])
    #printlis(lis)
    f.close()
    return lis
    #f = open("building.json",'w')
    #f.write(str(lis).replace('\'','\"'))
    #f.close()
