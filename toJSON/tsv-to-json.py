import sys
from jsonStarter import baseList as BL
if len(sys.argv) > 1:
    f = open(sys.argv[1],"rt")
else:
    f = ["time\t15\t2\t202\tห้องเรียนเทส"]
lis = BL()
for line in f:
    if "ประทับเวลา" in line:
        continue
    print(line)
    #15/10/2017, 1:29:04 15  2   203 ห้อง Lecture
    #[["1", "อาคารเรียนและบริหาร", "5", [{}, {}, {}, {}, {}]],
    line = line.split('\t')
    print(line)
    lis[int(line[1]) - 1 ][3][int(line[2]) - 1].append([line[3],line[4]])
#f.write(str(lis).replace('\"','\''))
realJSON = open("building-updated.json",'w')
realJSON.write("building = '"+str(lis).replace('\'','\"').replace('\\n','')+'\';')
realJSON.close()

