class Person:
    def __init__(self,fname,lname,email,dob):
        self.fname=fname
        self.lname=lname
        self.email = email
        self.dob = dob
    def display(self):
        print("first name=",self.fname)
        print("last name=",self.lname)
        print("email id=",self.email)
        print("date of birth=",self.dob)
p=Person("naveen","kumar","ynaveenreddy590@gmail.com","10/12/1196")
p.display()