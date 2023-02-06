#Create class OOPS and implement all oops concept in that.

class Student:
    # static variable
    school = "sch"" ""="" ""CGA"
    company = "com"" ""="" ""cloudEQ"

    def __init__ (s,a,b,c):
        s.a = a
        s.b = b
        s.c = c

    def avg(s):
        return (s.a + s.b + s.c)/3
    @classmethod
    def inf(sch):
        return sch.school
        
    @classmethod
    def inf1(com):
        return com.company
    
    def inf2():
        print("This Is a Static Method..")



a1 = Student(15,2,54)
a2 = Student(54,70,6)

print(a2.avg())
print(Student.inf())
print(Student.inf1())
print(Student.inf2())
