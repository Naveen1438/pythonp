class Customer:
    def assign(self, name):
            global noofpeople,tourdate
            self.name = name
            noofpeople = int(input("noofpeople is="))
            tourdate= input("tourdate is =")

    def tour(self):
        global cost

       # print(self.name)
        cost=dcost * noofpeople
        print("total cost for all customers:", cost)
    def type(self):
        global category,dcost,d,h,p
        d = 2000
        print("for discover india=",d)
        h = 1000
        print("for holiday=",h)
        p = 500
        print("for piligrimage=", p)

        category = int(input("enter the amopunt displayed above to choose type u want visit"))
        if category == 2000:
            print("ur choosen for discover india")
            dcost = 2000
        elif category == 1000:
            print("ur choosen for holiday")
            dcost = 1000
        else:
            print("ur choosen for piligrimage")
            dcost = 500

s1 =Customer()
s1.assign("naveen")
s1.type()
s1.tour()