

def podminka(num):
    st = str(int (num))
    a1 = int(st[0])
    a2 = int(st[1])
    a3 = int(st[2])
    a4 = int(st[3])
    a5 = int(st[4])
    a6 = int(st[5])
    if(a1<=a2 and a2<=a3 and a3<=a4 and a4<=a5 and a5<=a6 and (a1==a2 or a2==a3 or a3==a4 or a4==a5 or a5==a6)):
        return 1
    return 0



sum =0
for i in range(145852,616942,1):
    sum+=podminka(i)

print(sum)

def podminka2(num):
    tmp =num
    lastval= tmp%10
    tmp= tmp//10
    same_count=0
    while tmp>0:
        val =tmp%10
        tmp=tmp//10
        if(val>lastval):
            return 0
        if(val==lastval):
            same_count+=1
        lastval=val
    if(same_count>0):
        return 1
    return 0

sum2 =0
for i in range(145852,616942,1):
    sum2+=podminka2(i)

print(sum2)
def podminka3(num):
    tmp =num
    lastval= tmp%10
    tmp= tmp//10
    same_count=[0,0,0,0,0,0,0,0,0,0,0,0]
    while tmp>0:
        val =tmp%10
        tmp=tmp//10
        if(val>lastval):
            return 0
        if(val==lastval):
            same_count[val]+=1
        lastval=val
    for a in same_count:
        if(a==1):
            return 1
    return 0
sum3 =0
for i in range(145852,616942,1):
    sum3+=podminka3(i)
print(sum3)