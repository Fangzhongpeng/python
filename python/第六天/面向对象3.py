"""
cs 游戏角色类代码分解

在python中，用变量表示特征，用函数表示技能，因而具有相同特征和技能的一类事物就是‘类’，对象是则是这一类事物中具体的一个。
"""


class Role():
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name       #角色的名字
        self.role = role       #角色是警察还是恐怖分子
        self.weapon = weapon   #角色的武器
        self.life_value = life_value   #角色的生命值
        self.money = money     #角色的钱

    def shot(self):
        #射击
        print("shooting...")

    def got_shot(self):
        #中枪
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        #买武器
        print(" %s just bought %s" %(self.name, gun_name))


r1 = Role('Alex', 'police', 'AK47')   """
        生成一个角色   ,类的实例化，初始化一个类，造了一个对象,这个过程相当于
        Role.__init__(***) 
    
       r1 = Role(r1,'Alex', 'police', 'AK47')  ，将实例本身传给类
       r1.name = "Alex"
       r1.Role = "Police"        实例能够访问类中的属性和方法
       r1.Money = 15000
       
    每当你根据Role类创建新实
    例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约
    定，旨在避免Python默认方法与普通方法发生名称冲突。
    Python调用这个__init__()方法来创建Role实例时，将自动传入实参self。每个与类相关联的方法
    调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    我们创建Role实例时，Python将调用Role类的方法__init__()。我们将通过实参向Role()传递名字和
    年龄；self会自动传递，因此我们不需要传递它。每当我们根据Dog类创建实例时，都只需给最
    后两个形参（name和age）提供值。
    处定义的两个变量都有前缀self。以self为前缀的变量都可供类中的所有方法使用，我们
    还可以通过类的任何实例来访问这些变量。self.name = name获取存储在形参name中的值，并将
    其存储到变量name中，然后该变量被关联到当前创建的实例。self.age = age的作用与此类似。
"""

r2 = Role('Jack', 'terrorist', 'B22')   # 生成一个角色
r1.buy_gun("AK44")

""" __init__  构造函数
实例化一个类的时候如果想实例传参数，必须在__init__里边定义，在实例化的时候做一些类的初始化的工作   def  __init__(***) 
就是一个初始化的过程


"""