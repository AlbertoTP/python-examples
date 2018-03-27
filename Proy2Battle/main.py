# -*- coding: utf-8 -*-
"""
@author: AlbertoTP
"""
import random
from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Item


#Create Black Magic
fire = Spell("Fire",10,500,"black")
thunder = Spell("Thunder",30,3000,"black")
blizzard = Spell("Blizzard",20,700,"black")
meteor = Spell("Meteor",300,10000,"black")
quake = Spell("Quake",10,300,"black")

#Create white Magic
cure = Spell("Cure",10,100,"white")
cura = Spell("Cura",50,3000,"white")

#Create some items
potion=Item("Potion","potion","Heals 50HP",50)
hipotion=Item("Hi-Potion","potion","Heals 600 HP",600)
superpotion=Item("Super Potion","potion","Heals 1500 HP",1500)
elixer=Item("Elixer","elixer","Fully restore HP/MP of one member",9999)
hielixer=Item("MegaElixer","elixer","Fully restores party's HP/MP",9999)

grenade=Item("Grenade","attack","Deals 1000 damage",1000)

player_spells=[fire, thunder,blizzard,meteor,cure,cura]
player_items=[{"item":potion,"quantity":10},
              {"item":hipotion,"quantity":3},
              {"item":superpotion,"quantity":2},
              {"item":elixer,"quantity":3},
              {"item":hielixer,"quantity":2},
              {"item":grenade,"quantity":3}]

#Instantiate People
#           hp,mp, atk, df, magic
player1=Person("Alterno:",5500,500,500,200,player_spells,player_items)
player2=Person("Wizzard:",3000,900,200,100,player_spells,player_items)
player3=Person("Warrior:",6000,100,900,500,player_spells,player_items)

enemy1=Person("Enemy01",18000,700,525,25,[],[])
enemy2=Person("Enemy02",12000,130,560,325,[],[])
enemy3=Person("Enemy03",15000,130,560,325,[],[])

players=[player1,player2,player3]
enemies=[enemy1,enemy2,enemy3]

runnig=True
i=0
defeat_enemies=0
defeat_players=0

while runnig:
    print ("==="*15)
    
    for player in players:
        
        #Stats
        print (bcolors.BOLD+"NAME                      HP                               MP")
        for play in players:
            play.get_stats()
        for enemy in enemies:
            enemy.get_enemy_stats()
        
        player.choose_action()
        choice=input("    Choose action: ")
        index=int(choice)-1
        
        if index == 0:
            dmg=player.generate_damage()
            enemy=player.choose_target(enemies)
            if len(enemies)!=0:
                enemies[enemy].take_damage(dmg)
                print ("You attacked "+enemies[enemy].name+" for ",dmg," points of damage.")
            
            if enemies[enemy].get_hp()==0:
                print (bcolors.FAIL,enemies[enemy].name+ " has died."+bcolors.ENDC)
                del enemies[enemy]
        elif index==1:
            player.choose_magic()
            magic_choice=int(input("    Choose magic:"))-1
            
            if magic_choice == -1:
                continue
            
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
                enemy=player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print (bcolors.OKBLUE + "\n"+ spell.name+" deals "+str(magic_dmg)+" points of damage to ",enemies[enemy].name, bcolors.ENDC)
                
                if enemies[enemy].get_hp()==0:
                    print (bcolors.FAIL,enemies[enemy].name+ " has died."+bcolors.ENDC)
                    del enemies[enemy]
        elif index==2:
            player.choose_item()
            item_choice=int(input("    Choose item: "))-1
            
            if item_choice==-1:
                continue
            
            item=player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print (bcolors.FAIL+"\n None left..."+bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -=1
            
            if item.type=="potion":
                player.heal(item.prop*-1)
                print (bcolors.OKGREEN+"\n"+item.name+" heals for ",str(item.prop)," HP"+bcolors.ENDC)
            elif item.type=="elixer":
                player.hp=player.maxhp
                player.mp=player.maxmp
                print (bcolors.OKGREEN+"\n"+item.name+" fully restores HP/MP"+bcolors.ENDC)
            elif item.type=="attack":
                enemy=player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print (bcolors.FAIL+"\n"+item.name+" deals ",str(item.prop)," points of damage to ",enemies[enemy].name,bcolors.ENDC)
                
                if enemies[enemy].get_hp()==0:
                    print (bcolors.FAIL,enemies[enemy].name+ " has died."+bcolors.ENDC)
                    del enemies[enemy]
            
        enemy_choice=1
        target=random.randrange(0,3)
        if len(enemies)!=0:
            enemy_damage=enemies[0].generate_damage()
            players[target].take_damage(enemy_damage)
            print ("Enemy attacks ",players[target].get_name()," for ",enemy_damage," points.")
        
            for en in enemies:
                if en.get_hp()==0:
                    defeat_enemies += 1
                    print ("Enemy died.")
        else:
            defeat_enemies=2
                
        for play in players:
            if play.get_hp()==0:
                defeat_players += 1
                print ("Player died.")

        if defeat_enemies==2:
            print (bcolors.OKGREEN+"You win!!!"+bcolors.ENDC)
            runnig = False
            break
        elif defeat_players==2:
            print (bcolors.FAIL+"Your enemies have defeated you!"+bcolors.ENDC)
            runnig = False
            break