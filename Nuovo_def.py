def rot(t, sp=0):
    t = (' '*sp).join(list(t))
    tt = ' '*(len(t)-1) + t.upper()
    for i in range(0, len(tt), sp+1):
        print (tt[i:i+len(t)])
print (rot('python'))