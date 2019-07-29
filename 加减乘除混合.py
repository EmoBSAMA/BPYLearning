import random

'''
万以内加减       p1 a=0;b=0;c=得数;d=加减随机选择;e=对错判断
十位小数加减     p2 a=0;b=0;c=得数;d=加减随机选择;e=对错判断
两位数乘法       p3 a=0;b=0;c=得数;
百位除法，带余数 p4 a=0;b=0;c=得数;d=商;         ;e=对错判断
'''
a1=0;b1=0;c1=0;d1=0;e1=0
a2=0;b2=0;c2=0;d2=0;e2=0
a3=0;b3=0;c3=0;d3=0;e3=0
a4=0;b4=0;c4=0;d4=0;e4=0;choose_c='';choose_d=''

#答题次数
time_t=0
time_f=0

#模式选择
mode='exit'
mode_c=''
mode_list=['1','2','3','4','5']

#题型判断
tixing=0

#玩家输入
choose=""

def p1():#万以内加减法
    global a1,b1,c1,d1,e1,time_f,time_t
    time_t += 1
    e1=0
    d1=random.randint(1,2)
    b1=random.randint(1,9999)
    a1=random.randint(1,9999)
    c1=a1+b1
    while e1==0:
        print("第"+str(time_t)+"题")
        if d1 == 1:
            print(str(a1)+' + '+str(b1)+' = ?')
            choose=input('请回答')
            if choose == str(c1):
                print('回答正确,你成功完成了'+str(time_t)+'道题，但是你一共答错了'+str(time_f)+'道题。\n\n')
                e1=1
            else:
                time_f += 1
                print('回答错误，你一共答错'+str(time_f)+'道题\n\n')
        else:
            print(str(c1)+' - '+str(a1)+' = ?')
            choose=input('请回答')
            if choose == str(b1):
                print('回答正确,你成功完成了'+str(time_t)+'道题，但是你一共答错了'+str(time_f)+'道题。\n\n')
                e1=1
            else:
                time_f += 1
                print('回答错误，你一共答错'+str(time_f)+'道题\n\n')
    

def p2():#十位小数加减
    global a2,b2,c2,d2,e2,time_f,time_t
    time_t += 1
    e2=0
    d2=random.randint(1,2)
    b2=random.randint(1,100)
    a2=random.randint(1,100)
    a2=a2/10
    b2=b2/10
    c2=a2+b2
    while e2==0:
        print("第"+str(time_t)+"题")
        if d2 == 1:
            print(str(a2)+' + '+str(b2)+' = ?')
            choose=input('请回答')
            if choose == str(c2):
                print('回答正确,你成功完成了'+str(time_t)+'道题，但是你一共答错了'+str(time_f)+'道题。\n\n')
                e2=2
            else:
                time_f += 1
                print('回答错误，你一共答错'+str(time_f)+'道题\n\n')
        else:
            print(str(c2)+' - '+str(a2)+' = ?')
            choose=input('请回答')
            if choose == str(b2):
                print('回答正确,你成功完成了'+str(time_t)+'道题，但是你一共答错了'+str(time_f)+'道题。\n\n')
                e2=1
            else:
                time_f += 1
                print('回答错误，你一共答错'+str(time_f)+'道题\n\n')
    
def p3():#两位数乘法
    global a3,b3,c3,d3,e3,time_f,time_t
    time_t += 1
    a3 = random.randint(1,99)
    b3 = random.randint(1,99)
    c3=a3*b3
    e3=0
    while e3==0:
            print(str(a3)+' × '+str(b3)+' = ?')
            choose=input('请回答')
            if choose == str(c3):
                print('回答正确,你成功完成了'+str(time_t)+'道题，但是你一共答错了'+str(time_f)+'道题。\n\n')
                e3=2
            else:
                time_f += 1
                print('回答错误，你一共答错'+str(time_f)+'道题\n\n')

def p4():#百位除法，带余数
    global a4,b4,c4,d4,e4,time_f,time_t,choose_c,choose_d
    time_t += 1
    a4 = random.randint(1,99)
    b4 = random.randint(1,9)
    d4 = random.randint(0,b4-1)
    c4=a4*b4
    e4=0
    while e4==0:
            print(str(c4+d4)+' ÷ '+str(b4)+' = ? ······？')
            choose_c=input('请回答此题的商')
            choose_d=input('请回答此题的余数')
            if choose_c == str(a4) and choose_d == str(d4):
                print('回答正确,你成功完成了'+str(time_t)+'道题，但是你一共答错了'+str(time_f)+'道题。\n\n')
                e4=2
            else:
                time_f += 1
                print('回答错误，你一共答错'+str(time_f)+'道题\n\n')

#开始界面
print('欢迎来到小学加减乘除数学题检测\n')
print('请选择模式')
print('1.万以内加减法')
print('2.十位小数加减法')
print('3.两位数乘法')
print('4.百位除法，带余数')
print('5.上述混合'+'\n')
while not mode in mode_list:
    mode=input()
    if not mode in mode_list:
        print('输入错误，请重新输入')

while ((mode in mode_list) or (mode == 'exit')) and (mode_c!='exit'):
    if mode == '1':
        p1()
        
    if mode == '2':
        p2()
    if mode == '3':
        p3()
    if mode == '4':
        p4()
    if mode == '5':
        while (not mode =='exit') and (mode_c!='exit'):
            tixing= random.randint(1,4)
            if tixing == 1:
                p1()
            elif tixing == 2:
                p2()
            elif tixing == 3:
                p3()
            elif tixing == 4:
                p4()
    mode_c=input('继续请按回车键，结束请输入exit')
    








