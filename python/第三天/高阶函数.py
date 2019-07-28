"""
高阶函数
    1，把一个函数名当做实参传给另外一个函数
    2, 返回值中包含函数名
"""
def bar():
    print ("in the bar")
def test1(func):     #将bar这个变量赋值给func这个变量
#    print(func)      #打印门牌号的地址
    func()           #门牌号+（）调用函数
test1(bar)           #将bar这个实参赋值给func这个形参

#总之一句话，函数名名的本质是指向一个内存地址，函数名+()就能运行