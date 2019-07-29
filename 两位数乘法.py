import random
a=0
b=0
c=0
t=1
p=0
err=0
choose=""
out="0"
inp="0"

while out=="0":
    a = random.randint(1,99)
    b = random.randint(1,99)
    c=a*b
    while p==0:
        print("第"+str(t)+"题\n"+str(a)+"×"+str(b))
        choose=input("请输入得数")
        if str(choose)== str(c):
            print("回答正确")
            p=1
        else:
            print("回答错误")
            err+=1
    p=0
    t+=1
    print("\n\n\n")
    inp=input("你答错"+str(err)+"次，请按回车键继续\n\n")
    
