import random
class Monster:
  def __init__(self,name,type,strenght,hp):  
    self.x = 0
    self.y = 0
    self.name = name  
    self.type = type
    self.strenght = strenght
    self.hp = hp

  def say(self,text):
    print(text)

  def get_dmg(self):
    self.dmg = ((self.strenght**2)/2)*random.uniform(1,2)

test = Monster("Zyablik","bat",20,100)

test.say("Ай!Больно в ноге")