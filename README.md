# Sean-and-Gils-Game-Demo
Game prototype.

Protoype 2.0

List of stuff we need:

Environment:
-3 “frames”
	-Quest Giver Room
	-Street Scroll
	-Shop
Player
-Character
	-Idol with gun
	-Idol without gun
	-Walk cycle with gun
	-walk cycle without gun
	-Melee attack
-3 Weapons
	-Sword
	-Gun (Bullet)
	-Bat
-NPCs
	-Quest Giver “Old Man”
-Melee Enemy
-Melee Enemy Walk cycle
-Melee Enemy Attack Telegraph
-Melee Enemy Attack
-Ranged Enemy
-Ranged Enemy Attack Telegraph
-Ranged Enemy Attack
-Shopkeeper (May be part of background)
-Shady Guy
-Items
	-Pack of Cigarettes
-Interactions
	-Weapon indicator
	-Item indicator
	-Speech Bubbles
	-Dialogue selection

Prototype 2 Synopsis:
	The player begins in the quest giver room with the bat equipped. The old man is also in the room. When the player interacts with the old man he will request that the player buy him some cigarettes. The player can respond either “yes” or “no” and the old man responds accordingly. If the player answered “yes”, the old man will give him some money. The player leaves the quest giver room and enters the street scroll. 
	When the player enters the street scroll, he is confronted with a melee enemy and is introduced to melee combat. Using the bat, the enemy will die after 2 attacks. Once the enemy is killed, the player can continue walking down the street and will encounter a collectable gun. Further down the street, the player will come upon a ranged enemy and will be introduced to ranged combat. Once the ranged enemy is killed, the player will walk further down the street and get to the convenience store.
	The player enters the convenience store and will be able to walk up to a collectable pack of cigarettes and be given the option to purchase the item.
	When the player leaves the convenience store, a shady man will be standing outside. The player has the option to talk to the shady man and be given the option to end the demo at that moment or refuse and walk the pack of cigarettes he purchased back to the old man. 
If the player chooses to deliver the cigarettes to the old man, the old man will be thankful and will gift the player with the sword. The sword kills enemies in only 1 hit. When the player leaves the quest giver room, he will be confronted with 2 new melee enemies. Once the enemies are killed, the player can walk back down to the convenience store and still see the shady man standing outside. The player will then interact with the shady man outside of the convenience store and end the demo.

List of stuff for Sean:
	-Create environments
	-Create scrolling frames
	-Create non-scrolling frames
	-Implement walk
	-Implement jump
	-Animate characters
	-Animate character actions
	-Create main menu
	-Create pause screen with inventory displayed
	-Implement melee combat
	-Implement ranged combat
	-Create interactable dialog system
	-Create health interface
	-Create money interface
	-Create item interface
	-Create weapon interface
	-Pick up items
	-Purchase items
	-Implement item inventory system
	-Implement weapon inventory system
	-Change weapons

Controls:
Left arrow key or A key: walk left
	Right arrow key or D key: walk right
	Up arrow key or spacebar: jump
	Left mouse click: melee attack
	Right mouse click: ranged attack
	1 key: Change melee weapon (cycle for now)
	2 key: Change ranged weapon (cycle for now)
	C key: pick up or purchase item
	E key: interact with character
	
Window Size:
	800x600
	

Sean and Gil’s Game Design Doc.

Platform: PC (But it would be a good idea to design with a console controller in mind.)

Overview
Mechanics
Proof of Concept / Demo
Story Concept

1. Overview

We’re making a game! In my vision, I see a top down, action game, with strategic combat, and RPG elements in dialogue and faction allegiance.

2. Mechanics

The player has an array of weaponry. Each item has a different function: ranged, melee, AOE, etc. Weapons will only work against certain enemies - a sword wouldn’t work against an enemy across the stage and a sniper rifle would be useless against an enemy charging at the player. 

Only 2 items can be held at once. This could change depending on the perspective. If we go for an isometric camera angle it may render a jump button unnecessary, thus opening up an additional button.

There are a set number of weapons in the game and they are upgraded as the player progresses through the campaign, ya know, like in Bioshock. Examples of upgrades could be:

-Increased damage, obviously.
-A successful hit could freeze time allowing the player to immediately target another opponent without any of the other enemies moving.
-A combo of 10x or more allows the player to teleport to another enemy after a successful strike with a melee weapon.
-Increase/reduced range.

The player approaches combat by directionally targeting an enemy then clicking and dragging on PC or with the analog stick on a console controller and finally pressing the key or button for the weapon they would like to use. (It will require an adjustment for it to work properly on a controller, but I’ll get into that later.)

Combat Scenario: The player enters a stage with a medium ranged rifle and a sword equipped. There are 3 enemies. 2 melee and 1 ranged. The ranged one stands on a platform above the player.

The 2 melee enemies charge the player, head on. It will take a moment for the melee enemies to reach the player, so the obvious choice is to fire at the ranged enemy first. Click drag towards the enemy, direct precision is not important, and press the medium ranged rifel button. Boom. The ranged enemy is dead (In this scenario he’s dead. When it’s more difficult, he’s just be incapacitated or weakened). The melee enemies have reached the player. If the player does not react fast enough, he will take damage from the first melee enemy. This is where the player needs to learn to fight in quick succession. Click-drag towards the melee enemies, hit the sword button. Then, the same thing again to the second melee enemy. This scenario would result in a 3x combo and if there were no more enemies remaining on the stage, the player would receive the combat bonuses .. currency, health, whatever. 

3. Proof of Concept / Demo

In order to begin investing our time into a game, we need to actually make something. It just needs to have an ounce of our total ambition. It’s broken down into frames like a megaman game. When, the player reaches the top, left, or right of the frame, the camera shifts to the next frame. Here’s what I have in mind:

Frame 1:

Ok, there’s this guy. He lives in a city, as guys do. The demo starts in his apartment. He hops out the window onto the fire escape. He climbs up to roof by jumping up the fire escape platforms or climbing up ladders. 

(However, as I flesh it out in my head it may work better from a perspective similar to original Zelda or Stardew Valley.)

Frame 2:

On the roof, he encounters an NPC, quest-giver. Dialogue exchange:

Quest-giver: “Would you grab me a pack of smokes? I have some intel I can trade you for em.”

Player: Dialogue Options: 1. “Sure.” 2. “Get your own damn cigarettes.”

Quest-giver: 1. “Thanks. Meet me outside the (some location). And take this, it’s dangerous out there.” (He hands the player a sword) 2. “Man, I thought we were cool.”

The player walks right and encounters a vending machine where he buys a gun (Obviously this could be a choice in a more-fleshed out version of the game). Depending on if the player got the sword from the quest-giver, he picks up a baseball bat from the ground next to the vending machine. He walks on to the right.

Frame 3: 

He sees 3 goblin-like enemies, 2 melee and 1 ranged. They see the player and engage in combat. The combat plays out like the scenario described in section 2 of this document. After winning, the player receives a reward.

Frame 4:

The player reaches the end of the rooftop and climbs a ladder or slides down a pole to the street level. 

Frame 5:

There’s a ramen shop on the street level that he can enter. Next door to the ramen shop is a convenience store where the player can buy the cigarettes. 

Ramen Shop Interior:

If the player enters the ramen shop he overhears some dialogue from 2 NPCs sitting at the counter. They talk about some opportunity to make money (Specific information is unimportant for the purposes of this demo). This part can be skipped entirely by the player. 

Convenience Store Interior:

The player can approach the counter and buy cigarettes.

End

The player backtracks to the initial NPC and upon giving him the cigarettes he tells the player about an opportunity to make money; The same information the player learned in the ramen shop if the player chose to enter.

-If the player did not enter the ramen shop, then the demo ends.
-If the player already knew the intel, then the demo presents the player with 2 dialogue options: 1. “Thanks, I’ll look into it.” 2. “Waste of my time! I knew that.” Either option results in the demo ending. 

The purpose of the multiple options is to experiment with potential branching paths.

4. Story Concept

I’ll dig into this soon … 
