import random

s=0
l=100
number = random.randint(s,l)
time = int(1)
temp = input("猜猜数字（范围" + str(s) +"-" + str(l) +")\n")
guess = int(temp)
while guess !=number:
        if guess > number:
                print("猜错了,有点大")
                if l>guess :
                        l=guess
        else:
                print("猜错了,有点小")
                if s<guess :
                        s=guess
        temp = input("猜猜数字（范围" + str(s) +"-" + str(l) +")\n")
        guess = int(temp)
        time = time+1
print("猜对了,答案就是：" + str(number) + "。你一共猜了" + str(time)+ "次就能猜中")
p=('按任意键就能结束')

