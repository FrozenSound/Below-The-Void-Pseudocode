
Below the Void - Pseudocode Version
By Aaron Mayang


game start:
  menu start
    press start to play
    player can choose new game or load game
    new game = generate new file
    load game = open existing file

perk strength:
  when selected
    player gains 25% strength

perk speed:
  when selected
    player gains 25% speed

perk intelligence:
  when selected
    player gains 25% mana capacity
    player loses 25% strength

perk endurance:
  when selected
    player gains 25% resistance
    player loses 20% speed

base statistics:
  perk strength = 2.25 strength - 1 speed - 32 mana
    2 resistance
  perk speed = 2 strength - 1.25 speed - 32 mana
    2 resistance
  perk intelligence = 1.25 strength - 1.25 speed -    
    40 mana - 2 resistance
  perk resistance = 2 strength - 0.80 speed = 32 mana   2.5 resistance

item sword:
  usage melee
    wood sword = +1 strength
    copper sword = +2 strength
    iron sword = +4 strength
    steel sword = +8 strength
    titanium sword = +16 strength
    diamond sword = +32 strength
  damage
    damage = base strength * sword strength
  method
    when player left clicks (wielding a sword):
      swings in front and adjacent
      if any creature sword hits:
        deal _ damage

projectile magic:
  usage projectile
  damage
    damage = staff damage
  method
    if any creature projectile hits:
      deal _ spell damage
 
item staff:
  usage melee and magic
    apprentice staff = +3 spell damage
    adapt staff = +6 spell damage
    mage staff = +12 spell damage
    wizard staff = +24 spell damage
    sorcerer staff = +48 spell damage
    arcane staff = + 96 spell damage
  mana consumption
    mana consumption = staff damage/3
  method
    when player left clicks (holding a staff):
      fire magic projectile in the direction of the cursor
      if any creature projectie hits:
        deal _ spell damage

item armor:
  usage melee protection (without enchants)
  usage melee/spell protection (with enchants)
  without enchants
    leather armor = +5 resistance
    copper armor = +7.5 resistance
    chain mail armor = +10 resistance
    iron armor = +12.5 resistance
    steel armor = +15 resistance
    titanium armor = +17.5 resistance
    diamond armor = +20 resistance
    hardened diamond armor = +25 resistance
  with enchants
    leather armor = +5 resistence/+2.5 spell resistance
    copper armor = +7.5 resistence/+5 spell resistance
    chain mail armor = +10 resistence/+7.5 spell resistance
    iron armor = +12.5 resistence/+10 spell resistance
    steel armor = +15 resistence/+12.5 spell resistance
    titanium armor = +17.5 resistence/+15 spell resistance
    diamond armor = +20 resistence/+17.5 spell resistance
    hardened diamond armor = +25 resistence/+27.5 spell resistance
  damage infliction
    melee damage inflicted = (sword damage*base damage)-(armor resistance*base resistance)
      example 72(32*2.25)-62.5(25*2.5) = 9.5 damage inflicted
    spell damage inflicted = staff damage - (spell resistance*3)
      example 96(arcane staff)-82.5(27.5*3) = 14.5 damage inflicted

game generate:
  procedurally generate level(s)
    when new game is created:
      open("newfile.txt","w")
      level(s) generate random loot, gold, monsters (based on level)
    area of generating (0,0) - (15,15); (8,8) cannot be obstructed
      generate loot (rocks, crates, chests) _ (range(15),range(15))
      generate monsters _ (range(15),range(15))
    when monster is slain:
      drop gold range(1-15)
      
item/loot drops:
  drop chance
    swords 2-4 strength = 80% drop chance
    swords 8-16 strength = 15% drop chance
    swords 32 strength = 5% drop chance
  drop chance
    staffs 6-12 spell damage = 80% drop chance
    staffs 24-48 spell damage = 15% drop chance
    staffs 96 spell damage = 5% drop chance

monsters _ level xxx
  monsters _ levels (1-5):
    fragile skeleton - a skeleton whos bones are riddled with cracks
    skeleton - just a normal skeleton
    skeleton knight - this skeleton is given a helmet and a sword, to the king!
    skeleton giant - a far bigger threat, despite his brute strength he is far from capable of rivaling even the best of the best
    necromancer (miniboss) - summons the dead to do thy bidding (+1-4 skeletons every 10 seconds _ +1 skeleton knight every 20 seconds)

game mechanic
  -the player will begin (after they've created a world) by spawning in the center of a room
  -they can choose whether they'd like to go through the tutorial
  -once they have completed the tutorial (or have chosen not to)
  they will then get a cutscene of a person (them) falling into the abyss, where their true journey begins
controls
  -the player moves using wasd or the arrow keys, aims with the mouse (in the direction of the cursor), and left click to attack or use
  -the player must clear each floor in order to descend further into the endless (not at the moment) darkness that is the void
  -if any monsters (enemies) or objects drop loot, they simply have to walk close to it and they will pick up the item.
  -pressing esc will pause the game, but also acts as the options menu, where they can save their game, exit, or configure their settings
  -pressing e opens up the gui menu (their inventory)
inventory
  -the player can press e to open a gui menu, showcasing their character, inventory, and items currently equipped
  -to equip items from their inventory, they can hover their cursor over an item, select it and then choose to use it (any items they currently have equipped can be swapped out)
  -opening the inventory will pause the game until the player exits their inventory
bosses
  -after clearing several levels, the player may be faced with an enemy far more powerful than any which they may have seen
  -"mini bosses" will appear after 10 levels, whereas "bosses" appear every 20 levels
  -mini bosses are half the strength of normal bosses
  -upon succeeding in defeating the boss, the player will be granted loot that they may use on their journey
dying
  -if the player were to meet their unfortunate end, they will be greeted with a game over screen and the option to go back to the main menu, however they could also load their game and try again (assuming they saved)
    

    


    


    
      




  

    





