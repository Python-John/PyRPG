Sword = False
coins = 10
damage = 2
monster = 5
#Mandatory
speed = 1
up = 0
right = 0
interact = False

for i in range(100):
  inputt = input()
#Movement
  if inputt == "a":
    right = right - speed
  elif inputt == "d":
    right = right + speed
  elif inputt == "w":
    up = up + speed
  elif inputt == "s":
    up = up - speed
  elif inputt == "e":
    interact = True
#Shop 1
  if up == 2 and right == 0 and interact == True:
    print("""Welcome, browse my wares
    1 Sword = 10 Coins""")
    interact = False
    inpu = input()
    if inpu == "1":
      coins = coins - 10
      print("Heres your Sword\n")
      Sword = True
#Enemy 1
  if up == 1 and right == 1 and interact == True:
    print(Sword)
    if Sword == True:
      damage = 5
    print("""Hraa!
    Enemy Health =""",str(monster)),
    print(""""
    Player Damage =""",str(damage))
    if inpu == 1:
      monster = monster - damage
      if monster < 1:
        pass
    
  
  
  print("""Map
  Shop = 0,2
  Monster = 1,1\n\n Coordinates""", right,up)
