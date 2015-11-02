#_*_ coding:utf-8 _*_

#基本输入

#raw_input(): 会把所有的输入都当做是字符串来处理
name = raw_input('please input your name')
#age = raw_input('please input your age')
#input(): 原来的输入是什么类型就是什么类型
age = input('please input your age:')

job = raw_input('please input your job')
salary = raw_input('please input your salary')

#type(age): 输出age的类型
print type(age)

#基本输出
#print name , age
print '''
Personal information of %s:
			Name: %s
			Age: %s
			Job: %s
			Salary: %s
---------------------------
''' % (name,name,age,job,salary)