#_*_ coding:utf-8 _*_

count = input("please input loop numbeer")

while count >= 0:
    count -= 1

    if count == 8:
        continue
    print "%d" % count


    if count == 5:
     	#跳出循环
     	break
	 

print "end loop"  