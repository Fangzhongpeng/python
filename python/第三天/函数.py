# 定义：
def greet_user():
    print("Hello")
# 调用
greet_user()
"""
 函数参数
    实参和形参
        执行函数时，实参的值被存储在形参中
    位置实参
        第n个实参传递给n个形参
    关键字实参
        调用函数时以键值对的方式执行哪个实参给哪个形参

"""

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

#形参默认值
def describe_peg(name,animal_type='dog'):
    print("\n I hava a " + animal_type)
    print("\nMy"+ animal_type + "'s name is" + name.title()+".")
describe_peg("wh")

