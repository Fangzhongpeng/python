
def dog(name):
    # 利用函数实现功能，只有一个步骤，就是让狗叫
    print(name + "wang wang wang func")
dog('1')
dog('2')
dog('3')


class Dog:
    #利用类实现功能，有两个步骤，1，造狗 2，让狗叫
    def __init__(self,name):     #简单理解__init__就是传参数的，
        self.name = name
    def buik(self):
        print(self.name+"wang wang wang class")
        print("%s:+wang wang wang class" % self.name)

d1 = Dog('one')
d2 = Dog('two')
d3 = Dog('方忠朋')
print(d1.buik())
print(d2.buik())
print(d3.buik())


####  函数和类都可以让狗叫，为什么需要类，因为python中规定了类有函数不具备的特性，继承，封装，多态，是的类使用的范围更广