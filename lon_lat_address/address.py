# -*- coding: utf-8 -*-
# author:BerryHN

class address(object):
    def __init__(self,province,city,district,**kw):
        self.province=province
        self.city=city
        self.district=district
        for k,v in kw.items():
            setattr(self,k,v)

    def  getProvince(self):
        return self.province
    def  getCity(self):
        return self.province
    def getDistrict(self):
        return self.district



