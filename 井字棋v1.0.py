#初始化
import random

aic=0 #ai的选择
plc=0 #玩家的选择
win=0 #胜利方
again=str("y")
aa=0;ab=0;ac=0;
ba=0;bb=0;bc=0;
ca=0;cb=0;cc=0;
aash=1;absh=2;acsh=3;
bash=4;bbsh=5;bcsh=6;
cash=7;cbsh=8;ccsh=9;
pl=1
plcc=0
list9 = ["1","2","3","4","5","6","7","8","9"]

#单人AI模块
def aichoose(aic): 
    print("testing")
    return

#玩家选择
def plchoose():
    global pl,plc,plcc,aa,ab,ac,ba,bb,bc,ca,cb,cc,aash,absh,acsh,bash,bbsh,bcsh,cash,cbsh,ccsh
    print("轮到玩家"+str(pl)+"的回合\n")

    #循环判断是否重复
    while plcc==0:
        plc=input("请选择1-9\n")
        if (plc in list9):
            plc=int(plc)
        else:
            print("输入错误")

        if plc==1 and aa==0:
            if pl==1:
                aash="⚪"
            elif pl==2:
                aash="×"
            aa=pl
            plcc=1
        elif plc==2 and ab==0:
            if pl==1:
                absh="⚪"
            elif pl==2:
                absh="×"
            ab=pl
            plcc=1
        elif plc==3 and ac==0:
            if pl==1:
                acsh="⚪"
            elif pl==2:
                acsh="×"
            ac=pl
            plcc=1
        elif plc==4 and ba==0:
            plcc=1
            if pl==1:
                bash="⚪"
            elif pl==2:
                bash="×"
            ba=pl
            plcc=1
        elif plc==5 and bb==0:
            if pl==1:
                bbsh="⚪"
            elif pl==2:
                bbsh="×"
            bb=pl
            plcc=1
        elif plc==6 and bc==0:
            if pl==1:
                bcsh="⚪"
            elif pl==2:
                bcsh="×"
            bc=pl
            plcc=1
        elif plc==7 and ca==0:
            if pl==1:
                cash="⚪"
            elif pl==2:
                cash="×"
            ca=pl
            plcc=1
        elif plc==8 and cb==0:
            if pl==1:
                cbsh="⚪"
            elif pl==2:
                cbsh="×"
            cb=pl
            plcc=1
        elif plc==9 and cc==0:
            if pl==1:
                ccsh="⚪"
            elif pl==2:
                ccsh="×"
            cc=pl
            plcc=1
    if pl == 1:
        pl=2
    else:
        pl=1
    return


#胜负判断
def winorlose():
    global aa,ab,ac,ba,bb,bc,ca,cb,cc,win,aash,absh,acsh,bash,bbsh,bcsh,cash,cbsh,ccsh
    if aa==ab and ab==ac:#h1
        if aa == 1:
            win=1
        elif aa==2:
            win=2
    elif ba==bb and bb==bc:#h2
        if ba == 1:
            win=1
        elif ba==2:
            win=2
    elif ca==cb and cb==cc:#h3
        if ca == 1:
            win=1
        elif ca==2:
            win=2
    elif aa==ba and ba==ca:#z1
        if aa == 1:
            win=1
        elif aa==2:
            win=2
    elif ab==bb and bb==cb:#z2
        if ab == 1:
            win=1
        elif ab==2:
            win=2
    elif ac==bc and bc==cc:#z3
        if ac == 1:
            win=1
        elif ac==2:
            win=2
    elif aa==bb and bb==cc:#ltr
        if aa == 1:
            win=1
        elif aa==2:
            win=2
    elif ac==bb and bb==ca:#rtl
        if ac == 1:
            win=1
        elif ac==2:
            win=2
    if win==1:
        print("玩家1获胜")
    elif win==2:
        print("玩家2获胜")
    if win==1 or win==2:
        print("- - - - - - -")
        print("| "+str(aash)+" | "+str(absh)+" | "+str(acsh)+" |")#第一行
        print("- - - - - - -")
        print("| "+str(bash)+" | "+str(bbsh)+" | "+str(bcsh)+" |")#第二行
        print("- - - - - - -")
        print("| "+str(cash)+" | "+str(cbsh)+" | "+str(ccsh)+" |")#第三行
        print("- - - - - - -")
    return
            



#展示棋盘
def showchecker():
    global aash,absh,acsh,bash,bbsh,bcsh,cash,cbsh,ccsh,shoose
    print("- - - - - - -")
    print("| "+str(aash)+" | "+str(absh)+" | "+str(acsh)+" |")#第一行
    print("- - - - - - -")
    print("| "+str(bash)+" | "+str(bbsh)+" | "+str(bcsh)+" |")#第二行
    print("- - - - - - -")
    print("| "+str(cash)+" | "+str(cbsh)+" | "+str(ccsh)+" |")#第三行
    print("- - - - - - -")

    #调试模式
    if choose=="3":
        print("- - - - - - -")
        print("| "+str(aa)+" | "+str(ab)+" | "+str(ac)+" |")#第一行
        print("- - - - - - -")
        print("| "+str(ba)+" | "+str(bb)+" | "+str(bc)+" |")#第二行
        print("- - - - - - -")
        print("| "+str(ca)+" | "+str(cb)+" | "+str(cc)+" |")#第三行
        print("- - - - - - -")
    return

print("B佬君的井字棋游戏\n\n\n")

while again=="y":
    aa=0;ab=0;ac=0;
    ba=0;bb=0;bc=0;
    ca=0;cb=0;cc=0;
    aash=1;absh=2;acsh=3;
    bash=4;bbsh=5;bcsh=6;
    cash=7;cbsh=8;ccsh=9;
    pl=1
    win=0
    print("单人游戏选1（维护中)")
    print("双人游戏选2\n")
    choose=input("请输入1或2\n")

    if choose == "1":
        #Simpleplayer Gaming
        print("单人模式还在设计中")
    else:
        #Doubleplayer Gaming
        print("双人模式还在测试中")
        while win == 0:
            showchecker()   #展示棋盘
            plchoose()      #玩家选择
            winorlose()     #胜负判断
            plcc=0

    #Restarting
    again = input("想要重来选y，退出选n\n")

    
#Ending
print("感谢您的游玩,按回车键可结束游戏")
input()
