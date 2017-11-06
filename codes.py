# -*- coding: utf-8 -*-
# author:BerryHN
import codecs
s=u'岩'
print s
print type(s),s

u=s.encode("utf8").decode("utf8")
print u
print type(u)

u=u'汉'
print type(u)
print repr(u)
s=u.encode("utf8")
print repr(s)
u2=s.decode("utf-8")
print repr(u2)

import sys
import locale


print (sys.getdefaultencoding())
print (sys.getfilesystemencoding())
print (locale.getdefaultlocale())
print (locale.getpreferredencoding())



s1=u'人生苦短'
s2=unicode('人生苦短',"utf-8")
print type(s1)
print type(s2)



