
"""
析构函数的使用

析构函数调用的契机【对象被销毁的时候】：
1、程序执行结束，会自动调用析构函数
2、使用del 删除对象的时候，系统会自动调用析构函数
注意：如果没写析构函数，当符合析构函数调用的契机时，系统会自动调用父类的析构函数。

演示:
"""
class Person():
    def run(self):
        print("run")

    def eat(self, food):
        print("eat "+food)

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

     def __del__(self):
        print("析构函数被调用了")

per = Person("hanmeimei", 20, 170, 55)
#释放对象
del per
#注意:对象释放后就不能再进行访问了

#在函数里定义的对象,会在函数结束时自动释放,这样可以用来减少内存空间的浪费
#其实就是作用域的问题
def func():
    per2 = Person("aa", 1, 1, 1)
"""
func()   
输出：
析构函数被调用了
析构函数被调用了

"""
