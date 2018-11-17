import random
class Player:
  def __init__(self,name,straight,hp):
    self.name=name
    self.straight=straight
    self.x=0
    self.y=0
    self.hp=100
  

  def say(self, text):
    print(text)
  
  def get_damage(self):
    self.damage=(((self.straight)**2)/2)*random.uniform(1,2)

    return self.damage
  
  def attack(self):
    return self.get_damage()/2 
  

