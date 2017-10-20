f = open("building-name.txt",'r')
lis = []
count = 1
for line in f:
    print(line)
    line = line.split(" (")
    lis.append([str(count),line[0],line[1].split()[1]])
    count += 1
print(lis)
