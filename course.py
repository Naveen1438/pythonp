class Courses:
    def __init__(self):
        global cname,course,duriation,fee
        course=input("enter the course")
        if course=="python":
            cname = "python"
            duriation=3
            fee=3000
            print("course name =",cname)
            print("duriation time in months =",duriation)
            print("fee for course =",fee)

        elif course=="java":
            cname="java"
            duriation=4
            fee=4000
            print("course name =", cname)
            print("duriation time in months =", duriation)
            print("fee for course =", fee)

        elif course=="datascience":
            cname="datascience"
            duriation=3
            fee=5000
            print("course name =", cname)
            print("duriation time in months =", duriation)
            print("fee for course =", fee)
        else:
            print("enter valid course")
    def GetTotalFee(self,cname,noofstd,time):
        global name,fee,ctype,tfee
        ctype=input("enter ctype=")
        if ctype=="onsite":
            tfee=fee+(fee*10/100)
            self.cname=cname
            self.noofstd=noofstd
        elif ctype=="parttime":
            tfee=fee-(fee*10/100)
            self.time=time
        else:
            print("enter valid type")

    def print(self):
        print("couse name=",cname)
        print("total fee=",tfee)


c=Courses()
c.GetTotalFee(cname="infosys", noofstd=20, time=2)
c.print()