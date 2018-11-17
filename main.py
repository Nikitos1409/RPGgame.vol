import player
import monster
def title_screen_selection():
  ALLOWD_COMMANDS = ["play", "exit"]

  command = input("@> ").lower()

  if command in ALLOWD_COMMANDS:
    print(command)
  
  else:
    print("Ошибка команды! ")
  
title_screen_selection()

def get_play():
  name=input("ваше имя")
  straight=int(input("введите силу"))

  pl = player.Player(name,straight,hp)
  mn = monster.Monster(name,type,strenght,hp)
