import time
"""
 装饰器
    定义 ： 本质势函数，用来装饰其他函数（为其他函数添加附加功能）
    原则：
        1，不能修改被装饰函数的源代码
        2，不能修改被装饰函数的调用方式
 实现装饰器的知识储备：
    1，函数即”变量“ :定义一个函数就是将函数体赋值给函数名，同样有变量的内存回收机制，就是没有使用del删除，就永远占用一个内存块，del删除的是门牌号（变量名）
       真正被删除是python定时删除的   下附录 python的内存回收机制
       
    2，高阶函数
    3，嵌套函数
    
    高阶函数+嵌套函数 ==》 装饰器
"""
def timer(func):                    #装饰器  time(test1)  func=test1

    def  deco(*args,**kwargs):       #此处加参数是为了应对原函数是否有参数以及参数格式个数不确定的情况 （必须）   #装饰器里边定义一个函数
        start_time = time.time()
        func(*args,**kwargs)               #在函数里边引用原函数  run test1   （这一步必须）
        stop_time = time.time()
        print("the func rim time is %s" %(stop_time-start_time))
    return deco                                                        #返回函数的内存地址  （这一步也必须）
@timer    #test1=timer(test1)=deco
def test1():
    time.sleep(3)
    print("in the test1")
@timer    #test1=timer(test1)=deco
def test2():
    time.sleep(3)
    print("in the test2")
@timer    #test3=timer(test3) = deco
def test3(name):             #被装饰的函数有参数的情况
    print("test3:",name)

test3("fang")

#实际上上执行的是deco(),而deco（）做了其他事情

# test1=deco(test1)
# test2=deco(test2)
#
# test1()
# test2()



