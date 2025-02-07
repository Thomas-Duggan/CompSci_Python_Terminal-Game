# Copyright (c) 2020 Thomas Duggan
# This work is licensed under CC BY-SA 4.0


print("Simple Text-Based Adventure Game",'',sep='\n') #title

from random import randint
attack = randint(1,3) #Makes your stats one of these random numbers
attempt = 0
health = randint(10,20)

print("\/Beginning Stats\/")
print("Beginning Damage:",attack) #Says the numbers
print("Beginning Health:",health)


print('') #text seperator--------  \/FAIRY ZONE\/ --------


print('You slowly wake up in a radiant forest.','There are small creatures of all kinds surrounding you but you mainly see the blinding lights of small fairies.','You seem to be unsure where you are. What will you do?',sep='\n')
searchChance = 1

fairyZone = 1
while fairyZone == 1:
  
  print('Actions:','1: (Attack)','2: (Search)','3: (Continue)','4: (Check)',sep='\n')
  action = int(input('Your Action: ')) #shows the actions you can do
  
  if action == 1:
    if attempt == 0:
      print('','I cant let you do that, these creatures are too cute.',sep='\n') #first attempt at attacking them i dont let you
      attempt = 1
      print('')
      continue
    if attempt == 1:
      print('','Disregarding my request you attack them anyway.','Suprisingly, they are really tasty.','Your health has increased by 3',sep='\n')
      health = int(health + 3)
      attempt = 2
      print('')
      continue
    if attempt == 2:
      print ('','Sadly you ate all the cute little creatures already',sep='\n')
      print('')
      continue
      
  if action == 2:
    if searchChance == 0:
     print ('',"There's nothing else here",sep='\n')
      
    else:
      searchChance = randint (1,6)
      
      if int(searchChance < 2):
        print ('',"There's nothing here",sep='\n')

      if searchChance == 3:
        print('','You find a neat stick, your base attack increases by 1',sep='\n')
        attack = int(attack + 1)

      if searchChance == 4:
        print('','You find a flower, i wonder if you can create fireballs with this...','Oh, no you cant.',sep='\n')

      if searchChance == 5:
        print('','You find a flower, i wonder if you can create fireballs with this...','Oh, you can!','your base attack increases by 5',sep='\n')
        attack = int(attack + 5)

      if searchChance == 6:
        print('','You find a dotted mushroom, its illuminating an odd glow and is cold to the touch. would you like to consume it?',sep='\n')
          
        print('','Actions:','1.(Leave the creepy mushroom as is)','2.(Consume the weird glowing mushroom)',sep='\n')
        action = int(input('Your Action: ')) #shows the actions you can do

        if action == 2:
          print('','you feel severly weakened, your health is lowered significantlly',sep='\n')
          health = health - 10
            
        else:
         print('','you leave the weird mushroom as it is, good idea.', sep='\n')
    searchChance = 0
         
  if action == 4:
    print('','Your Health:',health,'Your Base Attack:',attack,sep='\n')
    
  if action == 3:
    print('',"You decide to find your way out of the forest.",sep='\n')
    fairyZone = 0
  
  print ('') #text seperator 
  
#                         -------- \/ORC BATTLE\/ --------
  
orcHealth = randint(5,50)
print ('Oh No! A level',orcHealth,'Orc blocked your path!')


while (int(orcHealth > 0)): #while the orcs health is more than 1 you can preform actions

  if health < 1: #quits the game if your health drops below 1
      quit ('YOU DIED, try again.')
      
 
  
  print('','Actions:','1: (Attack)','2: (Charged Attack)','3: (Check Stats)',sep='\n')
  action = int(input('Your Action: ')) #shows the actions you can do 

  if action == 1:
    diceAttack= randint(1,6)
    print ('') #text seperator
    print ('You roll a',diceAttack,'for attack in this turn') 
  if action == 2:
    diceAttack= randint(1,6)
    print ('') #text seperator
    print ('You roll a',diceAttack,'for attack in this turn') 
  
  if action == 1:
    crit = randint(1,10)
   #^gives you a chance to do more damage (crit)

    if crit == 10: #<Runs if you get a crit
      print ('Critical Hit! you get to roll again')
      crit = randint(1,6)
      print ('you roll a',crit) 
      print ('The orc takes',int(attack + diceAttack + crit),'damage, the orc now has',orcHealth,'health')      
      orcHealth = (orcHealth -(attack + diceAttack + crit))
      
    elif crit < 10:#<Runs if you do not
      orcHealth = int(orcHealth - (attack+diceAttack))
      print ('The orc takes',int(attack + diceAttack),'damage, the orc now has',orcHealth,'health')

  elif action == 2: 
    chargedAttack = randint(1,2)
    if chargedAttack == 2:
      print ('Your attack missed, the orc still has',orcHealth,'health') #welp.

    if chargedAttack == 1:
      orcHealth = int(orcHealth-((attack+diceAttack)*4)) #quadruples your damage if you hit
      print('You successfully charge, you do',int((attack + diceAttack)*4),'damage, the orc now has',orcHealth,'health')

  elif action == 3:
    print('Your Health:',health,'Your Base Attack:',attack,'Orc Health:',orcHealth,sep='\n')
    
  else:
    print ('The program doesnt understand what you wrote, please try again') 
    #runs the loop again if the program is confused
  
  if int(orcHealth<0): #if orc has negitive Health it will be set to 0
    orcHealth = 0
  
  if int(orcHealth>0):#if the orc is dead then it cannot attack
    
    if action == (2):#forces the orc to only attack if you also attack (1/2)
      orcAttack = randint(1,5)
      health = (int(health - orcAttack))  #lowers your health by the random number (Orc Attacks)
      print('The orc deals', orcAttack, 'damage, you now have', health,"health")
      
    if action == (1):
      orcAttack = randint(1,5)
      health = (int(health - orcAttack))  #lowers your health by the random number (Orc Attacks)
      print ('The orc deals', orcAttack, 'damage, you now have', health,"health")
      pass

print ("Congrats, the orc is now dead, you can now continue.") #orcs health is outside of the loop


#to be fixed:
#when you or orc is dead it can show a negitive number as health (maybe fix, its not that bad)
#fairy zone doesnt have a line when the program doesnt understand