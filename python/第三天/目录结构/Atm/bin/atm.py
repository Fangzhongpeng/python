
import os
import sys
print(__file__)
print(os.path.abspath(__file__))    #获取文件的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  #获取文件所在目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   #获取文件上上级目录

BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)    #动态添加系统环境变量

#import conf,core
from conf import setting
from core import main

main.login()