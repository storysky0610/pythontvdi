import tools
print(tools.SUN)
p1 = tools.Person(name="robert",age=30)
print(p1)
s1 = tools.Student(name="你好",age=31,chinese=87,english=75,math=67)
print(s1.name)
print(s1.age)
print(s1.enlish)
print(s1.math)
print(s1.chinese)
print(s1.total)
print(s1.average())
p2 = tools.get_person("名子",30)
print(p2)

print('===================')
s2 = tools.get_student("王",30)
print(s2)
print(s2.total)
print(s2.average())
