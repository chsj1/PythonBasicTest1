#_*_ coding=utf-8 _*_

'''
file('需要操作的文件','打开模式,默认是r')
strip('需要去除的字符')
split('分隔符')
'''
f = file('filetest.txt','a+b')

print "encoding: %s" % f.encoding

#readlines():读取多行
#readline():读取一行
for line in f.readlines():
	line = line.strip('\n').split(':')
	print line


f.write('hello python')

f.close()