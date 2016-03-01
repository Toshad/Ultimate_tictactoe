m = {}
class temp():
  def __init__(self,s,c):
    self.string = s
    self.chance = c

def temp(s,c):
        return s+c
    
def check(s,a):
        if isinstance(s,type("")):
                s = list(s)
        h = 0
        for i in range(9):
                if s[i] == a:
                        h += (1<<i)
        if (h&7) == 7:
                return 1
        if (h&56) == 56:
                return 1
        if (h&448) == 448:
                return 1
        if (h&292) == 292:
                return 1
        if (h&146) == 146:
                return 1
        if (h&73) == 73:
                return 1
        if (h&273) == 273:
                return 1
        if (h&84) == 84:
                return 1
        return 0


def dfs(s,c):
        global m
        if check(s,'x')==1:
                m[temp(s,c)] =  1.0
                return 1.0
        elif check(s,'o')==1:
                m[temp(s,c)]= -1.0
                return -1.0

        if temp(s,c) in m.keys():
                return m[temp(s,c)]

        if isinstance(s,type("")):
                s = list(s)
        x = -2.0
        y = 2.0 
        fl = 0
        for i in range(9):
                if s[i] == '-':
                        s[i] = c;
                        r = ''.join(s)
                        if c == 'x':
                                x =max(dfs(r,'o'),x)
                        else:
                                y = min(dfs(r,'x'),y)
                        s[i]='-'
                        fl += 1

        if(fl==0):
                fl=1
        r = ''.join(s)
        if c == 'x':
          m[temp(r,c)] = x/fl
          return x/fl
        else:
          m[temp(r,c)] = y/fl
          return y/fl


def start():
        global m
        s = "---------"
        m = {}
        dfs(s,'x')
        i = 0;
        print check("x-o-ooxxx",'x')
        print m["x-o-oox-xx"]
        i=0
        rrr = m.keys()
        rrr.sort()
        for k in rrr:
                i += 1
                print k,":",m[k]
        print i
