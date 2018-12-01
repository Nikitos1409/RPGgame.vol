class Fight:
  def __init__(self,f1,f2):
    self.f1 = f1#взятие статистики персонажа из player.py
    self.f2 = f2#взятие статистики персонажа из monster.py

  def tick(self):
    self.f1.hp = self.f1.hp - self.f2.attack()#кол-во ОЗ после получения урона для player
    self.f2.hp = self.f2.hp - self.f1.attack()#кол-во ОЗ после получения урона для monster 

