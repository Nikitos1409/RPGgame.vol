import random "мы импортируем модуль рандом"
class Player: "создаём класс player"
  def __init__(self,name,straight,hp): ""в классе player прописываем его имя,его
  сила и здоровье""
    self.name=name "имя"
    self.straight=straight "сила"
    self.x=0
    self.y=0
    self.hp=100 "здоровье"


  def say(self, text):  "функция для текста"
    print(text) "выводим текс"

  def get_damage(self): "создаем функцию урона"
    self.damage=(((self.straight)**2)/2)*random.uniform(1,2) "сдесь формула нанесения урона"

    return self.damage

  def attack(self): "функция атаки"
    return self.get_damage()/2 "вычесление атаки"
