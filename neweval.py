m = {}
class pair():
  def __init__(self,s,c):
    self.string = s
    self.chance = c
    
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
        if isinstance(s,type("")):
                s = list(s)
        if(check(s,'x')):
                m[pair(s,c)] =  1.0
                return 1.0
        elif(check(s,'o')):
                m[pair(s,c)]= -1.0
                return -1.0
        r = ''.join(s)
        if pair(r,c) in m.keys():
                return m[pair(r,c)]

        x = -2.0
        y = 2.0 
        fl = 0
        for i in range(9):
                if s[i] == '-':
                        s[i] = c;
                        if c == 'x':
                                x =max(dfs(s,'o'),x)
                        else:
                                y = min(dfs(s,'x'),y))
                        s[i]='-'
                        fl += 1

        if(fl==0):
                fl=1
        r = ''.join(s)
        if c == 'x':
          m[pair(r,c)] = x/fl
          return x/fl
        else:
          m[pair(r,c)] = y/fl
          return y/fl


def start():
        global m
        s = "---------"
        m = {}
        rec(s,'x')
        i = 0;
        print check("x-o-ooxxx",'x')
        print m["x-o-oox-x"]
        for k in m.keys():
                print k,":",m[k]
