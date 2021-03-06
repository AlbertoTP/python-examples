# -*- coding: utf-8 -*-
"""
@author: AlbertoTP
"""

import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
class Person:
    def __init__(self, name, hp,mp, atk, df, magic, items):
        self.name=name
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.items=items
        self.actions=["Attack","Magic","Items"]

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)
        
    def generate_spell_damage(self,i):
        ngl=self.magic[i]["dmg"]-100
        ngh=self.magic[i]["dmg"]+100
        return random.randrange(ngl,ngh)
        
    def take_damage(self, dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp
        
    def heal(self, dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp
        
    def get_name(self):
        return self.name
        
    def get_hp(self):
        return self.hp
        
    def get_max_hp(self):
        return self.maxhp
        
    def get_percent_hp(self):
        percent = (self.get_hp()/self.get_max_hp())*100
        return percent
        
    def get_mp(self):
        return self.mp
        
    def get_max_mp(self):
        return self.maxmp
        
    def get_percent_mp(self):
        percent = (self.get_mp()/self.get_max_mp())*100
        return percent
        
    def reduce_mp(self, cost):
        self.mp-=cost
        
    def get_spell_name(self,i):
        return self.magic[i]["name"]
        
    def get_spell_mp_cost(self,i):
        return self.magic[i]["cost"]
        
    def choose_action(self):
        i=1
        print ("\n    "+bcolors.BOLD+str(self.name)+bcolors.ENDC)
        print (bcolors.OKBLUE + bcolors.BOLD + "    Actions" + bcolors.ENDC)
        for item in self.actions:
            print ("        "+str(i)+".",item)
            i+=1
            
    def choose_magic(self):
        i=1
        print ("\n"+bcolors.OKBLUE + bcolors.BOLD + "    Magic" + bcolors.ENDC)
        for spell in self.magic:
            print ("        "+str(i)+".{:10}".format(spell.name),"cost:{:3}".format(spell.cost) )
            i+=1
            
    def choose_item(self):
        i=1
        print ("\n"+bcolors.OKGREEN+bcolors.BOLD+"    Items:"+bcolors.ENDC)
        for item in self.items:
            print ("        "+str(i)+".",item["item"].name,":",item["item"].description,"(x"+str(item["quantity"])+")")
            i+=1
            
    def choose_target(self,enemies):
        i=1
        print ("\n"+bcolors.FAIL+bcolors.BOLD+"    TARGET:"+bcolors.ENDC) 
        for enemy in enemies:
            if enemy.get_hp()!=0:
               print ("        "+str(i)+". ",enemy.name) 
            i+=1
        choise=int(input("    Choose Target:"))-1
        return choise
            
    def get_enemy_stats(self):
        hp_bar=""
        bar_ticks=(self.hp/self.maxhp)*100 /2
        while bar_ticks>0:
            hp_bar+="█"
            bar_ticks-=1
        while len(hp_bar)<50:
            hp_bar+=" "
            
        hp_string=str(self.hp)+"/"+str(self.maxhp)
        print ("                         __________________________________________________")
        print (bcolors.BOLD+str(self.name)+"    "+"{:11}".format(hp_string)+"  |"+
               bcolors.FAIL+hp_bar+bcolors.ENDC+"|")
            
    def get_stats(self):
        hp_bar = ""
        if self.hp<self.maxhp:
            bar_ticks=(self.hp/self.maxhp)*100 / 5
            while bar_ticks > 0:
                hp_bar+="█"
                bar_ticks-=1
            while len(hp_bar)<20:
                hp_bar+=" "
        else:
            for i in range(0,20):
                hp_bar+="█"
        
        mp_bar=""
        bar_magic=(self.mp/self.maxmp)*100 / 10
        while bar_magic > 0:
            mp_bar+="█"
            bar_magic-=1
        while len(mp_bar)<10:
            mp_bar+=" "
            
        hp_string=str(self.hp)+"/"+str(self.maxhp)
        mp_string=str(self.mp)+"/"+str(self.maxmp)
        
        #                               HP=20                          MP=10
        print ("                          ____________________             __________")
        print (bcolors.BOLD+str(self.name)+"    "+"{:11}".format(hp_string)+"  |"+
               bcolors.OKGREEN+hp_bar+bcolors.ENDC+
               bcolors.BOLD+"|  "+"{:7}".format(mp_string)+"  |"+
               bcolors.OKBLUE+mp_bar+bcolors.ENDC+
               bcolors.BOLD+"|")
            
#    def choose_enemy_spell(self):
#        magic_choice = random.randrange(0, len(self.magic))
#        spell = self.magic[magic_choice]
#        magic_dmg = spell.generate_damage()
#
#        pct = self.hp / self.maxhp * 100
#
#        if self.mp < spell.cost or spell.type == "white" and pct > 50:
#            self.choose_enemy_spell()
#        else:
#            return spell, magic_dmg
