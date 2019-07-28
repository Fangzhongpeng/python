"""
re模块

    re是提供正则表达式匹配操作的模块.

    在任何编程语言中, 对文本字符串的处理都是一个比较重要的内容.

    前面我们已经学习过str, 但是他对正则表达式的处理能力相对比较弱, 目前各大编程语言都支持一种更强的处理字符串的工具:正则表达式(regular expression)


    字符串是在程序处理的最多的一种数据, 程序对字符串的操作简直无处不在.

    比如去判断用户的输入的数据是否为一个合法的电话号码, 如果像以前的普通的处理方式, 一个一个的字符去判断就非常的麻烦, 代码的可读性也差. 判断一个 email 是不是一个合法的电邮等等这些需求, 都是比较平常的问题.

    所以, 各大编程语言几乎都支持一种功能更加强大, 简单易用的处理字符串的工具: 正则表达式

什么是正则表达式

    正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

    Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。

    re 模块使 Python 语言拥有全部的正则表达式功能。

    re 模块提供了一些方法，这些方法使用一个模式字符串做为它们的第一个参数。

    常用正则表达式符号

'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c


'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'

'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}


"""


import re

res = re.match("^fang\d+","fang321zhongpeng123")
print (res)
print (res.group())

