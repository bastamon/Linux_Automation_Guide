# -*-coding:utf-8 -*-
class People:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print("""
        ===========个人信息==========
        姓名：%s
        年龄：%s
        性别：%s
        """ %(self.name,self.age,self.sex))


class Teacher(People):

    def __init__(self, name, age, sex, level, salary):
        super().__init__(name,age,sex)

        self.level = level
        self.salary = salary

    def tell_info(self):
        super().tell_info()
        print("""
        等级：%s
        薪资：%s
        """ %(self.level,self.salary))

tea1 = Teacher('egon',18, 'male', 9, 3.1)
print(tea1.name, tea1.age, tea1.sex, tea1.level, tea1.salary)
tea1.tell_info()