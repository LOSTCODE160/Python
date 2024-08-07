 #single level inheritance
class parent():
    def  last_name(self):
        print("kun")
class child(parent):
    def first_name(self):
        print("vithal")
    def last_name(self):  #overwrite the last name 
        print("chan")

a=child()
a.first_name()
a.last_name()

#multiple inheritance
class father():
    def father_name(self):
        print("ram")
class mother():
    def mother_name(self):
        print("sita")
class child(father,mother):
    def child_name(self):
        print("krishna")
a=child()
a.child_name()
a.father_name()
a.mother_name()


# Multilevel inheritance
class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name

class Father(Grandfather):
    def __init__(self, grandfather_name, father_name):
        Grandfather.__init__(self, grandfather_name)
        self.father_name = father_name

class Son(Father):
    def __init__(self, grandfather_name, father_name, son_name):
        Father.__init__(self, grandfather_name, father_name)
        self.son_name = son_name

    def print_names(self):
        print("Grandfather name:", self.grandfather_name)
        print("Father name:", self.father_name)
        print("Son name:", self.son_name)

# Create an instance of Son
s1 = Son('Lal mani', 'Rampal', 'Prince')
s1.print_names()



        
