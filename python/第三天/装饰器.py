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

def test1():
    time.sleep(3)
    print("in the test1")
test1()

"""
匿名函数与lambda
 
    lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。

    lambda所表示的匿名函数的内容应该是很简单的，如果复杂的话，干脆就重新定义一个函数了，使用lambda就有点过于执拗了。

    lambda就是用来定义一个匿名函数的，如果还要给他绑定一个名字的话，就会显得有点画蛇添足，通常是直接使用lambda函数。如下所示：

    add = lambda x, y : x+y
    add(1,2)  # 结果为3
 

    那么到底要如何使用lambda表达式呢？

 

        1、应用在函数式编程中

        Python提供了很多函数式编程的特性，如：map、reduce、filter、sorted等这些函数都支持函数作为参数，lambda函数就可以应用在函数式编程中。如下：

        # 需求：将列表中的元素按照绝对值大小进行升序排列
        list = [3,5,-4,-1,0,-2,-6]
        sorted(list1, key=lambda x: abs(x))
        当然，也可以如下：

        list1 = [3,5,-4,-1,0,-2,-6]
        def get_abs(x):
            return abs(x)
        sorted(list1,key=get_abs)
        只不过这种方式的代码看起来不够Pythonic

 

2、应用在闭包中

def get_y(a,b):
     return lambda x:ax+b
y1 = get_y(1,1)
y1(1) # 结果为2
当然，也可以用常规函数实现闭包，如下：

def get_y(a,b):
    def func(x):
        return ax+b
    return func
y1 = get_y(1,1)
y1(1) # 结果为2
只不过这种方式显得有点啰嗦。
"""




"""
Python引入了一个机制：引用计数。

                python内部使用引用计数，来保持追踪内存中的对象，Python内部记录了对象有多少个引用，即引用计数，当对象被创建时就创建了一个引用计数，当对象不再需要时，这个对象的引用计数为0时，它被垃圾回收。
                
                总结一下对象会在一下情况下引用计数加1：
                
                1.对象被创建：x=4
                
                2.另外的别人被创建：y=x
                
                3.被作为参数传递给函数：foo(x)
                
                4.作为容器对象的一个元素：a=[1,x,'33']
                
                引用计数减少情况
                
                1.一个本地引用离开了它的作用域。比如上面的foo(x)函数结束时，x指向的对象引用减1。
                
                2.对象的别名被显式的销毁：del x ；或者del y
                
                3.对象的一个别名被赋值给其他对象：x=789
                
                4.对象从一个窗口对象中移除：myList.remove(x)
                
                5.窗口对象本身被销毁：del myList，或者窗口对象本身离开了作用域。
                
                 
                
                垃圾回收
                
                1、当内存中有不再使用的部分时，垃圾收集器就会把他们清理掉。它会去检查那些引用计数为0的对象，然后清除其在内存的空间。当然除了引用计数为0的会被清除，还有一种情况也会被垃圾收集器清掉：当两个对象相互引用时，他们本身其他的引用已经为0了。
                
                2、垃圾回收机制还有一个循环垃圾回收器, 确保释放循环引用对象(a引用b, b引用a, 导致其引用计数永远不为0)。
                
                 
                
                在Python中，许多时候申请的内存都是小块的内存，这些小块内存在申请后，很快又会被释放，由于这些内存的申请并不是为了创建对象，所以并没有对象一级的内存池机制。这就意味着Python在运行期间会大量地执行malloc和free的操作，频繁地在用户态和核心态之间进行切换，这将严重影响Python的执行效率。为了加速Python的执行效率，Python引入了一个内存池机制，用于管理对小块内存的申请和释放。
                
                内存池机制

 

Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回给操作系统。

Python中所有小于256个字节的对象都使用pymalloc实现的分配器，而大的对象则使用系统的 malloc。另外Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。"""