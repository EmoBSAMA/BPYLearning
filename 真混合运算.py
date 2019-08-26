'''
功能介绍：
提供一个自动化出题程序
主要考察的是连续运算以及混合运算的正确性

模式一：大整数连续加减
模式二：一位小数连续加减
模式三：二十以内整数数连续乘法
模式四：混合模式
'''
import random

#运算部分
que_list_1=[0,0,0,0,0,0]
que_list_2=[0,0,0,0,0,0]
que_list_3=[0,0,0,0,0,0]

ans_t1=0        #正确答案
ans_t2=0

ans_1=''        #一般答案
ans_2=''        #额外答案（如商）
qus_long=1      #混合次数(0-5)
que_tf=False

#答题次数
time_t=0
time_f=0

#模式选择
mode=''
mode_c=''
mode_list=['1','2','3','4','exit','test1','test2','test3','test4']
dif=''

#题型判断
tixing=0

#玩家输入
choose=""

'''
0为加，1为减
'''
def clean():
    global que_list_1,que_list_2,que_list_3,ans_1,ans_2,que_long,que_tf,ans_t1,ans_t2
    que_list_1=[0,0,0,0,0,0]
    que_list_2=[0,0,0,0,0,0]
    que_list_3=[0,0,0,0,0,0]
    ans_1=0;ans_2=0;qus_long=1;que_tf=False
    ans_t1=0;ans_t2=0

def ans_pd():
    global que_tf
    if que_tf == True:
        print('回答正确,你成功完成了'+str(time_t)+
          '道题，但是你一共答错了'+str(time_f)+
          '道题。\n\n')
    elif que_tf == False:
        print('回答错误，你一共答错'+str(time_f)+'道题\n\n')

    

def mode_1_ran():#大整数连续加减_加数随机_加减随机
    global que_long,que_list_1,que_list_2,ans_t1
    que_long = random.randint(2,6)#1-5
    for i in range(0,que_long):
        que_list_1[i]=random.randint(1,1000)
    for i in range(0,que_long-1):
        que_list_2[i]=random.randint(0,1)
    #计算题目得数

    ans_t1 = que_list_1[0]
    
    for i in range(0,que_long-1):
        if que_list_2[i] == 0:
            ans_t1 += que_list_1[i+1]
        else:
            ans_t1 -= que_list_1[i+1]
    if mode[0:4] == 'test':
        print('正确答案：' + str(ans_t1))
    
#打印题目（没问题）
def mode_1_print():
    global que_long,que_list_1,que_list_2

    if mode[0:4] == 'test':
        print(str(que_long))
        print(str(que_list_1))
        print(str(que_list_2))
    

    print("\n第"+str(time_t)+"题")
    #两数加减
    if que_long == 0:
        if que_list_2[0] == 0:
            print(str(que_list_1[0]) + ' + ' + str(que_list_1[1]) + " = ?")
        else:
            print(str(que_list_1[0]) + ' - ' + str(que_list_1[1]) + " = ?")
    else:
        for i in range(0,que_long):
            if i == 0:
                print(str(que_list_1[i]),sep='',end='')
            if i == que_long - 1:
                break
            if que_list_2[i] == 0:
                print(' + ',sep='',end='')
            else:
                print(' - ',sep='',end='')
            print(str(que_list_1[i+1]),sep='',end='')
        print(" = ?",sep='')

def mode_2_ran():
    global que_long,que_list_1,que_list_2,ans_t1
    que_long = random.randint(2,6)#1-5
    for i in range(0,que_long):
        que_list_1[i]=random.randint(1,100)
    for i in range(0,que_long-1):
        que_list_2[i]=random.randint(0,1)
    #计算题目得数

    ans_t1 = que_list_1[0]
    
    for i in range(0,que_long-1):
        if que_list_2[i] == 0:
            ans_t1 += que_list_1[i+1]
        else:
            ans_t1 -= que_list_1[i+1]
    ans_t1 /= 10
    ans_t1= round(ans_t1,1)
    for i in range(0,que_long):
        que_list_1[i] /= 10
        que_list_1[i] = round(que_list_1[i],1)
    if mode[0:4] == 'test':
        print('正确答案：' + str(ans_t1))
 
def mode_3_ran():#二十以内整数数连续乘法
    global que_long,que_list_1,que_list_2,ans_t1
    que_long = random.randint(2,6)
    for i in range(0,que_long):
        que_list_1[i]=random.randint(1,21)
    #计算题目得数
    ans_t1 = 0
    ans_t1 = que_list_1[0]
    
    for i in range(0,que_long):
        if i == 0:
            ans_t1 = que_list_1[i]
        elif i != 0:
            ans_t1 *= que_list_1[i]
    if mode[0:4] == 'test':
        print('正确答案：' + str(ans_t1))
    

def mode_3_print():
    global que_long,que_list_1,que_list_2

    if mode[0:4] == 'test':
        print(str(que_long))
        print(str(que_list_1))
    
    print("\n第"+str(time_t)+"题")
    #两数相乘
    if que_long == 0:
        print(str(que_list_1[0]) + ' × ' + str(que_list_1[1]) + " = ?")
    else:
        for i in range(0,que_long):
            if i == 0:
                print(str(que_list_1[i]),sep='',end='')
            if i == que_long - 1:
                break
            print(' × ',sep='',end='')
            print(str(que_list_1[i+1]),sep='',end='')
        print(" = ?",sep='')
    

def mode_ans():#玩家回答
    global ans_1,ans_2,mode,tixing

    if mode == '1' or mode == '2' or mode == 'test1' or mode == 'test2':
        ans_1=input('请输入此题得数:')
    elif mode == '3' or mode == 'test3':
        ans_1=input('请输入此题的积：')
    elif mode == '4' or mode == 'test4':
        if tixing == 1 or tixing == 2:
            ans_1=input('请输入此题得数:')
        if tixing == 3:
            ans_1=input('请输入此题的积：')

def mode_1():#大整数连续加减
    global que_list_1,que_list_2,ans_a,ans_2,que_long,que_tf,time_t,time_f,choose
    clean()
    time_t += 1

    #生成题目  
    mode_1_ran()
    
    #打印题目
    mode_1_print()

    #回答问题
    mode_ans()

    #答案判断
    while que_tf ==False:
        if ans_1 != str(ans_t1):
            que_tf=False
            time_f += 1
            ans_pd()
            mode_1_print()
            mode_ans()
        else:
            que_tf=True
            ans_pd()
    
    
def mode_2():#一位小数连续加减
    global que_list_1,que_list_2,ans_a,ans_2,que_long,que_tf,time_t,time_f,choose
    clean()
    time_t += 1

    #生成题目  
    mode_2_ran()
    
    #打印题目
    mode_1_print()

    #回答问题
    mode_ans()

    #答案判断
    while que_tf ==False:
        if ans_1 != str(ans_t1):
            que_tf=False
            time_f += 1
            ans_pd()
            mode_2_print()
            mode_ans()
        else:
            que_tf=True
            ans_pd()
    
def mode_3():#两位数乘法
    global que_list_1,que_list_2,ans_a,ans_2,que_long,que_tf,time_t,time_f,choose
    clean()
    time_t += 1

    #生成题目  
    mode_3_ran()
    
    #打印题目
    mode_3_print()

    #回答问题
    mode_ans()

    #答案判断
    while que_tf ==False:
        if ans_1 != str(ans_t1):
            que_tf=False
            time_f += 1
            ans_pd()
            mode_3_print()
            mode_ans()
        else:
            que_tf=True
            ans_pd()

    


#开始界面
print('欢迎来到小学加减乘除数学题检测加强版\n')
print('请选择模式')
print('1.大整数连续加减')
print('2.一位小数连续加减')
print('3.二十以内整数数连续乘法')
print('4.混合模式'+'\n')
while not mode in mode_list:
    mode=input()
    if not mode in mode_list:
        print('输入错误，请重新输入')

while (mode in mode_list) and (mode_c!='exit'):
    clean()
    if mode == '1' or mode == 'test1' :
        mode_1()
    elif mode == '2' or mode == 'test2':
        mode_2()
    elif mode == '3' or mode == 'test3':
        mode_3()
    elif mode == '4' or mode == 'test4':
        while (not mode =='exit') and (mode_c!='exit'):
            tixing= random.randint(1,3)
            if tixing == 1:
                mode_1()
            elif tixing == 2:
                mode_2()
            elif tixing == 3:
                mode_3()
    mode_c=input('继续请按回车键，结束请输入exit')
