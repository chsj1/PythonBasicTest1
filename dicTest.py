#_*_ coding=utf-8 _*_
'''
介绍字典dict的使用
'''

#字典的初始化
name_info = {
#key-value的形式
	'name':'jacky',
	'age':'23',
	'job':'engineer'
}

#修改 或 增加一个key。如果已经存在'salary'的key
#那么将它修改为15000。如果不存在,增加一个名为'salary'的key
name_info['salary'] = '15000'

#删除key为 age 的键值对
name_info.pop('age')
#随便删一个 key-value 键值对
name_info.popitem()

#查询key为 salary 的键值对
print name_info['salary']

#字典的循环方式(1):效率高
for i in name_info:
	#前者是key,后者是value
	print i,name_info[i]

#字典的循环方式(2):效率低
for key,value in name_info.items():
	print key ,value



#------以上是CRUD的基本操作.一下介绍一些辅助操作
#get(key): 当key不存在的时候不会报错,而是返回一个None
print name_info.get('salaryy')

#has_key(key): 判断字典中key是否存在
print name_info.has_key('salaryy')

#keys(): 返回所有的key
print name_info.keys()

#values(): 返回所有的value
print name_info.values()

#setdefault(key,value): 如果key还不存在,新建该key,然后将其值设置成value
#如果已经存在，则不修改它的值.
name_info.setdefault('studentid',1234)
name_info.setdefault('studentid',1234)

#olddict.update(newdict): 将新字典更新到老字典中
#如果新字典中的一些key已经在老字典中已经存在,则更新他的value,
#否则将该key新加进去
new_name_info = {
	'addr' : 'shanghai',
	'salary' : '20000'
}

name_info.update(new_name_info)

#浅复制: 两个引用指向同一个内存空间
#这时候修改其中一个，另外一个也会变
info2 = name_info
info2['addr'] = 'beijing'

#深复制: 这时候这两个引用分别指向两个不同的内存空间
info3 = name_info.copy()
info3['addr'] = 'shenzhen'
print 'info3: ', info3
print 'name_info: ', name_info


#字典的输出
print name_info