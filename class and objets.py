class enemy:
    life =3
    def attack(self):
        print("ouch")
        self.life-=1
    
    def checklife(self):
        if self.life<=0:
            print('im dead')
        else:
            print(str(self.life)+"life left")
enemy1=enemy()
enemy2=enemy()
enemy1.attack() 
enemy1.checklife()

