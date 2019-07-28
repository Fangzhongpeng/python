"""
什么是序列化：
    我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，
        marshalling，flattening等等，都是一个意思。序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

        现在就先介绍一下牛逼的json：

            如果我们要在不同的编程语言之间传递对象，数据交互，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
        可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
    """
import json

info = {
    'name':'fangzongpeng',
    'age':22
}

#使用传统方式序列化
"""
f = open("test.txt","w")
f.write(str(info))         #硬盘只能存储字符串，必须转换成字符串形式，将字典的数据类型序列化成字符串，将内存的数据存储到硬盘上
f.close()
"""

#使用json序列化
f = open("xuliehua.txt","w")
print(json.dumps(info))
f.write(json.dumps(info))  #   =json.dump(info.f)
f.close()