
import sys,os

if len(sys.argv) <= 4:
	print 'usage: '
   
old_text,new_text = sys.argv[1],sys.argv[2]

file_name = sys.argv[3]

print 'file_name',file_name

f = file(file_name,'rb')
new_file = file('.%s.bak' % file_name,'w')

for line in f.xreadlines():
	new_file.write(line.replace(old_text,new_text))

f.close()
new_file.close()

if '--bak' in sys.argv:
	os.rename(file_name,'%s.bak' % file_name)
	os.rename('.%s.bak' % file_name ,file_name)
else:
	os.rename('.%s.bak' %file_name ,file_name)
	
