
"""

高阶函数
    a:把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
    b:返回值中包含函数名（不修改函数的调用方式）


import time
"""
def bar():
    time.sleep(3)
    print('in the bar')
def test1(func):
    print(func)     # 便于理解，新功能1
    print("新加功能")   #新功能2
    return func   # 返回值中包含函数名

bar=test1(bar)   # 将新函数的返回值赋值给bar,新函数的返回值是一个func的地址（函数名），使得bar拥有新功能，

#print(bar)
bar()     # 结果是没修改bar函数调用方式的情况下为bar个函数添加了功能