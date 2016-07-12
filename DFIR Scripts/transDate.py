# -*- coding: utf-8 -*-
import time
import re

f = open('audit.log','r')
fout = open('auditHumanReadable.log','w')
lines = f.readlines()
f.close()
rex = re.compile(r'(?<=audit\()[0-9]*\.[0-9]*')
repls = {'old':'','new':''}				#测试lambda replace reduce(lambda a, kv: a.replace(*kv), repls.iteritems(), s)
for line in lines:
	rawtime = float(re.findall(rex,line)[0])
#	rawtime = re.findall(r'(?<=audit\()[0-9]*\.[0-9]*',line)
#	print rawtime
#	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(rawtime))
	out =  re.sub(rex,time.strftime("%Y-%m-%d/%H:%M:%S", time.localtime(rawtime)),line)
#	reduce(lambda a, kv : a.replace(*kv),repls,out)
	out_clean =  reduce(lambda k, kv : k.replace(*kv),repls.iteritems(),out)
	dataObj = re.split(r' ',out_clean)
	print dataObj
	fout.write(out_clean)
#	print line
fout.close()

