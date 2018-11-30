import player #импортируем player 
import monster # импортируем monster
def title_screen_selection():
  ALLOWD_COMMANDS = ["play", "exit"]#список разрешенных команд

  command = input("@> ").lower()#приводит к нижнему регистру

  if command in ALLOWD_COMMANDS:#(если команда есть в списке команд)
    print(command)
  
  else:
    print("Ошибка команды! ")
  
title_screen_selection()

def get_play():
  name=input("ваше имя")
  straight=int(input("введите силу"))

  pl = player.Player(name,straight,hp)
  mn = monster.Monster(name,type,strenght,hp)

