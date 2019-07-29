import random
a=0
b=0
c=0
d=0
t=1
p=0
choose=""
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
            while p==0:
                if d == 0:
                    print("第"+str(t)+"题\n"+str(a)+"+"+str(b))
                    choose=input("请输入得数")
                    if float(choose)== c:
                        print("回答正确")
                        p=1
                    else:
                        print("回答错误")
                else:
                    print("第"+str(t)+"题\n"+str(c)+"-"+str(a))
                    choose=input("请输入得数")
                    if float(choose)== b:
                        print("回答正确")
                        p=1
                    else:
                        print("回答错误")
            p=0
            t+=1
            print("\n\n\n")
    time=1
    inp=input("继续\n\n")
    
