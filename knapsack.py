def fun(alist,item):#returns True if 'item' is divisible by any element in 'alist'
	for y in alist:
		if item%y==0:
			return True
			break
	return False
def answer(alist,n):
	r=min(alist)
	temp = [0]
	for i in range(0,n+1):
		for j in range(0,len(temp)):
			x=i-temp[j]
			if fun(alist,x):
				temp.append(i)
				break
	return temp[-1]
T=input()
for j in range(T):
	size,n = map(int,raw_input().split())
	alist = map(int,raw_input().split())
	print answer(alist,n)