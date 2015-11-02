#_*_ coding:utf-8 _*_

'''
用于演示if else语句
'''

#age = raw_input('please input your age')
#在这里千万不要使用input()函数
age = input('please input your age')

if age > 40:
	msg = 'you are too old'
elif age > 30:
	msg = 'hello 30 boys'
else:
	msg = 'good studey day day up'

print msg