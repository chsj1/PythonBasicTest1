
#_*_ coding=utf-8 _*_
msg = 'hello world heLLo worLd'
print msg

#find():正向查找.索引从0开始
print 'position: %s' % msg.find('hello')
print 'position: %s' % msg.find('world')
#如果找不到返回-1
print 'position: %s' % msg.find('hjd')

#rfind():反向查找.返回的结果好像和正向查找差不多
print 'position: %s' % msg.rfind('hello')
print 'position: %s' % msg.rfind('world')

#index():返回所要寻找的字符串的位置.和find()大体相同,只是如果
#找不到会报错
print 'position: %s' % msg.index('world')
#print 'position: %s' % msg.index('hjd')

#capitalize(): 首字母大写,其他小写
print 'position: %s' % msg.capitalize()

#upper(): 全部大写
print 'position: %s' % msg.upper()

#lower(): 全部小写
print 'position: %s' % msg.lower()

#swapcase(): 大小写互换
print 'position: %s' % msg.swapcase()

#字符串msg分割之后就是一个列表list了
msg_list = msg.split(' ')
print msg_list

#join(list): 将字符串填充到list中
str =  '*'
str = str.join(msg_list)
print str

#cmp(str1,str2): 逐个比较两个字符串的大小.如果str1<str2,则返回-1
str1 = 'aB'
str2 = 'bA'
str3 = 'aB'
print cmp(str1,str2) 
print cmp(str1,str3)

#len(str): 获取字符串的长度
print len(msg)
print len(str1)

#max(str): 获取str中的最大字符
#min(str): 获取str中的最小字符
str = 'abcdcba'
print max(str)
print min(str)

#startswith(str): 是否以str开头
print msg.startswith('hello')
print msg.startswith('hjd')

#endswith(str): 时候以str结尾
print msg.endswith('Ld')
print msg.endswith('lD')