import json
f = open("xuliehua.txt","r")
#data = f.read()

"""
#传统方式反序列化
data = eval( f.read() )    #eval 将字符串str当成有效的表达式子来求值并返回计算结果。
f.close()
print(data['age'])
print(data)

"""
#json格式反序列化    读取硬盘数据

data = json.loads(f.read())   # =json.load(f)
print(data)
print(data["age"])