#生成器示例
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。next()函数，迭代器
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b #yield关键字  python的返回值会输出
		n = n+1
		(a,b)=b,a+b
	return 'done'

for n in fib(6):
	print(n)

g=fib(10)
while True:
	try:
		print('g', next(g))
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
	

#杨辉三角generator生成器
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
#生成器精髓：知道f(n)，推算f(n+1),next()函数，yield函数
def yhTriangle(n):
	l, index = [1], 0
	while index < n:
		yield l
		l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
		index += 1



#=================================================================================
#协程学习 coroutine
#子程序通过栈来实现，一个入口，一个返回，调用顺序明确
#协程看起来像个子程序，在子程序中中断，去执行其他子程序，python中协程通过generator实现
#----Python的yield不但可以返回一个值，它还可以接收调用者发出的参数，使用协程实现“生产者-消费者”模型

def consumer():
	r=''
	while True:
		n = yield r #每次只执行一次
		if not n:
			return
		print('[consumer] consumering %s', n)
		r = '200 OK'

def produce(c):
	c.send(None)
	n=0
	while n<5:
		n=n+1
		print('[procuce] procucing %s', n)
		r = c.send(n) #主动调用协程去执行，并传入参数
		print('[procuce] consumering return %s', r)
	c.close()

c = consumer()
produce(c)
