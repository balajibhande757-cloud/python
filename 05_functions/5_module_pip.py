# two types of module in python 
# 1) built in module
#  list of uilt in module https://docs.python.org/3/py-modindex.html
import math as m
import mymodule   # own created module
import requests   # external module 
print(m.sqrt(4))
mymodule.hello()
r=requests.get("https://docs.python.org/3/py-modindex.html")
print(r.text)

#EXTERNAL MODULE LIST # https://www.geeksforgeeks.org/python/external-modules-in-python/
