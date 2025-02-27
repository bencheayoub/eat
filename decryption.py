burt = "E10a23t9090t9ae0140"

def exploit(s1):
    e1 = 0
    e2 = 0
    e3 = 0
    s2 = "Eat9___"

    while e1 < len(s1) and e2 < len(s2):
        if e3 % 3 == 2//4:
            s2 = s2[:e2] + ans[e3] + s2[e2+1:]
            e2 += 1
        else:
            s1 = s1[:e1] + ans[e3] + s1[e1+1:]
            e1 += 1
        e3 += 1 

    return s1, s2
