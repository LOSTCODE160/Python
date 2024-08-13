#  single level inheritance
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

# multiple inheritance
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
    def __init__(self, father_name):
       # Grandfather.__init__(self, grandfather_name)
        self.father_name = father_name

class Son(Father):
    def __init__(self, son_name):
       # Father.__init__(self, grandfather_name, father_name)
        self.son_name = son_name

    def print_names(self):
        print("Grandfather name:", self.grandfather_name)
        print("Father name:", self.father_name)
        print("Son name:", self.son_name)

s1=son()

 
#hierarchical 
class father_name:
    def fathername(self):
        print("ram")
class son1_name(father_name):
    def sonname(self):
        print("sam")
class son2_name(father_name):
    def son2name(self):
        print("rom")
a=son1_name()
b=son2_name()
a.fathername()
a.sonname()
 




        
