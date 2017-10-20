import sys
f = open(sys.argv[1],'r')
lis = []
count = 1
for line in f:
    print(line)
    line = line.split(" (")
    lis.append([str(count),line[0]])
    count += 1
print(lis)
