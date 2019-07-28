"""
Json，用于字符串 和 python数据类型间进行转换
Pickle，用于python特有的类型（类，函数）和 python的数据类型间进行转换，使用方法和json一样

json.dumps(data)   #将data转化为str类型
json.loads(data)     #还原data的数据类型
json不能序列化函数（函数名）、类等对象，但是pickle可以
json提供四个功能：dumps,dump,loads,load
pickle提供四个功能：dumps,dump,loads,load
pickle模块和json模块还是比较实用的，还有许多的信息可以去了解，


那么为什么需要序列化和反序列化这一操作呢？
pickle序列化过程将文本信息转变为二进制数据流,所以pickle 需要以 rb 和wb的方式读取和写文件而json不需要。这样就信息就容易存储在硬盘之中，	当需要读取文件的时候，从硬盘中读取数据，然后再将其反序列化便可以得到原始的数据。
---------------------

"""