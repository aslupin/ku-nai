of = open("tower.json",'r')
s = ""
for line in of:
    s = s + line
of.close()
nf = open("new-tower.json",'w')

tabcount = 0
for c in s:
    if c == ']':
        tabcount -= 1
    if c != '[':
        nf.write(c)
    else:
        tabcount += 1
        nf.write('\n'+'  '*tabcount+c)

