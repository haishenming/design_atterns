"""
    面向对象
"""

# 封装：把数据和函数包装在类里  类的边界限制了一些外界的访问（私有属性，方法）
class A:
    def __init__(self, x):
        self.__personal = x

    def getpersonal(self):
        return self.__personal

    def setpersonal(self, x):
        self.__personal = x

# 继承：代码复用
class B(A):

    def setpersonal(self, x):
        # 重载父类方法
        self.__personal = x + 1

# 多态：python本身就是多态语言

