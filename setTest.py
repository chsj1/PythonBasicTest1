#_*_ coding=utf-8 _*_

#集合是天然就去重的
name_set = {
	1,2,3,4,5,5,4,3,2,1
}

#增加元素
name_set.add(6)

#删除元素: 从头开始删
name_set.pop()

#输出集合
print name_set

x = {
	1,2,3,4
}
y = {
	3,4,5,6
}
z = {
	3,4
}

#求 x与y 的交集
print x&y

#求 x与y 的并集
print x|y

#求只在 x中出现而不在y中出现 的元素
print x-y

#求只在 y中出现而不在x中出现 的元素
print y-x

#对称差集: 先求他们的合集,然后去掉他们之中都有的元素
print x^y

#判断z是否是y的子集
print z.issubset(y)
#判断z是否是y的父集
print z.issuperset(y)

