#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[ ]:





# In[5]:


##Heroes
#1. Rogue
#2. Paladin
#3. Wizard


# In[51]:


class rogue():
    """Creates a rogue character that can poison an enemy, dodge attacks, and do extra damage"""
    def __init__(self, health, max_health, mana, max_mana, strength, base_strength, agility, base_agility,
                intelligence, base_intelligence, poison_lvl, dodge_lvl, level, exp, exp_needed):
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.strength = strength
        self.base_strength = base_strength
        self.agility = agility
        self.base_agility = base_agility
        self.intelligence = base_intelligence
        self.poison_lvl = poison_lvl
        self.dodge_lvl = dodge_lvl
        self.level = level
        self.exp = exp
        self.exp_needed = exp_needed
        
    def attack(self):
        """Returns the damage done when the hero attacks"""
        damage = (self.agility * 1.1) + (self.strength * .7)
        return damage
    
    def defend(self):
        """Returns the defense score of the rogue"""
        defense = (self.agility * .8) + (self.strength * .2)
        return defense
    
    def poison(self):
        """This allows the rogue to cast poison for 20 mana and causes 30 damage each round multiplied by poison_lvl"""
        poison_damage = 30 * self.poison_lvl
        return poison_damage
    def dodge(self):
        """Whenever the rogue is attack, there is a chance of dodging the attack. This is a passive ability."""
        dodge_chance = self.dodge_lvl * self.agility
        return dodge_chance
    
    def level_up(self):
        if self.exp >= self.exp_needed:
            print('You leveled up!')
            self.health += 20
            self.max_health +=20
            self.mana +=10
            self.max_mana += 10
            self.base_strength += 5
            self.base_agility +=10
            #self.base_intelligence += 1
            self.exp_needed *= 1.1
            self.exp = 0
            self.level += 1
    
my_rogue = rogue(health = 200, max_health = 200, mana=40, max_mana =40, strength = 10, base_strength =10, agility = 15,
                base_agility = 15, intelligence=5, base_intelligence = 5, poison_lvl = 1, dodge_lvl = 1, level=1,
                exp = 0, exp_needed = 100)

class paladin():
    """This creates a paladin character that can boost strength and heal itself."""
    def __init__(self, health, max_health, mana, max_mana, strength, base_strength, agility, base_agility,
                intelligence, base_intelligence, strengthen_lvl, heal_lvl, level, exp, exp_needed):
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.strength = strength
        self.base_strength = base_strength
        self.agility = agility
        self.base_agility = base_agility
        self.intelligence = base_intelligence
        self.strengthen_lvl = strengthen_lvl
        self.heal_lvl = heal_lvl
        self.level = level
        self.exp = exp
        self.exp_needed = exp_needed
        
    def attack(self):
        """Returns the attack amount of the paladin"""
        damage = (self.strength * 1.1) + (self.agility * 0.7)
        return damage
    
    def defend(self):
        """This returns the defense score of the paladin"""
        defense = (self.strength * 0.8) + (self.agility * 0.2)
        return defense
        
    def strengthen(self):
        """Increases the strength of the hero by 5 at a cost of 20 mana"""
        self.strength_lvl *= 5
        self.mana -= 20
        
    def heal(self):
        """Increases the paladin's health by 100 * heal_lvl"""
        heal_amount = 100 * self.heal_lvl
        if ((self.health + heal_amount <= self.max_health) & (self.mana >=20)):
            self.health += heal_amount
            self.mana -= 20
        elif ((self.health + heal_amount > self.max_health) & (self.mana >=20)):
            self.health = self.max_health
            self.mana -= 20
        elif self.mana <20:
            print("You don't have enough mana to cast that!!")
            
    def level_up(self):
        if exp >= exp_needed:
            print('You leveled up!')
            self.health += 30
            self.max_health +=30
            self.mana +=10
            self.max_mana += 10
            self.base_strength += 10
            self.base_agility +=5
            self.base_intelligence += 1
            self.exp_needed *= 1.1
            self.exp = 0
            self.level += 1
            
my_paladin = paladin(health = 200, max_health = 200, mana=40, max_mana =40, strength = 15, base_strength =15, agility = 10,
                base_agility = 10, intelligence=5, base_intelligence = 5, strengthen_lvl = 1, heal_lvl = 1, level=1,
                exp = 0, exp_needed = 100)

class wizard():
    """This creates a wizard character that can shoot fireballs and polymorph enemies"""
    
    def __init__(self, health, max_health, mana, max_mana, strength, base_strength, agility, base_agility,
                intelligence, base_intelligence, fireball_lvl, polymorph_lvl, level, exp, exp_needed):
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.strength = strength
        self.base_strength = base_strength
        self.agility = agility
        self.base_agility = base_agility
        self.intelligence = base_intelligence
        self.fireball_lvl = fireball_lvl
        self.polymorph_lvl = polymorph_lvl
        self.level = level
        self.exp = exp
        self.exp_needed = exp_needed
        
    def attack(self):
        """Returns the base damage of the wizard's attack"""
        damage = (self.strength * 0.5) + (self.agility * 0.5)
        return damage
    def defend(self):
        """Returns the defense score of the wizard"""
        defense = (self.strength *0.5) + (self.agility * 0.5)
        return defense
    def fireball(self):
        """Causes the mage to cast a fireball that does 100 damage * fireball_lvl"""
        fireball_damage = 100 * self.fireball_lvl
        self.mana -= 20
        return fireball_damage
    def polymorph(self):
        """Transforms the enemy monster into a random forest critter so they can't attack for 2 turns"""
        polymorph_success_chance = 20 * polymorph_lvl
        return polymorph_success_chance
    
    def level_up(self):
        if exp >= exp_needed:
            print('You leveled up!')
            self.health += 10
            self.max_health +=10
            self.mana +=100
            self.max_mana += 100
            self.base_strength += 1
            self.base_agility +=1
            self.base_intelligence += 10
            self.exp_needed *= 1.1
            self.exp = 0
            self.level += 1

my_wizard = wizard(health = 200, max_health = 200, mana=200, max_mana =200, strength = 10, base_strength =10, agility = 15,
                base_agility = 15, intelligence=15, base_intelligence = 15, fireball_lvl = 1, polymorph_lvl = 1, level=1,
                exp = 0, exp_needed = 100)


# In[52]:


#hero_initializer
my_paladin.exp


# In[53]:


#monsters
#Troll
#demon

class troll():
    """Creates a troll monster"""
    def __init__(self, health, max_health, strength, base_strength, agility, base_agility, exp_dropped):
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.base_strength = base_strength
        self.agility = agility
        self.base_agility = base_agility
        self.exp_dropped = exp_dropped
        
    def attack(self):
        """Returns the damage value of the troll"""
        damage = (self.strength *0.5) + (self.agility * 0.5)
        return damage
    def defend(self):
        """Returns the defense value of the troll"""
        defense = (self.strength * 0.5) + (self.agility * 0.5)
        return defense
my_troll = troll(health = 40, max_health = 40, strength = 10, base_strength=10, agility = 10, base_agility=10, exp_dropped=100)


# In[54]:


#battle actions

#battle function
def battle(hero, monster):
    """How everyone fights"""
    while ((hero.health > 0) & (monster.health > 0)):
        decision = input("You encounter a monster! Do you attack or flee?")
        if decision == 'attack':
            print("You attack the monster!")
            damage_to_monster = hero.attack() - monster.defend()
            damage_to_hero = monster.attack() - hero.defend()
            print("You did ", damage_to_monster, " damage to the monster!")
            print("The monster damaged you for ", damage_to_hero, " health!")
            if damage_to_monster > 0:
                monster.health -= damage_to_monster
            elif damage_to_hero > 0:
                hero.health -= damage_to_hero
            print("You're health: ", hero.health)
            print("Monster health: ", monster.health)
            if hero.health <= 0:
                print("You have died")
            elif monster.health <= 0:
                print("You killed the monster!!")
                hero.exp += monster.exp_dropped
                hero.level_up()

        elif decision == 'flee':
            print('You fled')
            break


# In[55]:


battle(my_rogue, my_troll)


# In[48]:


print(my_rogue.level)


# In[ ]:



#battle function
def battle(hero, monster):
    """How everyone fights"""
    while ((hero.health > 0) & (monster.health > 0)):
        decision = input("You encounter a monster! Do you attack or flee?")
        if decision == 'attack':
            print("You attack the monster!")
            damage_to_monster = hero.attack() - monster.defend()
            damage_to_hero = monster.attack() - hero.defend()
            print("You did ", damage_to_monster, " damage to the monster!")
            print("The monster damaged you for ", damage_to_hero, " health!")
            if damage_to_monster > 0:
                monster.health -= damage_to_monster
            elif damage_to_hero > 0:
                hero.health -= damage_to_hero
            print("You're health: ", hero.health)
            print("Monster health: ", monster.health)
            if hero.health <= 0:
                print("You have died")
            elif monster.health <= 0:
                print("You killed the monster!!")
                hero.exp += monster.exp_dropped
                hero.level_up()

        elif decision == 'flee':
            print('You fled')
            break

