#这是个查找出第n位的质数
n=0
while n <= 0:
	n=input('请输入你想查询的第n个质数')
	n=int(n)
	if n>0:
		break
	else:
		print('错误，请输入一个自然数')
print('成功输入')


#设定初始值
j=[]
k=2		#k为除数
x=2		#x为待判定的数（逐渐递增）
m=0		#m为当前已经算到的第m的质数
o=0		#o为余数
if n<=3:
	if n==1:
		x=2
	if n==2:
		x=3
	if n==3:
		x=5
	q=True
else:
	q=False

while n!=m:				#当达到需求值时跳出循环
	if q:
		break

	while x>=k:			
		o=x%k
		#input()
		x=int(x)
		k=int(k)
		p=bool(x==k)	
		#print('o:',o,'x:',x,'k:',k,'m:',m,p)
		if o==0:
			if p:
				j.append(x)
				m=m+1
			break
		if x>=k:
			k=k+2
	if n==m:			#当符合目标时跳出
		break
	x=x+1
	k=3		


print('质数集合',j)
print('第',n,'个质数是：')
print(x)
