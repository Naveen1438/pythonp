class student:


    def assign(self,rno,name):
        global math,science,eng
        self.rno=rno
        self.name=name
        math = int(input("math is="))
        eng = int(input("english is ="))
        science = int(input("science is ="))

    def display(self):
        global total,percent
        total=math+science+eng
        print(self.rno)
        print(self.name)
        print("total marks in all subjects:",total)
        percent=total/3
        print("percentage:",percent)
s=student()
s.assign(100,"naveen")
s.display()
