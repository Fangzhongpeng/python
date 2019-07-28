
"""列表生成式"""
a = [i+1 for i in range(10)]
print(a)           #打印出列表的每个元素

"""生成器
        通过列表生成式，我们可以直接创建一个列表，但是受内存限制，列表容量肯定是有限的而且创建一个包含100万个元素的列表，不仅占用很大空间，如果我们
        仅仅需要访问前面几个元素，将会大大浪费内存
        所以如果列表元素可以按照某种算法推算出来，那我们就可以在循环的过程中不断推算出后续的元素，就不许创建完整的list,从而节省空间，在oython中
        这种一边循环以便计算的机制，成为生成器，generator.         """

b = (j*j for j in range(10))   # 第一种创建generator的方法,列表的[]改为（）
print(next(b))
print(next(b))                 #b保存的是算法，每调用一次next(b),就会计算出b的下一个元素的值
print(next(b))
print(next(b))
for n in b:                    #一般通过for循环来迭代generator而不是next()
    print(n)


def fib(max):    #斐波拉切数列的推算规则
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return '推算规则完成'     """但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，
                             必须捕获StopIteration错误，返回值包含在StopIteration的value中"""
print(fib(5))     #这里的结果就是一个数列
def fib2(max):    #斐波拉切数列的推算规则，定义列表生成式的另外一种方法
    n,a,b = 0,0,1
    while n < max:
        yield(b)
        a,b = b,a+b
        n = n + 1
    return '列表生成式完成'
for n in fib2(6):  #使用for循环来迭代取值
    print(n)
print(fib2(5))    #这里的结果的值就是fib2()的内存地址
print(fib2(100))  #这里的结果的值也是fib2()的内存地址
"""这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
                    在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。"""
data = fib2(10)
print(data)

print(data.__next__())
print(data.__next__())
print("干点别的事")
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())

#详解yeild参考https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/