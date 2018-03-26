# -*- coding: utf-8 -*-
"""
@author: AlbertoTP
"""

from classes.game import Person,bcolors

magic=[{"name":"Fire", "cost":10, "dmg":100},
       {"name":"Thunder", "cost":12, "dmg":120},
       {"name":"Blizzard", "cost":15, "dmg":150}]
       
#           hp,mp, atk, df, magic
player=Person(460,65,60,34,magic)
enemy=Person(1200,65,45,25,magic)

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
        magic_dmg=player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        
        current_mp=player.get_mp()
        if cost > current_mp:
            print (bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print (bcolors.OKBLUE + "\n"+ spell+" deals "+str(magic_dmg)+" points of damage"+ bcolors.ENDC)
        
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