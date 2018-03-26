# -*- coding: utf-8 -*-
"""
@author: AlbertoTP
"""

from classes.game import Person,bcolors
from classes.magic import Spell

#Create Black Magic
fire = Spell("Fire",10,100,"black")
thunder = Spell("Thunder",5,180,"black")
blizzard = Spell("Blizzard",12,200,"black")
meteor = Spell("Meteor",25,500,"black")
quake = Spell("Quake",10,100,"black")

#Create white Magic
cure = Spell("Cure",10,100,"white")
cura = Spell("Cura",20,500,"white")
       
#Instantiate People
#           hp,mp, atk, df, magic
player=Person(500,90,60,34,[fire, thunder,blizzard,meteor,cure,cura])
enemy=Person(1500,60,45,25,[])

runnig=True
i=0

while runnig:
    print ("==="*15)
    
    print ("\nPlayer HP:",bcolors.OKGREEN+"{0:.0f}%".format(player.get_percent_hp())+" = "+str(player.get_hp())+"/"+str(player.get_max_hp())+bcolors.ENDC+"\n")
    print ("Player MP:",bcolors.OKGREEN+"{0:.0f}%".format(player.get_percent_mp())+" = "+str(player.get_mp())+"/"+str(player.get_max_mp())+bcolors.ENDC+"\n")
    print ("Enemy HP:",bcolors.FAIL+"{0:.0f}%".format(enemy.get_percent_hp())+" = "+str(enemy.get_hp())+"/"+str(enemy.get_max_hp())+bcolors.ENDC+"\n")
    
    print ("---"*15)
    
    player.choose_action()
    choice=input("Choose action: ")
    index=int(choice)-1
    
    if index == 0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print ("You attacked for ",dmg," points of damage.")
    elif index==1:
        player.choose_magic()
        magic_choice=int(input("Choose magic:"))-1
        
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        current_mp=player.get_mp()
        if spell.cost > current_mp:
            print (bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        
        player.reduce_mp(spell.cost)
        if spell.type == "white":
            player.heal(magic_dmg*-1)
            print (bcolors.OKBLUE+"\n"+spell.name+" heals for "+str(magic_dmg)+" HP"+bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print (bcolors.OKBLUE + "\n"+ spell.name+" deals "+str(magic_dmg)+" points of damage"+ bcolors.ENDC)
        
    enemy_choice=1
    enemy_damage=enemy.generate_damage()
    player.take_damage(enemy_damage)
    print ("Enemy attacks for ",enemy_damage," points.")
    
    
    if enemy.get_hp()==0:
        print (bcolors.OKGREEN+"You win!!!"+bcolors.ENDC)
        runnig = False
    elif player.get_hp()==0:
        print (bcolors.FAIL+"Your enemy has defeated you!"+bcolors.ENDC)
        runnig = False