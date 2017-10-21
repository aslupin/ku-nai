import jsonStarter as jser
def formatted(s,t):
    t += 1
#    print(s)
    if '[' in s:
        return s
    return s[0:s.index('[')] + '\n' + '\t'*t + formatted(s[s.index('['),len(s)])
print(formatted(str(jser.baseList()),0))
