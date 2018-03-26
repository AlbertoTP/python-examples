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
    def __init__(self, hp,mp, atk, df, magic, items):
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
        ngl=self.magic[i]["dmg"]-5
        ngh=self.magic[i]["dmg"]+5
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
        print ("\n"+bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print ("    "+str(i)+".",item)
            i+=1
            
    def choose_magic(self):
        i=1
        print ("\n"+bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print ("    "+str(i)+".{:10}".format(spell.name),"cost:{.3}".format(spell.cost) )
            i+=1
            
    def choose_item(self):
        i=1
        print ("\n"+bcolors.OKGREEN+bcolors.BOLD+"ITEMS:"+bcolors.ENDC)
        for item in self.items:
            print ("    "+str(i)+".",item.name,":",item.description,"(x5)")
            i+=1
