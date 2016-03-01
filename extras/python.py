m = {}

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


def rec(s,c):
        if isinstance(s,type("")):
                s = list(s)
        if(check(s,'x')):
                return 1.0
        elif(check(s,'o')):
                return -1.0
        r = ''.join(s)
        if r in m.keys():
                return m[r]

        x = 0.0
        fl = 0
        for i in range(9):
                if s[i] == '-':
                        s[i] = c;
                        if c == 'x':
                                x +=rec(s,'o')
                        else:
                                x+=rec(s,'x')
                        s[i]='-'
                        fl += 1

        if(fl==0):
                fl=1
        r = ''.join(s)
        m[r] = x/fl
        return x/fl


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
