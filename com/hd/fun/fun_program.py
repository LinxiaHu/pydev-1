# coding:utf-8

import math




# python函数式编程
# 变量可以指向函数
f = abs
a1 = f(-1)
print a1

# 高阶函数——能接收函数做参数的函数
def add(x, y, z):
    return f(x) + f(y)


a2 = add(-1, -2, abs)
print a2

print '------------------------------'


# 闭包函数
# 内层函数引用了外层函数的变量（参数也算变量），
# 然后返回内层函数的情况，称为闭包（Closure）
# 闭包的特点是返回的函数还引用了外层函数的局部变量，
# 所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。举例如下：

# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# 结果全部都是 9
# 原因就是当count()函数返回了3个函数时，
# 这3个函数所引用的变量 i 的值已经变成了3,
# 由于f1、f2、f3并没有被调用，所以，此时他们并未计算 i*i
# 因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量。
print f1()
print f2()
print f3()

print '------------------------------'

def count2():
    fs = []
    for i in range(1, 4):
        def inf(x):
            return x * x
        fs.append(inf)
    return fs

a2, b2, c2 = count2()
print a2(1)
print b2(2)
print c2(3)

print '------------------------------'

# 匿名函数
# 关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
# 使用匿名函数，可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码

myabs = lambda x:-x if x < 0 else x 
print myabs(-1)

print '------------------------------'

# 面向对象
class Person(object):
    address = 'Earth'  # 类属性,当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问
    
    @classmethod
    def how_many(self): # 类方法
        return Person.address
    
    def __init__(self, name):
        self.name = name
        self.__title = 'Mr'
        self.__job = 'Student'
    
    def getTitle(self):  # 第一个参数永远是self,但被调用时self不需要显式传入
        return self.__title
        

p = Person('张三')
# print p.__title #私有属性无法被外部变量访问
print p.name
print p.getTitle()
print Person.address
print Person.how_many()


class Student(Person):
    def __init__(self, name, score):
        super(Student, self).__init__(name) #父类构造：def __init__(self, name):
        self.score = score

s = Student('王五', '99')
print(s.score)
print(s.name)

print isinstance(s, Student)
print isinstance(p, Person)


print '------------------------------'
