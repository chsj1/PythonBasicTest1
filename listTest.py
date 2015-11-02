
#_*_ coding=utf-8 _*_

#列表的初始化
name_list = ['hjd','jdh','huangjundong']

#列表元素的访问
print name_list[1]

#追加元素
name_list.append('hhjjdd')
#插入元素.在索引为2的位置插入jingjing 这个值
name_list.insert(2,'jingjing')
#删除 内容为hjd的元素
name_list.remove('hjd')
#修改索引为1的元素额值
name_list[1]='helloworld'

name_list.append('jd')
name_list.append('jd')

#输出内容为 jd 的元素的个数
print name_list.count('jd')

#输出内容为 jd 的元素第一次出现的位置
print name_list.index('jd')

#借助 系统命令 来按索引进行删除
del name_list[0]

#将 list 翻转过来
name_list.reverse()

#排序
name_list.sort()

name_list1 = ['jingjing','xjj']

#将 name_list1 列表添加到 name_list中
name_list.extend(name_list1)

#获取 索引在[2,4) 之间的元素
print name_list[2:4]
#获取 最后5个元素
print name_list[-5:-0]

#同样能够实现以上功能
name_list += name_list1

#[1::2] 把索引为1+2n的元素取出来
print name_list[1::2]

#输出一个列表中某一元素的所有索引(1)
first_pos = 0
for i in range(name_list.count('xjj')):
	new_list = name_list[first_pos:]
	next_pos = new_list.index('xjj') + 1

	print 'find position: ' , first_pos + new_list.index('xjj')

	first_pos += next_pos

#输出一个列表中某一元素的所有索引(2)
first_pos = 0;
for i in range(name_list.count('xjj')):
	new_list = name_list[first_pos:]
	delta = new_list.index('xjj')+1

	first_pos += delta
	print 'position: ' , first_pos-1

#输出整个列表
print name_list