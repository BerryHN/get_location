# -*- coding: utf-8 -*-
# author:BerryHN
import re
pattern = re.compile(
    r"((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))")
def is_ip(ip):
    ip_a=pattern.findall(ip)
    if ip_a:
        return ip_a[0][0]

    else:
         return ""

