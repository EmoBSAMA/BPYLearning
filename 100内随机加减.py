import random
a=0
b=0
c=0
d=0
out="0"
inp="0"
time=1
while out=="0":
    while time < 5 :
        a = random.randint(1,99)
        b = random.randint(1,99)
        d = random.randint(0,1)
        c=a+b
        if c<200 and c>0:
            a=a/10
            b=b/10
            c=c/10
            time=time+1
            if d == 0:
                print(str(a)+"+"+str(b))
            else:
                print(str(c)+"-"+str(a))
    time=1
    inp=input("继续\n\n")
    
