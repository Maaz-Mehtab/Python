# Write a code in python in which create a class named it Car which
# have 5 attributes such like (model, color and name etc.) and 3
# methods. And create 5 object instance from that class.

class Car:
    model=2019
    color="black"
    name="Corolla"
    company="Toyota"
    engine="1700CC"
    def getname(self):
         print("Name: %s"%(self.name))  
    def getModal(self):
        print("Modal: %d"%(self.model))  
    def getcompany(self):
        print("Company: %s"%(self.company))  
c1=Car()
c2=Car()
c3=Car()
c4=Car()
c5=Car()
c1.getname()
c2.getModal()
c2.getcompany()