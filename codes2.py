
# -*- coding: utf-8 -*-
# author:BerryHN
ss='北京市'
print type(ss),ss
us=ss.decode("utf-8")
print repr(us)
print us,type(us)

nus=u'北京市'
print nus,type(nus)
gbks=nus.encode("gbk")
print repr(gbks)

print gbks,type(gbks)

utfs=nus.encode("utf-8")
print utfs,type(utfs)
print repr(utfs)

xx=utfs.decode("utf-8")
print xx,type(xx)
print repr(utfs)
