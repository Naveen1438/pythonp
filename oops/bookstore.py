class Books:
    def assign(self, bno, bname,btitle,bauthor):
            global quantity, price
            self.bno =  bno
            self.bname = bname
            self.btitle = btitle
            self.bauthor = bauthor
            quantity = int(input("quantity is="))
            price = int(input("price is ="))

    def display(self):
            global billamount
            print(self.bno)
            print(self.bname)
            print(self.btitle)
            print(self.bauthor)
            billamount = quantity * price
            print("total billamount:", billamount)

s1 = Books()
s1.assign(100, "python","welcom to python","naveen")
s1.display()
