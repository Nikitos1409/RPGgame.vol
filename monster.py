import random "вызываем модуль рандом"
class Monster:
  def __init__(self,name,type,strenght,hp):  "сдесь то что состит в классе монстр"
    self.x = 0
    self.y = 0
    self.name = name  "имя"
    self.type = type "тип"
    self.strenght = strenght "сила"
    self.hp = hp "здоровье"

  def say(self,text): "функция разговора"
    print(text)

  def get_dmg(self): "получение дамага"
    self.dmg = ((self.strenght**2)/2)*random.uniform(1,2) "формула получения дамаг"

test = Monster("Zyablik","bat",20,100)

test.say("Ай!Больно в ноге")