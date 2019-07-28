"""
函数桥套
    在一个函数的函数体内声明(定义)一个函数
"""
def foo():
    print("in the foo")
    def bar():
            print("in the bar")
    bar()
foo()