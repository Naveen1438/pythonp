class student:


    def assign(self,rno,name):
         global math, science, eng
         self.rno = rno
         self.name = name
         math = int(input("math is="))
         eng = int(input(" english is ="))
         science =int(input("science is ="))

    def display(self):
        global total, percent
        print(type(self.rno))
        print(self.name)
        total = math + science + eng
        print("total marks in all subjects:",total)
        percent = total / 3
        print("percentage:",percent)
s1=student()
s1.assign(100,"naveen")
s1.display()
s2=student()
s2.assign(101,"lavan")
s2.display()
s3=student()
s3.assign(102,"praveen")
s3.display()
s4=student()
s4.assign(103,"pavan")
s4.display()
s5=student()
s5.assign(104,"villan")
s5.display()
