class enemy:
    def __init__(self,x):
        self.enemy=x
    def get_energy(self):
        print(self.enemy)

Y=enemy(50)
T=enemy(45)
Y.get_energy()
T.get_energy()
